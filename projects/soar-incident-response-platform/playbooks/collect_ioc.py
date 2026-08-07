"""
IOC collection response playbook for SOAR Incident Response Platform.
"""


def collect_ioc(
    alert
):
    """
    Extract indicators of compromise from alert.

    Args:
        alert (dict): Security alert.

    Returns:
        dict: Collected IOC information.
    """

    indicators = {}


    if alert.get(
        "source_ip"
    ):

        indicators["source_ip"] = (
            alert["source_ip"]
        )


    if alert.get(
        "destination_ip"
    ):

        indicators["destination_ip"] = (
            alert["destination_ip"]
        )


    if alert.get(
        "hash"
    ):

        indicators["hash"] = (
            alert["hash"]
        )


    if alert.get(
        "domain"
    ):

        indicators["domain"] = (
            alert["domain"]
        )


    return {

        "action":
            "COLLECT_IOC",

        "status":
            "SUCCESS",

        "indicators":
            indicators,

        "message":
            "Indicators collected successfully",

    }
