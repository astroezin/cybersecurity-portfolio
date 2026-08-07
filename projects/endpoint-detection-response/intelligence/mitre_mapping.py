"""
MITRE ATT&CK mapping module for Endpoint Detection & Response Simulator.
"""


MITRE_MAP = {

    "SUSPICIOUS_PROCESS":
        "T1059 - Command and Scripting Interpreter",

    "MALICIOUS_COMMAND":
        "T1059.001 - PowerShell",

    "PERSISTENCE_DETECTED":
        "T1547 - Boot or Logon Autostart Execution",

    "SUSPICIOUS_FILE":
        "T1204 - User Execution",

    "SUSPICIOUS_NETWORK_CONNECTION":
        "T1071 - Application Layer Protocol",

}


def map_to_mitre(
    detections
):
    """
    Map detections to MITRE ATT&CK techniques.

    Args:
        detections (list): Detection events.

    Returns:
        list: MITRE techniques.
    """

    techniques = []


    for detection in detections:

        detection_type = detection.get(
            "type",
            ""
        )

        technique = MITRE_MAP.get(
            detection_type
        )

        if technique:

            techniques.append(
                technique
            )


    return list(
        set(
            techniques
        )
    )
