from enum import Enum, auto
from typing import Optional, Union
from datetime import datetime
import glfw

class CustomEvent(Event):
	"""
	Custom event class.
	"""
	def __init__(self, event_type: str, data: Optional[Union[str, int, float]] = None, timestamp: Optional[datetime] = datetime.now()):
		if not isinstance(event_type, EventType):
			raise TypeError("EventType must be an instance of EventType")
		if data is not None and not isinstance(data, (str, int, float)):
			raise TypeError("data must be a string, integer or float")
		if not isinstance(timestamp, datetime):
			raise TypeError("timestamp must be of type datetime")
		
		super().__init__(EventCategory.CUSTOM, timestamp)
		self.EventType = event_type
		self.data = data

	def __repr__(self):
		return f"CustomEvent(EventType={self.EventType}, data={self.data})"

	def __str__(self):
		return f"CustomEvent: {self.EventType} ({self.data})"
	
	def is_EventType(self, EventType: str) -> bool:
		"""
		Checks if the EventType matches the event EventType.
		"""
		return self.EventType == EventType

class UndefinedEvent:
	"""
	Undefined event class.
	"""
	def __init__(self, event_type: str, timestamp: Optional[datetime] = datetime.now(), **kwargs):
		if not isinstance(event_type, str):
			raise TypeError("event_type must be a string")
		if not isinstance(timestamp, datetime):
			raise TypeError("timestamp must be of type datetime")

		super().__init__(EventCategory.UNDEFINED, timestamp)
		self.event_type = event_type
		self.kwargs = kwargs

	def __repr__(self):
		return f"UndefinedEvent(type={self.event_type}, \n\t\targs={self.kwargs})"

	def __str__(self):
		return f"UndefinedEvent: {self.event_type}\n\t\targs={self.kwargs}"