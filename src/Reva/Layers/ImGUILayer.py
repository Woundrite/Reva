import imgui
from Reva.EventSystem.Layer import Layer
import glfw
from imgui.integrations.glfw import GlfwRenderer

class ImGUILayer(Layer):
	def __init__(self, name: str = "ImGUILayer"):
		super().__init__(name)
	
	def OnAttach(self, window):
		imgui.create_context()
		imgui.style_colors_dark()
		self.io = imgui.get_io()
		self.io.backend_flags |= imgui.BACKEND_FLAG_HAS_MOUSE_CURSORS
		self.io.backend_flags |= imgui.BACKEND_FLAG_HAS_SET_MOUSE_POS
		
		# TEMPORARY: should eventually use Hazel key codes
		self.io.KeyMap[imgui.Key_Tab] = glfw.KEY_TAB
		self.io.KeyMap[imgui.Key_LeftArrow] = glfw.KEY_LEFT
		self.io.KeyMap[imgui.Key_RightArrow] = glfw.KEY_RIGHT
		self.io.KeyMap[imgui.Key_UpArrow] = glfw.KEY_UP
		self.io.KeyMap[imgui.Key_DownArrow] = glfw.KEY_DOWN
		self.io.KeyMap[imgui.Key_PageUp] = glfw.KEY_PAGE_UP
		self.io.KeyMap[imgui.Key_PageDown] = glfw.KEY_PAGE_DOWN
		self.io.KeyMap[imgui.Key_Home] = glfw.KEY_HOME
		self.io.KeyMap[imgui.Key_End] = glfw.KEY_END
		self.io.KeyMap[imgui.Key_Insert] = glfw.KEY_INSERT
		self.io.KeyMap[imgui.Key_Delete] = glfw.KEY_DELETE
		self.io.KeyMap[imgui.Key_Backspace] = glfw.KEY_BACKSPACE
		self.io.KeyMap[imgui.Key_Space] = glfw.KEY_SPACE
		self.io.KeyMap[imgui.Key_Enter] = glfw.KEY_ENTER
		self.io.KeyMap[imgui.Key_Escape] = glfw.KEY_ESCAPE
		self.io.KeyMap[imgui.Key_A] = glfw.KEY_A
		self.io.KeyMap[imgui.Key_C] = glfw.KEY_C
		self.io.KeyMap[imgui.Key_V] = glfw.KEY_V
		self.io.KeyMap[imgui.Key_X] = glfw.KEY_X
		self.io.KeyMap[imgui.Key_Y] = glfw.KEY_Y
		self.io.KeyMap[imgui.Key_Z] = glfw.KEY_Z

		self.impl = GlfwRenderer(window)
	
	def OnDetach(self):
		self.impl.shutdown()

	def OnUpdate(self, delta_time: float):
		imgui.new_frame()
		show = True
		imgui.show_demo_window(show)

		self.io.delta_time = delta_time
		imgui.render()
		self.impl.render(imgui.get_draw_data())

	def OnEvent(self, event):
		pass
