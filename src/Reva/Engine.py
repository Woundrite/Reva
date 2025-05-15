import imgui
import OpenGL.GL as gl
from Reva.Window import *
from Reva.EventSystem import *
import glfw
from Reva.Utils.logger import Logger

class Engine:
	def __init__(self, title: str, size: list[int]):
		self.title = title
		self.size = size
		self.window = Window(size[0], size[1], title)
		self.Logger = Logger()
		self.Logger.debug("Engine initialized.")
		self.EventSystem = EventSystem(logger=self.Logger)
		self.LayerHandler = LayerHandler(logger=self.Logger)
		self.setupCallbacks()
		self.EventSystem.dispatch
		# self.Mouse = Mouse()
		# self.Keyboard = Keyboard()
		self.deltatime = 0.0

	def onEvent(self, event):
		self.LayerHandler.onEvent(event)
		self.EventSystem.dispatch(event)
		# self.Logger.debug(event)
	
	@event_listener(EventType.WINDOW_CLOSE)
	def onWindowClose(self, event):
		try:
			self.window.terminate()
			self.Logger.warning("Window closed.")
			return True
		except Exception as e:
			self.Logger.error(f"Error closing window: {e}")
			return False
	
	def __del__(self):
		self.window.terminate()

	def setupCallbacks(self):
		self.window.set_window_size_callback(lambda window, width, height: self.onEvent(WindowEvent(EventType.WINDOW_RESIZE, width, height)))
		self.window.set_key_callback(lambda window, key, scancode, action, mods: self.onEvent(self.__genKeyEvent(window, key, scancode, action, mods)))
		self.window.set_mouse_button_callback(lambda window, button, action, mods: self.onEvent(self.__getMouseButtonEvent(window, button, action, mods)))
		self.window.set_cursor_pos_callback(lambda window, x, y: self.onEvent(self.__getMouseMoveEvent(window, x, y)))
		self.window.set_scroll_callback(lambda window, xoffset, yoffset: self.onEvent(self.__getMouseScrollEvent(window, EventType.MOUSE_SCROLL, xoffset, yoffset)))
		self.window.set_window_close_callback(lambda window: self.onEvent(WindowCloseEvent()))
		self.window.set_window_focus_callback(lambda window, focused: self.onEvent(WindowFocusEvent(focused)))
		# self.window.set_window_move_callback(lambda window, x, y: self.onEvent(WindowMoveEvent(x, y)))
		self.window.set_window_resize_callback(lambda window, width, height: self.onEvent(WindowResizeEvent(width, height)))
	
	def run(self):
		while not self.window.should_close():
			self.window.poll_events()
			self.window.swap_buffers()

	def __getMouseButtonEvent(self, window, key, action, mods):
		x, y = glfw.get_cursor_pos(window)
		if action == glfw.PRESS:
			return MouseButtonEvent(event_type = EventType.MOUSE_BUTTON_PRESS, button=key, mods=mods, x = x, y= y)
		elif action == glfw.RELEASE:
			return MouseButtonEvent(event_type = EventType.MOUSE_BUTTON_RELEASE, button=key, mods=mods, x = x, y= y)
	
	def __getMouseMoveEvent(self, window, x, y):
		return MouseMoveEvent(x=x, y=y)
	
	def __getMouseScrollEvent(self, window, xoffset, yoffset):
		print(f"Mouse Scroll: {xoffset}, {yoffset}")
		x, y = glfw.get_cursor_pos(window)
		return MouseScrollEvent(xoffset=xoffset, yoffset=yoffset)
		# elif action == glfw.ENTER:
		# 	self.onEvent(MouseEvent(EventType.MOUSE_ENTER, key, mods))
		# elif action == glfw.LEAVE:
		# 	self.onEvent(MouseEvent(EventType.MOUSE_LEAVE, key, mods))
		# elif action == glfw.DRAG:
		# 	self.onEvent(MouseEvent(EventType.MOUSE_DRAG, key, mods))

	def __genKeyEvent(self, window, key, scancode, action, mods):
		if action == glfw.PRESS:
			return KeyEvent(EventType.KEY_PRESS, key, scancode, mods)
		elif action == glfw.RELEASE:
			return KeyEvent(EventType.KEY_RELEASE, key, scancode, mods)
		elif action == glfw.REPEAT:
			return KeyEvent(EventType.KEY_REPEAT, key, scancode, mods)