import platform

# inhert from different types of platform windows to create a window class
from Reva.Window.OpenGL import GLFWWindow
from Reva.Window.Mac import MetalWindow
from Reva.Window.Windows import DirectxWindow

match platform.system():
	case "Windows":
		_win_handle = DirectxWindow.Window
	case "Darwin":
		_win_handle = MetalWindow.Window
	case "Linux":
		_win_handle = GLFWWindow.Window
	case _:
		raise Exception("Unsupported platform")

# Temporary solution until the dedicated platform specific window classes are implemented
# for now, we will use the GLFWWindow class for all platforms
_win_handle = GLFWWindow.Window

class Window(_win_handle):
	def __init__(self, width: int, height: int, title: str):
		super().__init__(width, height, title)
		self.width = width
		self.height = height
		self.title = title
		self.is_vsync = True
	
	def set_title(self, title: str):
		self.title = title
		self.set_window_title(title)

	def get_title(self) -> str:
		return self.title
	
	def set_size(self, width: int, height: int):
		self.width = width
		self.height = height
		self.set_window_size(width, height)
	
	def get_size(self) -> tuple[int, int]:
		return self.width, self.height
	
	def get_width(self) -> int:
		return self.width
	
	def get_height(self) -> int:
		return self.height	
	
	def set_vsync(self, value):
		self.is_vsync = value
		return super().set_vsync(value)

	def get_vsync(self) -> bool:
		return self.is_vsync