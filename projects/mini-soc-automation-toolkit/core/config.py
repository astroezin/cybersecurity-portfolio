"""
Configuration handler for Mini SOC Automation Toolkit.

Loads environment variables and provides centralized configuration.
"""

import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")


class Config:
    """
    Application configuration.
    """

    VIRUSTOTAL_API_KEY = os.getenv(
        "VIRUSTOTAL_API_KEY",
        ""
    )

    ABUSEIPDB_API_KEY = os.getenv(
        "ABUSEIPDB_API_KEY",
        ""
    )

    REPORT_DIRECTORY = BASE_DIR / "reports"

    LOG_DIRECTORY = BASE_DIR / "logs"

    TOOL_NAME = "Mini SOC Automation Toolkit"


def ensure_directories():
    """
    Create required directories if missing.
    """

    Config.REPORT_DIRECTORY.mkdir(
        exist_ok=True
    )

    Config.LOG_DIRECTORY.mkdir(
        exist_ok=True
    )
