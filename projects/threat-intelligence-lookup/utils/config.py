import os
from dotenv import load_dotenv


load_dotenv()


VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
ABUSEIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY")


def validate_api_keys():
    """
    Validate that required API keys are available.
    """
    missing = []

    if not VIRUSTOTAL_API_KEY:
        missing.append("VIRUSTOTAL_API_KEY")

    if not ABUSEIPDB_API_KEY:
        missing.append("ABUSEIPDB_API_KEY")

    if missing:
        raise EnvironmentError(
            "Missing environment variables: "
            + ", ".join(missing)
            + "\nCreate a .env file based on .env.example."
        )
