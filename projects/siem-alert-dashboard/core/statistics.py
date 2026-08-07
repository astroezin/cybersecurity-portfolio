"""
Statistics helpers for SIEM Alert Dashboard.
"""

from collections import Counter


def calculate_statistics(alerts):
    """
    Calculate dashboard statistics.
    """

    total = len(alerts)

    severity_counter = Counter()

    status_counter = Counter()

    source_counter = Counter()

    mitre_counter = Counter()

    for alert in alerts:

        severity_counter.update(
            [alert.get("severity", "Unknown")]
        )

        status_counter.update(
            [alert.get("status", "Unknown")]
        )

        source_counter.update(
            [alert.get("source", "Unknown")]
        )

        techniques = alert.get(
            "mitre",
            []
        )

        if isinstance(
            techniques,
            str
        ):

            techniques = [techniques]

        mitre_counter.update(
            techniques
        )

    return {

        "total_alerts": total,

        "severity": dict(
            severity_counter
        ),

        "status": dict(
            status_counter
        ),

        "sources": dict(
            source_counter
        ),

        "mitre": dict(
            mitre_counter
        )

    }


def filter_alerts(
    alerts,
    severity=None,
    status=None
):
    """
    Filter alerts.
    """

    results = alerts

    if severity:

        results = [

            alert

            for alert in results

            if alert.get(
                "severity"
            ) == severity

        ]

    if status:

        results = [

            alert

            for alert in results

            if alert.get(
                "status"
            ) == status

        ]

    return results
