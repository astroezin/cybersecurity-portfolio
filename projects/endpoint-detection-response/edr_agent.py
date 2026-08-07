"""
Endpoint Detection & Response Simulator.

Main execution engine.
"""

from core.config import (
    create_directories,
    SAMPLE_DIR,
)

from core.database import load_json

from core.logger import setup_logger

from core.reporter import (
    create_report,
    save_report,
)

from detection.process_monitor import (
    analyze_processes,
)

from detection.persistence_detector import (
    analyze_persistence,
)

from detection.file_monitor import (
    analyze_files,
)

from detection.network_detector import (
    analyze_network_events,
)

from intelligence.mitre_mapping import (
    map_to_mitre,
)

from intelligence.risk_engine import (
    calculate_risk,
)


def main():
    """
    Run EDR analysis.
    """

    create_directories()

    logger = setup_logger()

    logger.info(
        "Starting EDR analysis"
    )


    processes = load_json(
        SAMPLE_DIR /
        "processes.json"
    )

    startup_entries = load_json(
        SAMPLE_DIR /
        "startup_entries.json"
    )

    network_events = load_json(
        SAMPLE_DIR /
        "network_events.json"
    )


    detections = []


    detections.extend(
        analyze_processes(
            processes
        )
    )


    detections.extend(
        analyze_persistence(
            startup_entries
        )
    )


    detections.extend(
        analyze_network_events(
            network_events
        )
    )


    mitre = map_to_mitre(
        detections
    )


    risk = calculate_risk(
        detections
    )


    report = create_report(
        detections,
        risk,
        mitre,
    )


    files = save_report(
        report
    )


    print("=" * 60)

    print(
        "ENDPOINT DETECTION & RESPONSE SIMULATOR"
    )

    print("=" * 60)


    print()

    print(
        f"Detections: {len(detections)}"
    )

    print(
        f"Risk Level: {risk['level']}"
    )

    print(
        f"Risk Score: {risk['score']}/100"
    )


    print()

    print(
        "Detection Summary"
    )

    print(
        "-" * 40
    )


    for detection in detections:

        print(
            f"{detection['severity']}: "
            f"{detection['description']}"
        )


    print()

    print(
        "Reports Generated:"
    )

    print(
        files
    )


    logger.info(
        "EDR analysis completed"
    )


if __name__ == "__main__":

    main()
