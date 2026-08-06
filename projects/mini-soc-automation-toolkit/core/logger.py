"""
Logging configuration module.

Creates application logs for auditing
and troubleshooting.
"""

import logging

from core.config import Config


def setup_logger():
    """
    Configure application logger.
    """

    log_file = (
        Config.LOG_DIRECTORY
        /
        "soc_toolkit.log"
    )

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format=(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(message)s"
        )
    )

    return logging.getLogger(
        "SOC_TOOLKIT"
    )
