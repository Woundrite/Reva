import glfw
import OpenGL.GL as gl

class Window:
	def __init__(self, width: int, height: int, title: str):
		if not glfw.init():
			raise Exception("GLFW cannot be initialized")
		
		glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
		glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
		glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

		glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)


		self.window = glfw.create_window(width, height, title, None, None)
		
		
		if not self.window:
			glfw.terminate()
			raise Exception("GLFW window cannot be created")
		
		glfw.make_context_current(self.window)

	def should_close(self) -> bool:
		return glfw.window_should_close(self.window)

	def swap_buffers(self):
		glfw.swap_buffers(self.window)

	def poll_events(self):
		glfw.poll_events()

	def terminate(self):
		try:
			glfw.terminate()
		except Exception as e:
			print(f"Error while terminating GLFW: {e}")
	
	def __getattr__(self, name):
		return getattr(self.window, name)
	
	def __setattr__(self, name, value):
		if name == "window":
			self.__dict__[name] = value
		else:
			setattr(self.window, name, value)
	
	def __del__(self):
		self.terminate()
	
	def set_vsync(self, value: bool):
		pass

	def set_key_callback(self, callback):
		glfw.set_key_callback(self.window, callback)
	
	def set_mouse_button_callback(self, callback):
		glfw.set_mouse_button_callback(self.window, callback)
	
	def set_cursor_pos_callback(self, callback):
		glfw.set_cursor_pos_callback(self.window, callback)
	
	def set_scroll_callback(self, callback):
		glfw.set_scroll_callback(self.window, callback)
	
	def set_window_size_callback(self, callback):
		glfw.set_window_size_callback(self.window, callback)
	
	def set_window_pos_callback(self, callback):
		glfw.set_window_pos_callback(self.window, callback)
	
	def set_window_close_callback(self, callback):
		glfw.set_window_close_callback(self.window, callback)

	def set_window_refresh_callback(self, callback):
		glfw.set_window_refresh_callback(self.window, callback)

	def set_window_iconify_callback(self, callback):
		glfw.set_window_iconify_callback(self.window, callback)
	
	def set_window_maximize_callback(self, callback):
		glfw.set_window_maximize_callback(self.window, callback)

	def set_window_focus_callback(self, callback):
		glfw.set_window_focus_callback(self.window, callback)

	def set_window_drop_callback(self, callback):
		glfw.set_drop_callback(self.window, callback)
	
	def set_window_user_pointer(self, pointer):
		glfw.set_window_user_pointer(self.window, pointer)

	def get_window_user_pointer(self):
		return glfw.get_window_user_pointer(self.window)

	def set_window_title(self, title: str):
		glfw.set_window_title(self.window, title)

	def get_window_title(self) -> str:
		return glfw.get_window_title(self.window)

	def set_window_size(self, width: int, height: int):
		glfw.set_window_size(self.window, width, height)

	def get_window_size(self) -> tuple[int, int]:
		return glfw.get_window_size(self.window)
	
	def set_window_pos(self, x: int, y: int):
		glfw.set_window_pos(self.window, x, y)

	def get_window_pos(self) -> tuple[int, int]:
		return glfw.get_window_pos(self.window)
	
	def set_window_aspect_ratio(self, numerator: int, denominator: int):
		glfw.set_window_aspect_ratio(self.window, numerator, denominator)

	def get_window_aspect_ratio(self) -> tuple[int, int]:
		return glfw.get_window_aspect_ratio(self.window)
	
	def set_window_opacity(self, opacity: float):
		glfw.set_window_opacity(self.window, opacity)

	def get_window_opacity(self) -> float:
		return glfw.get_window_opacity(self.window)
	
	def set_window_icon(self, icon: str):
		glfw.set_window_icon(self.window, icon)

	def get_window_icon(self) -> str:
		return glfw.get_window_icon(self.window)
	
	def set_window_monitor(self, monitor: str):
		glfw.set_window_monitor(self.window, monitor)

	def get_window_monitor(self) -> str:
		return glfw.get_window_monitor(self.window)
	
	def set_window_framebuffer_size(self, width: int, height: int):
		glfw.set_window_framebuffer_size(self.window, width, height)

	def get_window_framebuffer_size(self) -> tuple[int, int]:
		return glfw.get_window_framebuffer_size(self.window)
	
	def set_window_framebuffer_aspect_ratio(self, numerator: int, denominator: int):
		glfw.set_window_framebuffer_aspect_ratio(self.window, numerator, denominator)

	def get_window_framebuffer_aspect_ratio(self) -> tuple[int, int]:
		return glfw.get_window_framebuffer_aspect_ratio(self.window)
	
	def set_window_framebuffer_opacity(self, opacity: float):
		glfw.set_window_framebuffer_opacity(self.window, opacity)

	def get_window_framebuffer_opacity(self) -> float:
		return glfw.get_window_framebuffer_opacity(self.window)
	
	def set_window_framebuffer_icon(self, icon: str):
		glfw.set_window_framebuffer_icon(self.window, icon)

	def get_window_framebuffer_icon(self) -> str:
		return glfw.get_window_framebuffer_icon(self.window)
	
	def set_window_framebuffer_monitor(self, monitor: str):
		glfw.set_window_framebuffer_monitor(self.window, monitor)

	def get_window_framebuffer_monitor(self) -> str:
		return glfw.get_window_framebuffer_monitor(self.window)
	
	def set_window_framebuffer_size(self, width: int, height: int):
		glfw.set_window_framebuffer_size(self.window, width, height)

	def get_window_framebuffer_size(self) -> tuple[int, int]:
		return glfw.get_window_framebuffer_size(self.window)
	
	def set_window_resizable(self, resizable: bool):
		glfw.set_window_resizable(self.window, resizable)

	def set_window_resize_callback(self, callback):
		glfw.set_window_size_callback(self.window, callback)