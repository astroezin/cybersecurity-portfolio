"""
Risk scoring engine for Endpoint Detection & Response Simulator.
"""


SEVERITY_SCORE = {

    "LOW": 10,

    "MEDIUM": 30,

    "HIGH": 60,

    "CRITICAL": 90,

}


def calculate_risk(
    detections
):
    """
    Calculate overall incident risk.

    Args:
        detections (list): Detection alerts.

    Returns:
        dict: Risk assessment.
    """

    score = 0

    reasons = []


    for detection in detections:

        severity = detection.get(
            "severity",
            "LOW"
        )


        score += SEVERITY_SCORE.get(
            severity,
            0
        )


        reasons.append(
            detection.get(
                "description",
                "Unknown detection"
            )
        )


    if score >= 100:

        level = "CRITICAL"

    elif score >= 60:

        level = "HIGH"

    elif score >= 30:

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
