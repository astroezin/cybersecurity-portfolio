"""
Threat intelligence correlation engine.

Combines multiple security signals
and calculates an overall risk rating.
"""


def calculate_risk(
    vt_data=None,
    abuse_data=None
):
    """
    Calculate overall risk level.

    Returns:
        Dictionary containing:
        - risk level
        - score
        - reasons
    """

    score = 0
    reasons = []

    vt_data = vt_data or {}
    abuse_data = abuse_data or {}

    # VirusTotal analysis

    malicious = vt_data.get(
        "malicious",
        0
    )

    suspicious = vt_data.get(
        "suspicious",
        0
    )

    if malicious >= 10:
        score += 50
        reasons.append(
            "High VirusTotal malicious detection count"
        )

    elif malicious >= 5:
        score += 35
        reasons.append(
            "Multiple VirusTotal malicious detections"
        )

    elif malicious > 0:
        score += 20
        reasons.append(
            "VirusTotal malicious detections found"
        )


    if suspicious > 0:
        score += 10
        reasons.append(
            "VirusTotal suspicious detections found"
        )


    # AbuseIPDB analysis

    abuse_score = abuse_data.get(
        "abuse_score",
        0
    )

    if abuse_score >= 90:
        score += 50
        reasons.append(
            "Critical AbuseIPDB confidence score"
        )

    elif abuse_score >= 70:
        score += 35
        reasons.append(
            "High AbuseIPDB confidence score"
        )

    elif abuse_score >= 40:
        score += 20
        reasons.append(
            "Moderate AbuseIPDB confidence score"
        )


    # Final classification

    if score >= 80:
        risk = "CRITICAL"

    elif score >= 50:
        risk = "HIGH"

    elif score >= 25:
        risk = "MEDIUM"

    elif score > 0:
        risk = "LOW"

    else:
        risk = "INFORMATIONAL"


    return {
        "risk": risk,
        "score": score,
        "reasons": reasons
    }
