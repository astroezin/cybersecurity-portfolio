"""
Notification response playbook for SOAR Incident Response Platform.
"""


def notify_analyst(
    case_id,
    severity
):
    """
    Simulate analyst notification.

    Args:
        case_id (str): Incident case identifier.
        severity (str): Incident severity.

    Returns:
        dict: Notification result.
    """

    return {

        "action":
            "NOTIFY_ANALYST",

        "status":
            "SUCCESS",

        "recipient":
            "SOC Analyst",

        "message":
            (
                f"Analyst notified about "
                f"{severity} incident {case_id}"
            ),

    }
