import logging
import sys
from logging.handlers import RotatingFileHandler

LOG_FILE_PATH = "/app/logs/app.log"


def setup_logging():
    formatter = logging.Formatter(
        fmt='{"time": "%(asctime)s", "level": "%(levelname)s", "module": "%(module)s", "message": "%(message)s"}'
    )

    # Console output (Docker STDOUT)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    # File rotation (max 5MB × 3 files)
    file_handler = RotatingFileHandler(LOG_FILE_PATH, maxBytes=5_000_000, backupCount=3)
    file_handler.setFormatter(formatter)

    logging.basicConfig(level=logging.INFO, handlers=[console_handler, file_handler])

    logger = logging.getLogger("backend")
    logger.info("📜 Logging initialized")
    return logger
