"""
Endpoint isolation response playbook for SOAR Incident Response Platform.
"""


def isolate_host(
    hostname
):
    """
    Simulate endpoint isolation.

    Args:
        hostname (str): Host to isolate.

    Returns:
        dict: Response action result.
    """

    return {

        "action":
            "ISOLATE_HOST",

        "target":
            hostname,

        "status":
            "SUCCESS",

        "message":
            (
                f"Endpoint isolation request "
                f"sent to {hostname}"
            ),

    }
