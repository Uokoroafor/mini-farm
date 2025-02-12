import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

# Set up log directory
log_dir = Path("./logs")
log_dir.mkdir(exist_ok=True)

# Create a logger
logger = logging.getLogger("todo_app")
logger.setLevel(logging.DEBUG)

# Create handlers
file_handler = RotatingFileHandler(log_dir / "backend.log", maxBytes=5 * 1024 * 1024, backupCount=5)
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create formatters and add them to the handlers
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
