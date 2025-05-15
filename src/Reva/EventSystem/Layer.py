from abc import ABC, abstractmethod

class Layer(ABC):
	"""
	Abstract base class for layers in the event system.
	Each layer should implement the `process_event` method to handle events.
	"""
	def __init__(self, name: str = "Layer"):
		self.name = name
	
	def __str__(self):
		"""
		String representation of the layer.
		
		Returns:
			str: The name of the layer.
		"""
		return self.name
	
	def __repr__(self):
		"""
		String representation of the layer.
		
		Returns:
			str: The name of the layer.
		"""
		return self.name
	
	def getName(self) -> str:
		"""
		Get the name of the layer.
		
		Returns:
			str: The name of the layer.
		"""
		return self.name
	
	@abstractmethod
	def OnAttach(self):
		"""
		Called when the layer is attached to the event system.
		"""
		pass
	
	@abstractmethod
	def OnDetach(self):
		"""
		Called when the layer is detached from the event system.
		"""
		pass

	@abstractmethod
	def OnEvent(self):
		pass

	@abstractmethod
	def OnUpdate(self, delta_time: float):
		"""
		Called every frame to update the layer.
		
		Args:
			delta_time: The time since the last update in seconds.
		"""
		pass

	def __del__(self):
		"""
		Clean up the layer when it is deleted.
		"""
		self.OnDetach()