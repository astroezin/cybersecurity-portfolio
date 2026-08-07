"""
Alert loader for the SIEM Alert Dashboard.
"""

import json

from core.config import (
    ALERT_FILE,
    create_directories
)

from core.logger import setup_logger


logger = setup_logger()


REQUIRED_FIELDS = [

    "alert_id",

    "title",

    "severity",

    "status",

    "source_ip",

    "username",

    "timestamp"

]


def validate_alert(alert):
    """
    Validate a single alert.
    """

    for field in REQUIRED_FIELDS:

        if field not in alert:

            logger.warning(
                f"Missing field '{field}' in alert."
            )

            return False

    return True


def load_alerts():
    """
    Load alerts from the JSON file.
    """

    create_directories()

    if not ALERT_FILE.exists():

        logger.warning(
            "Alert file not found."
        )

        return []

    try:

        with open(
            ALERT_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(
                file
            )

    except json.JSONDecodeError:

        logger.error(
            "Invalid JSON format."
        )

        return []

    except Exception as error:

        logger.error(
            f"Unable to load alerts: {error}"
        )

        return []

    alerts = []

    for alert in data:

        if validate_alert(
            alert
        ):

            alerts.append(
                alert
            )

    logger.info(
        f"{len(alerts)} alerts loaded."
    )

    return alerts
