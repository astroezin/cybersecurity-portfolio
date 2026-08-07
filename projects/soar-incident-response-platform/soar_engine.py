"""
SOAR Incident Response Platform.

Main automation engine.
"""

from core.config import (
    create_directories,
    SAMPLE_DIR,
)

from core.database import (
    load_data,
    save_data,
)

from core.logger import (
    setup_logger,
)

from core.reporter import (
    create_incident_report,
    save_report,
)

from workflows.incident_handler import (
    handle_incident,
)

from intelligence.risk_engine import (
    calculate_risk,
)

from intelligence.mitre_mapping import (
    map_multiple_alerts,
)


def main():
    """
    Execute SOAR workflow.
    """

    create_directories()

    logger = setup_logger()

    logger.info(
        "Starting SOAR Incident Response Platform"
    )


    alerts = load_data(
        SAMPLE_DIR /
        "alerts.json"
    )


    incidents = []


    for alert in alerts:

        incident = handle_incident(
            alert
        )

        incidents.append(
            incident
        )


    risk = calculate_risk(
        alerts
    )


    mitre = map_multiple_alerts(
        alerts
    )


    if incidents:

        report = create_incident_report(
            {
                "case_id":
                    incidents[0]["case_id"],

                "severity":
                    risk["level"],

                "status":
                    "Investigating",

                "summary":
                    "Automated SOAR incident response completed.",

                "detections":
                    alerts,

                "actions":
                    incidents[0]["actions"],

                "mitre":
                    mitre,

                "risk":
                    risk,
            }
        )


        files = save_report(
            report
        )


        save_data(
            incidents,
            "cases/cases.json"
        )


    print("=" * 60)

    print(
        "SOAR INCIDENT RESPONSE PLATFORM"
    )

    print("=" * 60)

    print()

    print(
        f"Alerts processed: {len(alerts)}"
    )

    print(
        f"Risk Level: {risk['level']}"
    )

    print(
        f"Risk Score: {risk['score']}/100"
    )

    print()

    print(
        "MITRE ATT&CK Mapping"
    )

    print(
        "-" * 40
    )


    for technique in mitre:

        print(
            technique
        )


    print()

    print(
        "Incident Reports Generated:"
    )

    print(
        files
    )


    logger.info(
        "SOAR workflow completed"
    )


if __name__ == "__main__":

    main()
