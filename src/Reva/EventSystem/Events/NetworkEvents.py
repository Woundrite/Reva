from Reva.EventSystem.Events.Events import Event, EventType, EventCategory
import glfw
from datetime import datetime
from typing import Optional, Union

"""
This file defines the NetworkEvents class, which is an enumeration of various network-related events.
The NetworkEvents class inherits from the Event class and provides additional functionality
To be implemented:
	- NETWORK_CONNECT
	- NETWORK_DISCONNECT
	- NETWORK_DATA_RECEIVED
	- NETWORK_DATA_SENT
"""

class NetworkEvents(Event):
	"""
	NetworkEvents class is an enumeration of various network-related events.
	"""
	def __init__(self, event_type: EventType, timestamp: Optional[datetime] = datetime.now()):
		if not isinstance(event_type, EventType):
			raise TypeError("EventType must be an instance of EventType")
		if not isinstance(timestamp, datetime):
			raise TypeError("timestamp must be of type datetime")
		
		super().__init__(EventCategory.NETWORKEVENT, timestamp)
		self.EventType = event_type