"""
Logging configuration for the Network Intrusion Detection Toolkit.
"""

import logging

from core.config import LOG_FILE


def setup_logger():
    """
    Configure application logger.

    Returns:
        logging.Logger
    """

    LOG_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    logger = logging.getLogger(
        "NIDS"
    )

    logger.setLevel(
        logging.INFO
    )

    if not logger.handlers:

        formatter = logging.Formatter(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(message)s"
        )

        file_handler = logging.FileHandler(
            LOG_FILE
        )

        file_handler.setFormatter(
            formatter
        )

        console_handler = logging.StreamHandler()

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
