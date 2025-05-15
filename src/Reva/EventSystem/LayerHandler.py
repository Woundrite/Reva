from Reva.EventSystem.Layer import Layer
from Reva.EventSystem.Events import Event

class LayerHandler:
	"""
	Handles the layers in the engine.
	"""
	def __init__(self, logger):
		self.layers = []
		self.logger = logger
		self.logger.debug("LayerHandler initialized.")

	def add_layer(self, layer: Layer):
		"""
		Adds a layer to the layer stack.
		"""
		if not isinstance(layer, Layer):
			self.logger.error(f"Layer {layer} is not an instance of Layer.")
			self.logger.warning(f"Layer {layer} not added to the stack.")
			return
		self.layers.append(layer)
		self.logger.debug(f"Layer {layer.name} added to the stack.")

	def remove_layer(self, layer: Layer):
		"""
		Removes a layer from the layer stack.
		"""
		if layer in self.layers:
			self.layers.remove(layer)
			self.logger.debug(f"Layer {layer.name} removed from the stack.")
		else:
			self.logger.warning(f"Layer {layer.name} not found in the stack.")
	
	def onEvent(self, event: Event):
		"""
		Handles an event by passing it to the appropriate layer.
		"""
		for layer in self.layers:
			layer.process_event(event)
			self.logger.debug(f"Event {event.event_type} processed by layer {layer.name}.")
		self.logger.debug(f"Event {event} not handled by any layer.")

	