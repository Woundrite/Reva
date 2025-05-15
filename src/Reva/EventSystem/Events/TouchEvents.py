from Reva.EventSystem.Events.Events import Event, EventType, EventCategory
import glfw
from datetime import datetime
from typing import Optional, Union

	
class TouchEvent(Event):
	"""
	Touch event class.
	"""
	def __init__(self, event_type: str, x: float, y: float, timestamp: Optional[datetime] = datetime.now()):
		if not isinstance(event_type, EventType):
			raise TypeError("EventType must be an instance of EventType")
		if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
			raise TypeError("x and y must be numbers")
		if not isinstance(timestamp, datetime):
			raise TypeError("timestamp must be of type datetime")
		
		super().__init__(EventCategory.TOUCH, timestamp)
		self.EventType = event_type
		self.x = x
		self.y = y

	def __repr__(self):
		return f"TouchEvent(EventType={self.EventType}, x={self.x}, y={self.y})"

	def __str__(self):
		return f"TouchEvent: {self.EventType} ({self.x}, {self.y})"
	
	def is_pressed(self) -> bool:
		"""
		Checks if the touch is pressed.
		"""
		return self.EventType == EventType.TOUCH_PRESS
	
	def is_released(self) -> bool:
		"""
		Checks if the touch is released.
		"""
		return self.EventType == EventType.TOUCH_RELEASE
	
	def is_moved(self) -> bool:
		"""
		Checks if the touch is moved.
		"""
		return self.EventType == EventType.TOUCH_MOVE
	
	def is_scrolled(self) -> bool:
		"""
		Checks if the touch is scrolled.
		"""
		return self.EventType == EventType.TOUCH_SCROLL
	
	def is_touch_down(self, x: float, y: float) -> bool:
		"""
		Checks if the touch is down at the given coordinates.
		"""
		return self.x == x and self.y == y and self.is_pressed()
	
	def is_touch_up(self, x: float, y: float) -> bool:
		"""
		Checks if the touch is up at the given coordinates.
		"""
		return self.x == x and self.y == y and self.is_released()