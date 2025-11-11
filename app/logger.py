import logging
from logging.handlers import RotatingFileHandler
import os


LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "app.log")


handler = RotatingFileHandler(LOG_FILE, maxBytes=2_000_000, backupCount=5)
formatter = logging.Formatter(
    "%(asctime)s - [%(levelname)s] - %(name)s - %(message)s"
)
handler.setFormatter(formatter)

logger = logging.getLogger("addressbook")
logger.setLevel(logging.INFO)
logger.addHandler(handler)