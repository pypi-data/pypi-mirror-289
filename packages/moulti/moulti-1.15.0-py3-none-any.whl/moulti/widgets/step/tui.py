import os
import selectors
from queue import Queue, Empty
from time import monotonic_ns
from typing import Any, Callable
from textual import work
from textual.app import ComposeResult
from textual.worker import get_current_worker
from rich.text import Text
from . import MOULTI_PASS_DEFAULT_READ_SIZE
from ..collapsiblestep.tui import CollapsibleStep
from ..moultilog import MoultiLog

ANSI_ESCAPE_SEQUENCE = '\x1b'

class ThrottledAppender:
	"""
	This class uses Textual's call_from_thread() to schedule calls to "step.append(buffer)" inside Textual's asyncio
	event loop in a thread-safe manner. These calls are throttled so as not to flood the event loop.
	"""
	def __init__(self, step: 'Step', delay_ms: int):
		self.step = step
		self.call_from_thread = step.app.call_from_thread
		self.delay_ns = delay_ms * 1_000_000
		self.buffers: list[list[bytes]] = []
		self.last_append = 0

	def new_data(self, buffer: list[bytes], force: bool = False) -> None:
		self.buffers.append(buffer)
		self.append(force)

	def append(self, force: bool = False) ->  None:
		if self.buffers:
			now = monotonic_ns()
			if force or (now - self.last_append >= self.delay_ns):
				if buffered_string := b''.join([c for b in self.buffers for c in b]).decode('utf-8', errors='surrogateescape'):
					self.call_from_thread(self.step.append, buffered_string)
				self.buffers.clear()
				self.last_append = now

class Step(CollapsibleStep):
	"""
	This widget represents a step in a script, program or process.
	Visually speaking, it is essentially a collapsible text area surrounded
	with optional text lines.
	"""

	BINDINGS = [
		("c", "to_clipboard(False)", "Copy"),
		("w", "to_clipboard(True)", "With colors"),
	]

	def __init__(self, id: str, **kwargs: str|int|bool): # pylint: disable=redefined-builtin
		self.log_widget = MoultiLog(highlight=False)

		self.min_height = 1
		self.max_height = 25

		super().__init__(id=id, **kwargs)

		self.color = ''

	def cli_action_append(self, kwargs: dict[str, Any], helpers: dict[str, Any]) -> tuple:
		if 'text' not in kwargs:
			helpers['reply'](done=False, error='missing text for append operation')
			return ()
		return self.append, '\n'.join(kwargs['text'])

	def cli_action_clear(self, _kwargs: dict[str, str|int|bool], _helpers: dict[str, Any]) -> tuple:
		return self.clear, # pylint: disable=trailing-comma-tuple

	def subcompose(self) -> ComposeResult:
		yield self.log_widget

	def update_properties(self, kwargs: dict[str, str|int|bool]) -> None:
		super().update_properties(kwargs)
		if 'text' in kwargs:
			self.clear()
			self.append(str(kwargs['text']))
		if 'min_height' in kwargs:
			self.min_height = int(kwargs['min_height'])
		if 'max_height' in kwargs:
			self.max_height = int(kwargs['max_height'])
		self.log_widget.styles.min_height = self.min_height
		self.log_widget.styles.max_height = self.max_height if self.max_height > 0 else None

	def export_properties(self) -> dict[str, Any]:
		prop = super().export_properties()
		prop['min_height'] = self.min_height
		prop['max_height'] = self.max_height
		return prop

	def save(self, opener: Callable[[str, int], int], filename: str, extra_properties: dict[str, Any]) -> None:
		super().save(opener, filename, extra_properties)
		filename = filename + '.contents.log'
		with open(filename, 'w', encoding='utf-8', errors='surrogateescape', opener=opener) as contents_filedesc:
			self.log_widget.to_file(contents_filedesc)

	@CollapsibleStep.copy_to_clipboard
	def action_to_clipboard(self, keep_styles: bool = True) -> tuple[bool, str, str]:
		lines = list(self.log_widget.to_lines(keep_styles))
		lines_count = len(lines)
		lines.append('') # add an extra \n
		data = '\n'.join(lines)
		return True, data, f'copied {lines_count} lines, {len(data)} characters to clipboard'

	def clear(self) -> None:
		self.log_widget.clear()
		self.color = ''

	def append(self, text: str) -> None:
		# RichLog does not handle partial lines and thus always adds a trailing \n; therefore, we must strip one (and
		# only one) trailing \n, if present:
		if text and text[-1] == '\n':
			text = text[:-1]
		# If necessary, prepend the ANSI escape code for the color inherited from the last line:
		if self.color:
			text = self.color + text
		# Deal with colored text; the text_to_write variable is made necessary by mypy.
		text_to_write: str | Text = text
		if ANSI_ESCAPE_SEQUENCE in text:
			# Convert text and an extra character from ANSI to Rich Text
			text_to_write = Text.from_ansi(text + '_')
			# The extra character reflects the color the next line should inherit:
			self.color = Step.last_character_color(text_to_write)
			# Strip the extra character:
			text_to_write.right_crop(1)
		self.log_widget.write(text_to_write)
		self.activity()

	@classmethod
	def last_character_color(cls, text: Text) -> str:
		# If the last span (if any) covers the last character...
		if text.spans and text.spans[-1].end == len(text):
			# ... return the ANSI escape code for its color:
			style = text.spans[-1].style
			assert not isinstance(style, str) # prevent calling render() on str
			return style.render('_').split('_')[0]
		return ''

	def cli_action_pass(self, kwargs: dict[str, str|int|bool], helpers: dict[str, Any]) -> tuple:
		if not helpers['file_descriptors']:
			helpers['reply'](done=False, error='missing file descriptor for pass operation')
			return ()
		# Set up a queue between two workers:
		# - one that reads data from the file descriptor and replies to the client;
		# - one that appends lines to the step.
		queue: Queue = Queue()
		self.append_from_queue(queue, helpers)
		self.append_from_file_descriptor_to_queue(queue, kwargs, helpers)
		return ()

	@work(thread=True)
	async def append_from_file_descriptor_to_queue(
		self,
		queue: Queue,
		kwargs: dict[str, Any],
		helpers: dict[str, Any],
	) -> None:
		current_worker = get_current_worker()
		error = None
		try:
			file_descriptor = helpers['file_descriptors'][0]
			assert isinstance(file_descriptor, int)
			# Although this thread is dedicated to reading from a single file descriptor, it should:
			# - not block indefinitely on a read()
			# - check is_cancelled at regular intervals
			# This ensures Moulti exits correctly.
			# To this end, use non-blocking mode along with a select()-like interface:
			os.set_blocking(file_descriptor, False)
			output_selector = selectors.DefaultSelector()
			try:
				output_selector.register(file_descriptor, selectors.EVENT_READ)
				def can_read() -> bool:
					return bool(output_selector.select(0.5))
			except Exception:
				# register() may fail: for instance, on Linux, epoll() does not support regular files and returns EPERM.
				def can_read() -> bool:
					return True
			# Read binary data from the given file descriptor using a FileIO (raw binary stream whose methods only make
			# one system call):
			with os.fdopen(file_descriptor, mode='rb', buffering=0) as binary_stream:
				read_size = int(kwargs.get('read_size', MOULTI_PASS_DEFAULT_READ_SIZE))
				if read_size <= 0:
					read_size = MOULTI_PASS_DEFAULT_READ_SIZE
				end_of_file = False
				# Outer loop: check for worker cancellation and rely on select() to detect activity:
				while not current_worker.is_cancelled and not end_of_file:
					if can_read():
						# Inner loop: read data until it would block, keep checking for worker cancellation:
						# "If the object is in non-blocking mode and no bytes are available, None is returned."
						while (data := binary_stream.read(read_size)) is not None:
							# "If 0 bytes are returned, and size was not 0, this indicates end of file."
							if not data:
								end_of_file = True
								break
							queue.put_nowait(data)
							if current_worker.is_cancelled:
								break
				queue.put_nowait(None)
		except Exception as exc:
			error = str(exc)
			helpers['debug'](f'pass: {error}')
		helpers['reply'](done=error is None, error=error)

	@work(thread=True)
	async def append_from_queue(self, queue: Queue, helpers: dict[str, Any]) -> None:
		current_worker = get_current_worker()
		self.prevent_deletion += 1
		try:
			throttling_ms = 25
			throttling_s = throttling_ms / 1000
			appender = ThrottledAppender(self, throttling_ms)
			buffer = []
			while True:
				if current_worker.is_cancelled:
					break
				try:
					data = queue.get(block=True, timeout=throttling_s)
					if data is not None:
						# Buffer data to avoid queuing partial lines as, down the
						# line, RichLog.write() only handles complete lines:
						# look for the position of \n from the end of the string :
						eol = data.rfind(b'\n')
						if eol == -1: # no \n found, buffer the whole string:
							buffer.append(data)
						else:
							before = data[:eol+1]
							after = data[eol+1:]
							buffer.append(before)
							appender.new_data(buffer)
							buffer = []
							if after:
								buffer.append(after)
					else: # Reached EOF: flush buffer and exit:
						appender.new_data(buffer, True)
						break
				except Empty:
					# No data: there may be data left in the appender's buffer:
					appender.append(True)
		except Exception as exc:
			helpers['debug'](f'append_from_queue: {exc}')
		finally:
			self.prevent_deletion -= 1

	DEFAULT_CSS = CollapsibleStep.DEFAULT_CSS + """
	Step {
		& MoultiLog {
			scrollbar-corner-color: $step_default;
		}
		&.success {
			& MoultiLog { scrollbar-corner-color: $step_success; }
		}
		&.warning {
			& MoultiLog { scrollbar-corner-color: $step_warning; }
		}
		&.error {
			& MoultiLog { scrollbar-corner-color: $step_error; }
		}
	}
	"""
MoultiWidgetClass = Step
