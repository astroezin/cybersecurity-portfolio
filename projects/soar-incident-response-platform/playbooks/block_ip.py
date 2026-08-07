"""
IP blocking response playbook for SOAR Incident Response Platform.
"""


def block_ip(
    ip_address
):
    """
    Simulate blocking a malicious IP address.

    Args:
        ip_address (str): IP address to block.

    Returns:
        dict: Response action result.
    """

    return {

        "action":
            "BLOCK_IP",

        "target":
            ip_address,

        "status":
            "SUCCESS",

        "message":
            (
                f"Firewall rule created "
                f"to block {ip_address}"
            ),

    }
