from Reva.EventSystem.Events.Events import Event, EventType, EventCategory
import glfw
from datetime import datetime
from typing import Optional, Union

class KeyEvent(Event):
	"""
	Key event class.
	"""
	def __init__(self, event_type: str, key: int, scancode: int, mods: int, timestamp: Optional[datetime] = datetime.now()):
		if not isinstance(timestamp, datetime):
			raise TypeError("timestamp must be of type datetime")
		if not isinstance(key, int):
			raise TypeError("key must be an integer")
		if not isinstance(scancode, int):
			raise TypeError("key must be an integer")
		if not isinstance(mods, int):
			raise TypeError("key must be an integer")
		if not isinstance(event_type, EventType):
			raise TypeError("EventType must be an instance of EventType")
		

		super().__init__(EventCategory.KEYBOARD, timestamp)
		self.key = key
		self.EventType = event_type
		self.scancode = scancode
		self.mods = mods

	def __repr__(self):
		return f"KeyEvent(key={self.key}, mods={self.mods}, scancode={self.scancode}, EventType={self.EventType})"

	def __str__(self):
		return f"KeyEvent: key={self.key} mods={self.mods} scancode={self.scancode} EventType={self.EventType}"

	def get_key_name(self) -> int:
		"""
		Gets the key of the event.
		"""
		return glfw.get_key_name(self.key)
	
	def is_pressed(self) -> bool:
		"""
		Checks if the key is pressed.
		"""
		return self.EventType == EventType.KEY_PRESS
	
	def is_released(self) -> bool:
		return self.EventType == EventType.KEY_RELEASE

	def is_down(self) -> bool:
		"""
		Checks if the key is held down.
		"""
		return self.EventType == EventType.KEY_DOWN
	
	def is_key_down(self, key: str) -> bool:
		"""
		Checks if the key is down.
		"""
		return self.key == key and self.is_down()
	
	def is_key_up(self, key: str) -> bool:
		"""
		Checks if the key is up.
		"""
		return self.key == key and self.is_released()
	
	def is_key_pressed(self, key: str) -> bool:
		"""
		Checks if the key is up.
		"""
		return self.key == key and self.is_pressed()
	