from Reva.EventSystem.Events.Events import Event, EventType, EventCategory
import glfw
from datetime import datetime
from typing import Optional, Union
	
class WindowEvent(Event):
	"""
	Window event class.
	"""
	def __init__(self, event_type: str, width: int, height: int, timestamp: Optional[datetime] = datetime.now()):
		if not isinstance(timestamp, datetime):
			raise TypeError("timestamp must be of type datetime")
		if not isinstance(event_type, EventType):
			raise TypeError("EventType must be an instance of EventType")
		if not isinstance(width, int) or not isinstance(height, int):
			raise TypeError("width and height must be integers")


		super().__init__(EventCategory.WINDOW, timestamp)
		self.EventType = event_type
		self.width = width
		self.height = height

	def __repr__(self):
		return f"WindowEvent(EventType={self.EventType}, width={self.width}, height={self.height})"

	def __str__(self):
		return f"WindowEvent: {self.EventType} ({self.width}, {self.height})"

class WindowCloseEvent(WindowEvent):
	"""
	Window close event class.
	"""
	def __init__(self, timestamp: Optional[datetime] = datetime.now()):
		super().__init__(EventType.WINDOW_CLOSE, 0, 0, timestamp)

class WindowResizeEvent(WindowEvent):
	"""
	Window resize event class.
	"""
	def __init__(self, width: int, height: int, timestamp: Optional[datetime] = datetime.now()):
		super().__init__(EventType.WINDOW_RESIZE, width, height, timestamp)

class WindowFocusEvent(WindowEvent):
	"""
	Window focus event class.
	"""
	def __init__(self, focused: bool, timestamp: Optional[datetime] = datetime.now()):
		super().__init__(EventType.WINDOW_FOCUS if focused else EventType.WINDOW_UNFOCUS, 0, 0, timestamp)
		self.focused = focused

class WindowMoveEvent(WindowEvent):
	"""
	Window move event class.
	"""
	def __init__(self, x: int, y: int, timestamp: Optional[datetime] = datetime.now()):
		super().__init__(EventType.WINDOW_MOVE, x, y, timestamp)
		self.x = x
		self.y = y