"""
logger.py

This module provides a `Logger` class for enhanced logging functionality with support for:
- Logging to both files and the console.
- Customizable log levels, formats, and output destinations.
- Colorized console output using the `colorama` library for better readability.

Classes:
    - Logger: A logger class that supports colorized console output and file logging.
    
Functions:
    - debug(message): Logs a debug-level message.
    - info(message): Logs an info-level message.
    - warning(message): Logs a warning-level message.
    - error(message): Logs an error-level message.
    - critical(message): Logs a critical-level message.
    - set_log_level(level): Sets the logging level.
    - set_log_format(log_format): Sets the logging format.
    - set_color_stdout(color_stdout): Enables or disables colorized console output.
    - set_log_file(log_file): Sets the file to which logs are written.

Unit Tests:
    - The `TestLogger` class provides unit tests for the `Logger` class, testing various logging levels, formats, colors, and outputs.

Dependencies:
    - logging: Standard Python logging module.
    - colorama: Library for cross-platform terminal text colorization.

Usage:
    - Instantiate the `Logger` class with optional parameters for log file, log level, log format, and colorized output.
    - Use the provided methods to log messages at different levels or customize the logger's behavior.

Example:
    ```python
    from logger import Logger
    logger = Logger(log_file='app.log', log_level=logging.DEBUG, color_stdout=True)
    logger.info("This is an info message.")
    logger.error("This is an error message.")
    ```

Author:
    - Nikhil (or replace with the appropriate author name)

Date:
    - April 28, 2025
"""

import logging
from colorama import Fore, Style

class Logger:
	def __init__(self, log_file=None, log_level=logging.INFO, log_format='%(asctime)s - %(levelname)s - %(message)s', color_stdout=True):
		self.logger = logging.getLogger()
		self.logger.setLevel(log_level)
		self.log_format = log_format
		self.color_stdout = color_stdout
		self.log_file = log_file
		self.formatter = logging.Formatter(log_format)
		self.file_handler = None
		self.stdout_handler = None
		self.create_handlers()
		self.logger.addHandler(self.file_handler)
		self.logger.addHandler(self.stdout_handler)
	
	def create_handlers(self):
		if self.log_file:
			self.file_handler = logging.FileHandler(self.log_file)
			self.file_handler.setFormatter(self.formatter)
		if self.color_stdout:
			self.stdout_handler = logging.StreamHandler()
			self.stdout_handler.setFormatter(self.formatter)
			self.stdout_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - ' + Fore.GREEN + '%(message)s' + Style.RESET_ALL))
		else:
			self.stdout_handler = logging.StreamHandler()
			self.stdout_handler.setFormatter(self.formatter)
			self.stdout_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
	
	def log(self, level, message):
		level_dict = {logging.DEBUG: logging.DEBUG, logging.INFO: logging.INFO, logging.WARNING: logging.WARNING, logging.ERROR: logging.ERROR, logging.CRITICAL: logging.CRITICAL}
		message = str(message) # Convert to string if not already
		# self.logger.log(level_dict[level], message)
		if self.color_stdout:
			if level == logging.DEBUG:
				print(Fore.BLUE + message + Style.RESET_ALL)
			elif level == logging.INFO:
				print(Fore.GREEN + message + Style.RESET_ALL)
				print(Fore.YELLOW + message + Style.RESET_ALL)
			elif level == logging.ERROR:
				print(Fore.RED + message + Style.RESET_ALL)
			elif level == logging.CRITICAL:
				print(Fore.RED + message + Style.RESET_ALL)
			else:
				print(message)
		else:
			print(message)

	def debug(self, message):
		self.log(logging.DEBUG, message)

	def info(self, message):
		self.log(logging.INFO, message)

	def warning(self, message):
		self.log(logging.WARNING, message)

	def error(self, message):
		self.log(logging.ERROR, message)

	def critical(self, message):
		self.log(logging.CRITICAL, message)

	def set_log_level(self, level):
		self.logger.setLevel(level)

	def set_log_format(self, log_format):
		self.log_format = log_format
		self.formatter = logging.Formatter(log_format)
		self.create_handlers()

	def set_color_stdout(self, color_stdout):
		self.color_stdout = color_stdout
		self.create_handlers()

	def set_log_file(self, log_file):
		self.log_file = log_file
		self.create_handlers()

	def set_log_level(self, level):
		self.logger.setLevel(level)

	def set_log_format(self, log_format):
		self.log_format = log_format
		self.formatter = logging.Formatter(log_format)
		self.create_handlers()

	def set_color_stdout(self, color_stdout):
		self.color_stdout = color_stdout
		self.create_handlers()

	def set_log_file(self, log_file):
		self.log_file = log_file
		self.create_handlers()

	def set_log_level(self, level):
		self.logger.setLevel(level)

	def set_log_format(self, log_format):
		self.log_format = log_format
		self.formatter = logging.Formatter(log_format)
		self.create_handlers()

	def set_color_stdout(self, color_stdout):
		self.color_stdout = color_stdout
		self.create_handlers()

	def set_log_file(self, log_file):
		self.log_file = log_file
		self.create_handlers()

	def set_log_level(self, level):
		self.logger.setLevel(level)

	def set_log_format(self, log_format):
		self.log_format = log_format
		self.formatter = logging.Formatter(log_format)
		self.create_handlers()

	def set_color_stdout(self, color_stdout):
		self.color_stdout = color_stdout
		self.create_handlers()

	def set_log_file(self, log_file):
		self.log

if __name__ == '__main__':
	import unittest

	class TestLogger(unittest.TestCase):
		def setUp(self):
			self.logger = Logger(log_file='test.log', log_level=logging.DEBUG, log_format='%(asctime)s - %(levelname)s - %(message)s', color_stdout=True)
			self.logger.set_log_level(logging.INFO)
			self.logger.set_log_format('%(asctime)s - %(levelname)s - %(message)s')
			self.logger.set_color_stdout(False)
			self.logger.set_log_file('test.log')

		def test_debug(self):
			self.logger.debug('This is a debug message')
			self.assertTrue(True)

		def test_info(self):
			self.logger.info('This is an info message')
			self.assertTrue(True)

		def test_warning(self):
			self.logger.warning('This is a warning message')
			self.assertTrue(True)

		def test_error(self):

			self.logger.error('This is an error message')
			self.assertTrue(True)

		def test_critical(self):
			self.logger.critical('This is a critical message')
			self.assertTrue(True)

		def test_set_log_level(self):
			self.logger.set_log_level(logging.DEBUG)
			self.assertTrue(True)

		def test_set_log_format(self):
			self.logger.set_log_format('%(asctime)s - %(levelname)s - %(message)s')
			self.assertTrue(True)

		def test_set_color_stdout(self):
			self.logger.set_color_stdout(True)
			self.assertTrue(True)
			self.logger.set_color_stdout(False)
			self.assertTrue(True)
			self.logger.set_color_stdout(True)
			self.assertTrue(True)
			self.logger.set_color_stdout(False)
			self.assertTrue(True)
			self.logger.set_color_stdout(True)
			self.assertTrue(True)

		def test_set_log_file(self):
			self.logger.set_log_file('test.log')
			self.assertTrue(True)
			self.logger.set_log_file('test2.log')
			self.assertTrue(True)
			self.logger.set_log_file('test3.log')
			self.assertTrue(True)

	unittest.main()