from collections.abc import Callable
from Reva.EventSystem.Events import EventType, EventCategory, Event
import uuid
from collections import defaultdict, deque
from datetime import datetime

def event_listener(event_type: EventType):
	if not isinstance(event_type, EventType):
		raise TypeError("event_type must be of type EventType")
	def wrapper(func):
		if not callable(func):
			raise TypeError("func must be callable")
		ev = EventSystem()
		ev.bind(event_type, func)
		func._event_type = event_type
		return func
	return wrapper

class Delegate:
	def __init__(self):
		self._func = None

	def bind(self, func):
		self._func = func

	def unbind(self):
		self._func = None

	def invoke(self, *args, **kwargs):
		if self._func:
			return self._func(*args, **kwargs)

class MulticastDelegate:
	def __init__(self):
		self._listeners = []

	def add(self, func):
		self._listeners.append(func)

	def broadcast(self, event, *args, **kwargs):
		for f in self._listeners:
			if event.is_handled():
				break
			f(event, *args, **kwargs)

class EventSystem:
	_instance = None

	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super(EventSystem, cls).__new__(cls)
		
		return cls._instance
	
	def __init__(self, logger=None):
		self._events = defaultdict(MulticastDelegate)
		self._history = deque()
		self._logger = logger
		self._logger.debug("EventSystem initialized") if self._logger else None

	def bind(self, event_type, callback):
		self._logger.debug(f"Binding {event_type} to {callback}") if self._logger else None
		if not isinstance(event_type, EventType):
			raise ValueError("event_type must be an instance of EventType")
		self._events[event_type].add(callback)

	def dispatch(self, event, replicable=False):
		self._logger.debug(f"Dispatching event: {event}") if self._logger else None
		if not isinstance(event, Event):
			raise ValueError("event must be an instance of Event")
		
		self._history.append(event)
		self._events[event.get_event_type()].broadcast(event)

		if replicable:
			self.replicate_event(event)

	def replicate_event(self, event):
		# Placeholder for actual network logic
		print(f"[Network] Replicating event: {event.name} -> {event.data}")