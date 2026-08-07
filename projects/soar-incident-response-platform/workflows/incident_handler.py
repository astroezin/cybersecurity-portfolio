"""
Incident response workflow engine for SOAR Incident Response Platform.
"""

from datetime import datetime

from playbooks.block_ip import (
    block_ip,
)

from playbooks.isolate_host import (
    isolate_host,
)

from playbooks.collect_ioc import (
    collect_ioc,
)

from playbooks.notify import (
    notify_analyst,
)

from intelligence.threat_lookup import (
    lookup_ip,
)


def generate_case_id():
    """
    Generate unique case identifier.

    Returns:
        str: Case ID.
    """

    timestamp = datetime.now().strftime(
        "%Y%m%d-%H%M%S"
    )

    return (
        f"SOAR-{timestamp}"
    )


def handle_incident(
    alert
):
    """
    Execute incident response workflow.

    Args:
        alert (dict): Security alert.

    Returns:
        dict: Incident case.
    """

    case_id = generate_case_id()

    actions = []


    source_ip = alert.get(
        "source_ip"
    )


    if source_ip:

        threat = lookup_ip(
            source_ip
        )


        if threat.get(
            "found"
        ):

            actions.append(
                block_ip(
                    source_ip
                )
            )


    hostname = alert.get(
        "hostname"
    )


    if hostname:

        actions.append(
            isolate_host(
                hostname
            )
        )


    actions.append(
        collect_ioc(
            alert
        )
    )


    actions.append(
        notify_analyst(
            case_id,
            alert.get(
                "severity",
                "UNKNOWN"
            )
        )
    )


    return {

        "case_id":
            case_id,

        "severity":
            alert.get(
                "severity",
                "UNKNOWN"
            ),

        "status":
            "Investigating",

        "summary":
            alert.get(
                "title",
                "Security Incident"
            ),

        "detections":
            [
                alert
            ],

        "actions":
            actions,

    }
