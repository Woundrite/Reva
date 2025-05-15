from Reva.EventSystem.Events.Events import Event, EventType, EventCategory
import glfw
from datetime import datetime
from typing import Optional, Union

"""
This module contains the GUIEvent class, which is used to represent GUI events.
The GUIEvent class inherits from the Event class and provides additional functionality
To be implemented:
	- ENGINE_START
	- ENGINE_STOP
	- ENGINE_UPDATE
	- ENGINE_RENDER
	- ENGINE_SETTINGS_CHANGE
	- ENGINE_SCENE_CHANGE
	- ENGINE_SCENE_OBJECT_ADD
	- ENGINE_SCENE_OBJECT_REMOVE
	- ENGINE_MODIFY
"""