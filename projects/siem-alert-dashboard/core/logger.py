"""
Logging utilities
for the SIEM Alert Dashboard.
"""

import logging

from core.config import (
    LOG_FILE,
    create_directories
)


def setup_logger():
    """
    Configure and return
    the application logger.
    """

    create_directories()

    logger = logging.getLogger(
        "siem_dashboard"
    )

    if logger.handlers:
        return logger

    logger.setLevel(
        logging.INFO
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        LOG_FILE
    )

    file_handler.setLevel(
        logging.INFO
    )

    file_handler.setFormatter(
        formatter
    )

    console_handler = logging.StreamHandler()

    console_handler.setLevel(
        logging.INFO
    )

    console_handler.setFormatter(
        formatter
    )

    logger.addHandler(
        file_handler
    )

    logger.addHandler(
        console_handler
    )

    return logger
