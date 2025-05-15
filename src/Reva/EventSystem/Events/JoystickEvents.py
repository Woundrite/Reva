from Reva.EventSystem.Events.Events import Event, EventType, EventCategory
import glfw
from datetime import datetime
from typing import Optional, Union

"""
This module contains the GUIEvent class, which is used to represent GUI events.
The GUIEvent class inherits from the Event class and provides additional functionality
To be implemented:
	- JOYSTICK_BUTTON_PRESS
	- JOYSTICK_BUTTON_RELEASE
	- JOYSTICK_AXIS_MOVE
	- JOYSTICK_HAT_MOVE
"""

class JoystickEvent(Event):
	"""
	Joystick event class.
	"""
	def __init__(self, joystick_id: int, event_type: str, axis: Optional[int] = None, value: Optional[float] = None, timestamp: Optional[datetime] = datetime.now()):
		if not isinstance(joystick_id, int):
			raise TypeError("joystick_id must be an integer")
		if not isinstance(event_type, EventType):
			raise TypeError("EventType must be an instance of EventType")
		if axis is not None and not isinstance(axis, int):
			raise TypeError("axis must be an integer")
		if value is not None and not isinstance(value, (int, float)):
			raise TypeError("value must be a number")
		if not isinstance(timestamp, datetime):
			raise TypeError("timestamp must be of type datetime")
		
		
		super().__init__(EventCategory.JOYSTICK, timestamp)
		self.joystick_id = joystick_id
		self.EventType = event_type
		self.axis = axis
		self.value = value

	def __repr__(self):
		return f"JoystickEvent(joystick_id={self.joystick_id}, EventType={self.EventType}, axis={self.axis}, value={self.value})"

	def __str__(self):
		return f"JoystickEvent: {self.joystick_id} {self.EventType} ({self.axis}, {self.value})"
