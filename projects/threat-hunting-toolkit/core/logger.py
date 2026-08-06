"""
Threat Hunting Toolkit Logger

Provides logging functionality for audit tracking.
"""

import logging
from pathlib import Path


def setup_logger():

    Path("logs").mkdir(
        exist_ok=True
    )

    logger = logging.getLogger(
        "ThreatHunter"
    )

    logger.setLevel(
        logging.INFO
    )


    if not logger.handlers:

        file_handler = logging.FileHandler(
            "logs/threat_hunter.log"
        )


        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )


        file_handler.setFormatter(
            formatter
        )


        logger.addHandler(
            file_handler
        )


    return logger
