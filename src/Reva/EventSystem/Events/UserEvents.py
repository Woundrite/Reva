from Reva.EventSystem.Events.Events import Event, EventType, EventCategory
import glfw
from datetime import datetime
from typing import Optional, Union, Any
from Reva.Utls.decor import deprecated


@deprecated
class UserEvent(Event):
	"""
	User event class.
	"""
	def __init__(self, event_type: str, data: Any = None, timestamp: Optional[datetime] = datetime.now()):
		if not isinstance(event_type, EventType):
			raise TypeError("EventType must be an instance of EventType")
		if data is not None and not isinstance(data, (str, int, float)):
			raise TypeError("data must be a string, integer or float")
		if not isinstance(timestamp, datetime):
			raise TypeError("timestamp must be of type datetime")
		
		
		super().__init__(EventCategory.GAME, timestamp)
		self.EventType = event_type
		self.data = data

	def __repr__(self):
		return f"UserEvent(EventType={self.EventType}, data={self.data})"

	def __str__(self):
		return f"UserEvent: {self.EventType} ({self.data})"
	
	def is_EventType(self, EventType: str) -> bool:
		"""
		Checks if the EventType matches the event EventType.
		"""
		return self.EventType == EventType