import logging
import logging.config
import yaml

# Load logging configuration from an external file
with open("logging_config.yaml", "r") as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

# Create a logger
logger = logging.getLogger("todo_app")
