import logging
import logging.config
import yaml
import os

# Load logging configuration from an external file
with open("logging_config.yaml", "r") as f:
    config = yaml.safe_load(f.read())

# Ensure log directory exists
log_file_path = config["handlers"]["file"]["filename"]
log_dir = os.path.dirname(log_file_path)

if log_dir and not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Apply logging configuration
logging.config.dictConfig(config)

# Create a logger
logger = logging.getLogger("todo_app")
logger.info("Logging setup complete.")