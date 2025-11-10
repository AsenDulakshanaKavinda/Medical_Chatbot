import os
import logging
import logging.config
from logging.handlers import RotatingFileHandler
from from_root import from_root
from datetime import datetime

# constants for log configurations
LOG_DIR = 'logs'
LOG_FILE = f"{datetime.now().strftime('%m-%d-%Y-%H-%M-%S')}.log"
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 3

# construct log file path
log_dir_path = os.path.join(from_root(), LOG_DIR)
os.makedirs(log_dir_path, exist_ok=True)
log_file_path = os.path.join(log_dir_path, LOG_FILE)

LOG_CONFIG = {
    "version": 1,
    "formatters": {
        "json": {
            "format": '{"time": "%(asctime)s", "level": "%(levelname)s", "logger": "%(name)s", "message": "%(message)s"}'
        },
        "detailed": {
            "format": "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "detailed",
            "level": "INFO"
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "json",
            "filename": log_file_path,
            "maxBytes": MAX_LOG_SIZE,
            "backupCount": BACKUP_COUNT,
            "level": "DEBUG",
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console", "file"]
    }
}

# Apply config
logging.config.dictConfig(LOG_CONFIG)

if __name__ == "__main__":
    # Example usage
    app_logger = logging.getLogger("app")
    db_logger = logging.getLogger("db")

    for i in range(10):  # generate enough logs to force rotation
        app_logger.info(f"Processing request {i}")
        db_logger.error(f"Database error on request {i}")