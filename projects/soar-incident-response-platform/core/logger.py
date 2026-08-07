"""
Logging configuration for SOAR Incident Response Platform.
"""

import logging

from core.config import LOG_FILE


def setup_logger():
    """
    Configure application logger.

    Returns:
        logging.Logger
    """

    logger = logging.getLogger(
        "SOAR"
    )

    logger.setLevel(
        logging.INFO
    )


    if not logger.handlers:

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
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
