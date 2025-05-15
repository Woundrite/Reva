from Reva.EventSystem.Events.Events import Event, EventType, EventCategory
import glfw
import os
from datetime import datetime
from typing import Optional, Union

"""
This module contains the FSEvent class, which is used to represent file system events.
The FSEvent class inherits from the Event class and provides additional functionality
To be implemented:
	- FSEVENT_CREATE
	- FSEVENT_DELETE
	- FSEVENT_MODIFY
	- FSEVENT_RENAME
"""

class FSEvent(Event):
	"""
	FSEvent class for file system events.
	"""
	def __init__(self, event_type: str, data: Optional[Union[str, bytes]] = None, timestamp: Optional[datetime] = datetime.now()):
		if not isinstance(event_type, EventType):
			raise TypeError("EventType must be an instance of EventType")
		if data is not None and not isinstance(data, (str, bytes)):
			raise TypeError("data must be a string or bytes")
		if not isinstance(timestamp, datetime):
			raise TypeError("timestamp must be of type datetime")
		
		super().__init__(EventCategory.FSEVENT, timestamp)
		self.EventType = event_type
		self.data = data

class FSEventCreate(FSEvent):
	"""
	FSEvent class for file system create events.
	"""
	def __init__(self, path: str, timestamp: Optional[datetime] = datetime.now()):
		if not isinstance(path, str):
			raise TypeError("path must be a string")
		if not os.path.exists(path):
			raise FileNotFoundError(f"Path {path} does not exist")
		
		super().__init__(EventType.FSEVENT_CREATE, path, timestamp)
		self.path = path