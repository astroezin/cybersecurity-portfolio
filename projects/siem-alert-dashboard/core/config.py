"""
Configuration settings
for the SIEM Alert Dashboard.
"""

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SAMPLES_DIR = BASE_DIR / "samples"

REPORTS_DIR = BASE_DIR / "reports"

LOGS_DIR = BASE_DIR / "logs"

STATIC_DIR = BASE_DIR / "static"

TEMPLATES_DIR = BASE_DIR / "templates"


ALERT_FILE = SAMPLES_DIR / "alerts.json"

LOG_FILE = LOGS_DIR / "dashboard.log"


SEVERITY_LEVELS = [

    "CRITICAL",

    "HIGH",

    "MEDIUM",

    "LOW"

]


STATUS_TYPES = [

    "NEW",

    "INVESTIGATING",

    "CLOSED"

]


APP_TITLE = "SIEM Alert Dashboard"

APP_VERSION = "1.0"


def create_directories():

    """
    Create required project folders.
    """

    REPORTS_DIR.mkdir(

        parents=True,

        exist_ok=True

    )

    LOGS_DIR.mkdir(

        parents=True,

        exist_ok=True

    )

    SAMPLES_DIR.mkdir(

        parents=True,

        exist_ok=True

    )
