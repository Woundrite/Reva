from enum import Enum, auto
from typing import Optional, Union
from datetime import datetime
import glfw

class EventType(Enum):
	# Keyboard EventTypes
	KEY_PRESS = auto()
	KEY_RELEASE = auto()
	KEY_REPEAT = auto()

	# Mouse EventTypes
	MOUSE_BUTTON_PRESS = auto()
	MOUSE_BUTTON_RELEASE = auto()
	MOUSE_BUTTON_DOWN = auto()
	MOUSE_MOVE = auto()
	MOUSE_SCROLL = auto()
	MOUSE_ENTER = auto()
	MOUSE_LEAVE = auto()
	MOUSE_DRAG = auto()

	# Window EventTypes
	WINDOW_RESIZE = auto()
	WINDOW_CLOSE = auto()
	WINDOW_MINIMIZE = auto()
	WINDOW_MAXIMIZE = auto()
	WINDOW_RESTORE = auto()
	WINDOW_FOCUS = auto()
	WINDOW_UNFOCUS = auto()
	WINDOW_MOVE = auto()

	# IMGUI EventTypes (to be implemented)

	# Game EventTypes (custom events)
	USER_EVENT = auto()
	COMPONENT_ADD = auto()
	COMPONENT_REMOVE = auto()
	SAVE = auto()
	LOAD = auto()
	QUIT = auto()
	PAUSE = auto()
	RESUME = auto()
	
	# Custom EventTypes (to be defined by the user)
	CUSTOM = auto()

	# Joystick EventTypes (to be implemented)
	JOYSTICK_BUTTON_PRESS = auto()
	JOYSTICK_BUTTON_RELEASE = auto()
	JOYSTICK_AXIS_MOVE = auto()
	JOYSTICK_HAT_MOVE = auto()
	
	# Touch EventTypes (to be implemented)
	TOUCH_PRESS = auto()
	TOUCH_RELEASE = auto()
	TOUCH_MOVE = auto()
	TOUCH_SCROLL = auto()

	# File System EventTypes (to be implemented)
	FSEVENT_CREATE = auto()
	FSEVENT_DELETE = auto()
	FSEVENT_MODIFY = auto()
	FSEVENT_RENAME = auto()
	
	# Engine EventTypes (to be implemented): (for when an engine event occurs such as a setting is changed, or something is added to the scene, etc.)
	ENGINE_START = auto()
	ENGINE_STOP = auto()
	ENGINE_UPDATE = auto()
	ENGINE_RENDER = auto()
	ENGINE_SETTINGS_CHANGE = auto()
	ENGINE_SCENE_CHANGE = auto()
	ENGINE_SCENE_OBJECT_ADD = auto()
	ENGINE_SCENE_OBJECT_REMOVE = auto()
	ENGINE_MODIFY = auto()

	# Network EventTypes (to be implemented): (for when a network event occurs such as a connection is made, or data is received, etc.)
	NETWORK_CONNECT = auto()
	NETWORK_DISCONNECT = auto()
	NETWORK_DATA_RECEIVED = auto()
	NETWORK_DATA_SENT = auto()

	# Audio EventTypes (to be implemented): (for when an audio event occurs such as a sound is played, or a sound is stopped, etc.)
	AUDIO_PLAY = auto()
	AUDIO_STOP = auto()
	AUDIO_PAUSE = auto()
	AUDIO_RESUME = auto()

	# Video EventTypes (to be implemented): (for when a video event occurs such as a video is played, or a video is stopped, etc.)
	VIDEO_PLAY = auto()
	VIDEO_STOP = auto()
	VIDEO_PAUSE = auto()
	VIDEO_RESUME = auto()

	# Multiwork EventTypes (to be implemented): 
	# (for when a 2 people are working on the same project, and one of them makes a change, the other persons project 
	# is updated (usually will be acompanied by another necessary event such as a file system event , a network event, etc))
	MULTIWORK_UPDATE = auto()

	# Undefined EventTypes
	UNDEFINED = auto()

class EventCategory(Enum):
	# Keyboard EventTypes
	KEYBOARD = auto()

	# Mouse EventTypes
	MOUSE = auto()

	# Window EventTypes
	WINDOW = auto()

	# IMGUI EventTypes (to be implemented)
	IMGUI = auto()

	# Game EventTypes (custom events)
	GAME = auto()

	# Custom EventTypes (to be defined by the user)
	CUSTOM = auto()

	# Joystick EventTypes (to be implemented)
	JOYSTICK = auto()

	# Touch EventTypes (to be implemented)
	TOUCH = auto()

	# File System EventTypes (to be implemented)
	FSEVENT = auto()
	
	# Engine EventTypes (to be implemented): (for when an engine event occurs such as a setting is changed, or something is added to the scene, etc.)
	ENGINE = auto()

	# Network EventTypes (to be implemented): (for when a network event occurs such as a connection is made, or data is received, etc.)
	NETWORK= auto()

	# Audio EventTypes (to be implemented): (for when an audio event occurs such as a sound is played, or a sound is stopped, etc.)
	AUDIO = auto()

	# Video EventTypes (to be implemented): (for when a video event occurs such as a video is played, or a video is stopped, etc.)
	VIDEO = auto()

	# Multiwork EventTypes (to be implemented): 
	MULTIWORK = auto()

	# Undefined EventTypes
	UNDEFINED = auto()

class Event:
	"""
	Base class for all events.
	"""
	def __init__(self, event_type: EventCategory, timestamp: Optional[datetime] = datetime.now()):
		if not isinstance(event_type, EventCategory):
			raise TypeError("event_type must be of type EventCategory")
		self.event_type = event_type
		self.__handled = False
		self.timestamp = timestamp

	def __repr__(self):
		return f"Event(type={self.event_type})"

	def __str__(self):
		return f"Event: {self.event_type}"
	
	def is_handled(self) -> bool:
		"""
		Checks if the event has been handled.
		"""
		return self.__handled
	
	def set_handled(self, handled: bool) -> None:
		"""
		Sets the handled state of the event.
		"""
		if not isinstance(handled, bool):
			raise TypeError("handled must be a boolean")
		self.__handled = handled
	
	def get_timestamp(self) -> datetime:
		"""
		Gets the timestamp of the event.
		"""
		return self.timestamp
	
	def set_timestamp(self, timestamp: datetime) -> None:
		"""
		Sets the timestamp of the event.
		"""
		if not isinstance(timestamp, datetime):
			raise TypeError("timestamp must be of type datetime")
		self.timestamp = timestamp

	def get_event_type(self) -> EventCategory:
		"""
		Gets the event type of the event.
		"""
		return self.event_type
	
	def is_event_type(self, event_type: EventCategory) -> bool:
		"""
		Checks if the event type matches the event type.
		"""
		if not isinstance(event_type, EventCategory):
			raise TypeError("event_type must be of type EventCategory")
		return self.event_type == event_type
	