"""
Risk scoring engine for SOAR Incident Response Platform.
"""


SEVERITY_SCORE = {

    "LOW":
        20,

    "MEDIUM":
        40,

    "HIGH":
        70,

    "CRITICAL":
        90,

}


def calculate_risk(
    alerts
):
    """
    Calculate incident risk score.

    Args:
        alerts (list): Security alerts.

    Returns:
        dict: Risk information.
    """

    score = 0

    reasons = []


    for alert in alerts:

        severity = alert.get(
            "severity",
            "LOW"
        )


        score += SEVERITY_SCORE.get(
            severity,
            0
        )


        reasons.append(
            alert.get(
                "title",
                "Unknown alert"
            )
        )


    if score >= 150:

        level = "CRITICAL"

    elif score >= 100:

        level = "HIGH"

    elif score >= 50:

        level = "MEDIUM"

    else:

        level = "LOW"


    return {

        "score":
            min(
                score,
                100
            ),

        "level":
            level,

        "reasons":
            reasons,

    }
