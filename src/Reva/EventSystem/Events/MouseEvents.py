from Reva.EventSystem.Events.Events import Event, EventType, EventCategory
import glfw
from datetime import datetime
from typing import Optional, Union
from numbers import Number


class MouseEvent(Event):
	"""
	Mouse event class.
	"""
	def __init__(self, event_type: EventType, x: float = 0, y: float = 0, timestamp: Optional[datetime] = datetime.now()):
		"""Generates a mouse event.
		Generates a mouse event with the given event type, button, x and y coordinates, and timestamp.

		Args:
			event_type (EventType): event type (EventType.MOUSE_BUTTON_PRESS, EventType.MOUSE_BUTTON_RELEASE, EventType.MOUSE_MOVE, EventType.MOUSE_SCROLL, EventType.MOUSE_ENTER, EventType.MOUSE_LEAVE, EventType.MOUSE_DRAG).
			mods (int, optional): the additional modifications (shift, alt, ctrl, etc.). Defaults to 0.
			x (float, optional): X position of event. Defaults to 0.
			y (float, optional): Y position of event. Defaults to 0.
			xoffset (float, optional): X offset of event. Defaults to 0.
			yoffset (float, optional): Y offset of event. Defaults to 0.
			timestamp (Optional[datetime], optional): _description_. Defaults to datetime.now().

		Raises:
			TypeError: if event_type is not of type EventType
			TypeError: if x is not a number
			TypeError: if y is not a number
			TypeError: if timestamp is not of type datetime
		"""
		if not isinstance(event_type, EventType):
			raise TypeError("EventType must be an instance of EventType")
		if not isinstance(x, (Number, int, float)) or not isinstance(y, (Number, int, float)):
			raise TypeError("x and y must be numbers")
		if not isinstance(timestamp, datetime):
			raise TypeError("timestamp must be of type datetime")
		
		super().__init__(EventCategory.MOUSE, timestamp)
		self.EventType = event_type
		self.x = x
		self.y = y

	def __repr__(self):
		return f"MouseEvent(EventType={self.EventType}, x={self.x}, y={self.y})"

	def __str__(self):
		return f"MouseEvent: EventType={self.EventType} x={self.x} y={self.y}"
	

class MouseButtonEvent(MouseEvent):

	def __init__(self, event_type: EventType, button: int, mods:int = 0, x: float = 0, y: float = 0, timestamp: Optional[datetime] = datetime.now()):
		"""
		Generates a mouse button event.
		Generates a mouse button event with the given event type, button, x and y coordinates, and timestamp.

		Args:
			event_type (EventType): event type (EventType.MOUSE_BUTTON_PRESS, EventType.MOUSE_BUTTON_RELEASE).
			button (int): button number (1 for left, 2 for middle, 3 for right).
			x (float, optional): X position of event. Defaults to 0.
			y (float, optional): Y position of event. Defaults to 0.
			timestamp (Optional[datetime], optional): _description_. Defaults to datetime.now().

		Raises:
			TypeError: if event_type is not of type EventType
			TypeError: if x is not a number
			TypeError: if y is not a number
			TypeError: if timestamp is not of type datetime
			TypeError: if button is not a number
			TypeError: if mods is not a number
		"""
		super().__init__(event_type, x=x, y=y, timestamp=timestamp)
		if not isinstance(button, int):
			raise TypeError("button must be an integer")
		if not isinstance(mods, int):
			raise TypeError("mods must be an integer")
		
		self.button = button
		self.mods = mods

	def is_pressed(self, button = None) -> bool:
		"""
		Checks if the mouse button is pressed.
		"""
		if button == None:
			return self.EventType == EventType.MOUSE_BUTTON_PRESS
		else:
			return self.EventType == EventType.MOUSE_BUTTON_PRESS and self.button == button
	
	def is_released(self, button = None) -> bool:
		"""
		Checks if the mouse button is released.
		"""
		if button == None:
			return self.EventType == EventType.MOUSE_BUTTON_RELEASE
		else:
			return self.EventType == EventType.MOUSE_BUTTON_RELEASE and self.button == button
	
	def is_down(self, button = None) -> bool:
		"""
		Checks if the mouse button is held down.
		"""
		if button == None:
			return self.EventType == EventType.MOUSE_BUTTON_DOWN
		else:
			return self.EventType == EventType.MOUSE_BUTTON_DOWN and self.button == button
	
	def __repr__(self):
		return f"MouseEvent(button={self.button}, EventType={self.EventType}, x={self.x}, y={self.y})"

	def __str__(self):
		return f"MouseEvent: button={self.button} EventType={self.EventType} x={self.x} y={self.y}"

class MouseMoveEvent(MouseEvent):
	def __init__(self, x: float, y: float, timestamp: Optional[datetime] = datetime.now()):
		"""
		Generates a mouse move event.
		Generates a mouse move event with the given x and y coordinates and timestamp.

		Args:
			x (float): X position of event.
			y (float): Y position of event.
			timestamp (Optional[datetime], optional): _description_. Defaults to datetime.now().

		Raises:
			TypeError: if x is not a number
			TypeError: if y is not a number
		"""
		super().__init__(EventType.MOUSE_MOVE, x=x, y=y, timestamp=timestamp)

class MouseScrollEvent(MouseEvent):
	def __init__(self, xoffset: float, yoffset: float, timestamp: Optional[datetime] = datetime.now()):
		"""
		Generates a mouse scroll event.
		Generates a mouse scroll event with the given x and y offsets and timestamp.

		Args:
			xoffset (float): X offset of event.
			yoffset (float): Y offset of event.
			timestamp (Optional[datetime], optional): _description_. Defaults to datetime.now().

		Raises:
			TypeError: if xoffset is not a number
			TypeError: if yoffset is not a number
		"""
		super().__init__(EventType.MOUSE_SCROLL, x=xoffset, y=yoffset, timestamp=timestamp)

class MouseEnterEvent(MouseEvent):
	def __init__(self, x: float, y: float, timestamp: Optional[datetime] = datetime.now()):
		"""
		Generates a mouse enter event.
		Generates a mouse enter event with the given x and y coordinates and timestamp.

		Args:
			x (float): X position of event.
			y (float): Y position of event.
			timestamp (Optional[datetime], optional): _description_. Defaults to datetime.now().

		Raises:
			TypeError: if x is not a number
			TypeError: if y is not a number
		"""
		super().__init__(EventType.MOUSE_ENTER, x=x, y=y, timestamp=timestamp)

class MouseLeaveEvent(MouseEvent):
	def __init__(self, x = 0, y = 0, timestamp = datetime.now()):
		"""
		Generates a mouse leave event.
		Generates a mouse leave event with the given x and y coordinates and timestamp.

		Args:
			x (float): X position of event.
			y (float): Y position of event.
			timestamp (Optional[datetime], optional): _description_. Defaults to datetime.now().

		Raises:
			TypeError: if x is not a number
			TypeError: if y is not a number
		"""
		super().__init__(EventType.MOUSE_LEAVE, x=x, y=y, timestamp=timestamp)

class MouseDragEvent(MouseEvent):
	def __init__(self, x: float, y: float, res=None, timestamp: Optional[datetime] = datetime.now()):
		"""
		Generates a mouse drag event.
		Generates a mouse drag event with the given x and y coordinates and timestamp.

		Args:
			x (float): X position of event.
			y (float): Y position of event.
			timestamp (Optional[datetime], optional): _description_. Defaults to datetime.now().

		Raises:
			TypeError: if x is not a number
			TypeError: if y is not a number
		"""
		self.res = res
		super().__init__(EventType.MOUSE_DRAG, x=x, y=y, timestamp=timestamp)