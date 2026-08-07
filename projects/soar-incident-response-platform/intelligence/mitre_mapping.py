"""
MITRE ATT&CK mapping module for SOAR Incident Response Platform.
"""


MITRE_TECHNIQUES = {

    "BRUTE_FORCE":
        "T1110 - Brute Force",

    "MALWARE":
        "T1204 - User Execution",

    "PHISHING":
        "T1566 - Phishing",

    "COMMAND_EXECUTION":
        "T1059 - Command and Scripting Interpreter",

    "DATA_EXFILTRATION":
        "T1041 - Exfiltration Over C2 Channel",

    "SUSPICIOUS_NETWORK":
        "T1071 - Application Layer Protocol",

}


def map_alert_to_mitre(
    alert_type
):
    """
    Map alert category to MITRE ATT&CK.

    Args:
        alert_type (str): Detection type.

    Returns:
        str: MITRE technique.
    """

    return MITRE_TECHNIQUES.get(
        alert_type,
        "Unknown Technique"
    )


def map_multiple_alerts(
    alerts
):
    """
    Map multiple alerts.

    Args:
        alerts (list): Alert list.

    Returns:
        list: MITRE mappings.
    """

    techniques = []


    for alert in alerts:

        technique = map_alert_to_mitre(
            alert.get(
                "type",
                ""
            )
        )


        if technique not in techniques:

            techniques.append(
                technique
            )


    return techniques
