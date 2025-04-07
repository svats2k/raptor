"""
Logging set for the repository
"""

import logging

from pathlib import Path
from rich.logging import RichHandler

logger = logging.getLogger(__name__)

# creating a new directory called logs if it doesn't exist
Path("logs/").mkdir(parents=True, exist_ok=True)

shell_handler = RichHandler()
file_handler = logging.FileHandler("logs/debug.log")

logger.setLevel(logging.INFO)
shell_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.INFO)

# the formatter determines how the logger looks like
FMT_SHELL = "%(message)s"
FMT_FILE = """%(levelname)s %(asctime)s [%(filename)s
    %(funcName)s %(lineno)d] %(message)s"""

shell_formatter = logging.Formatter(FMT_SHELL)
file_formatter = logging.Formatter(FMT_FILE)

# Putting them together
shell_handler.setFormatter(shell_formatter)
file_handler.setFormatter(file_formatter)

logger.addHandler(shell_handler)
logger.addHandler(file_handler)
