# demonstrate the logging api in Python

# use the built-in logging module
import logging

# Use basicConfig to configure logging
# if filename not specified, console will be used, 
# filemode="w": file contents will be replaced 
logging.basicConfig(level=logging.DEBUG, filename="output.log", filemode="w")

# Try out each of the log levels
logging.debug("This is a debug-level message")
logging.info("This is a info-level message")
logging.warning("This is a warning-level message")
logging.error("This is a error-level message")
logging.critical("This is a critical-level message")

# Output formatted strings to the log
x = "string"
y = 10
logging.info(f"Here's a {x} variable and an int: {y}")
