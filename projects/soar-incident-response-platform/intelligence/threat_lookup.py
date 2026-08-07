"""
Threat intelligence enrichment module for SOAR Incident Response Platform.
"""


KNOWN_MALICIOUS_IPS = {

    "185.220.101.25":
        {
            "reputation": "MALICIOUS",
            "category": "TOR Exit Node",
            "confidence": 90,
        },

    "203.0.113.50":
        {
            "reputation": "SUSPICIOUS",
            "category": "Threat Intelligence Match",
            "confidence": 70,
        },

}


def lookup_ip(
    ip_address
):
    """
    Simulate IP reputation lookup.

    Args:
        ip_address (str): IP address.

    Returns:
        dict: Threat intelligence result.
    """

    result = KNOWN_MALICIOUS_IPS.get(
        ip_address
    )


    if result:

        return {

            "ip":
                ip_address,

            "found":
                True,

            "reputation":
                result["reputation"],

            "category":
                result["category"],

            "confidence":
                result["confidence"],

        }


    return {

        "ip":
            ip_address,

        "found":
            False,

        "reputation":
            "UNKNOWN",

        "category":
            "No Threat Data",

        "confidence":
            0,

    }
