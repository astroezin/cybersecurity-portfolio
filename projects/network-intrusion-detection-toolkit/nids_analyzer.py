"""
Network Intrusion Detection Toolkit

Main CLI analysis engine.
"""

import argparse

from core.config import create_directories
from core.loader import (
    load_packets,
    get_capture_information,
)
from core.logger import setup_logger
from core.reporter import (
    create_report,
    save_report,
)
from core.statistics import (
    calculate_statistics,
    count_alerts,
)

from detector.arp_detector import detect_arp_spoofing
from detector.http_detector import detect_http_activity
from detector.ioc_extractor import extract_iocs
from detector.scan_detector import (
    detect_port_scan,
    detect_syn_scan,
)
from detector.timeline import (
    create_timeline,
    summarize_timeline,
)


def parse_arguments():
    """
    Parse command line arguments.

    Returns:
        argparse.Namespace
    """

    parser = argparse.ArgumentParser(
        description=
        "Network Intrusion Detection Toolkit"
    )

    parser.add_argument(
        "pcap",
        help=
        "PCAP or PCAPNG file to analyze"
    )

    return parser.parse_args()


def run_detection(
    packets
):
    """
    Execute all detection modules.

    Args:
        packets (list): Scapy packets.

    Returns:
        list: Detection alerts.
    """

    alerts = []

    alerts.extend(
        detect_syn_scan(
            packets
        )
    )

    alerts.extend(
        detect_port_scan(
            packets
        )
    )

    alerts.extend(
        detect_arp_spoofing(
            packets
        )
    )

    alerts.extend(
        detect_http_activity(
            packets
        )
    )

    return alerts


def main():

    create_directories()

    logger = setup_logger()

    args = parse_arguments()

    logger.info(
        "Starting NIDS analysis"
    )

    logger.info(
        f"Analyzing file: {args.pcap}"
    )

    packets = load_packets(
        args.pcap
    )

    capture_info = get_capture_information(
        packets
    )

    logger.info(
        f"Loaded {len(packets)} packets"
    )

    alerts = run_detection(
        packets
    )

    statistics = calculate_statistics(
        packets
    )

    statistics[
        "alert_summary"
    ] = count_alerts(
        alerts
    )

    iocs = extract_iocs(
        packets
    )

    timeline = create_timeline(
        packets
    )

    report_data = create_report(
        packets,
        alerts,
        statistics,
        iocs,
        {
            "summary":
                summarize_timeline(
                    timeline
                ),

            "events":
                timeline[:100],
        }
    )

    report_data[
        "capture_information"
    ] = capture_info

    report_path = save_report(
        report_data
    )

    print("=" * 60)

    print(
        "NETWORK INTRUSION DETECTION TOOLKIT"
    )

    print("=" * 60)

    print()

    print(
        f"Packets analyzed: {len(packets)}"
    )

    print(
        f"Alerts detected: {len(alerts)}"
    )

    print()

    print(
        "Alert Summary"
    )

    print(
        "-" * 40
    )

    for severity, count in statistics[
        "alert_summary"
    ].items():

        print(
            f"{severity}: {count}"
        )

    print()

    print(
        "Report Generated:"
    )

    print(
        report_path
    )

    logger.info(
        "Analysis completed successfully"
    )


if __name__ == "__main__":

    main()
