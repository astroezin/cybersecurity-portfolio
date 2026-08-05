#!/usr/bin/env python3

"""
PCAP Analyzer

Author: Rejin Lama
"""

import argparse
import os
import sys

from modules.analysis import (
    analyze_capture_statistics,
    analyze_conversations,
    analyze_ip_addresses,
    analyze_packet_sizes,
    analyze_ports,
    analyze_protocols,
)
from modules.loader import load_pcap
from modules.reporter import (
    print_banner,
    print_capture_statistics,
    print_conversations,
    print_ip_statistics,
    print_packet_sizes,
    print_ports,
    print_protocols,
)


def main():
    parser = argparse.ArgumentParser(
        description="Professional PCAP Analyzer"
    )

    parser.add_argument(
        "pcap",
        help="Path to a PCAP file"
    )

    args = parser.parse_args()

    if not os.path.isfile(args.pcap):
        print(f"[ERROR] File not found: {args.pcap}")
        sys.exit(1)

    packets = load_pcap(args.pcap)

    protocols = analyze_protocols(packets)
    source_ips, destination_ips = analyze_ip_addresses(packets)
    conversations = analyze_conversations(packets)
    tcp_ports, udp_ports = analyze_ports(packets)
    packet_sizes = analyze_packet_sizes(packets)
    capture_stats = analyze_capture_statistics(packets)

    print_banner(args.pcap, len(packets))
    print_protocols(protocols)

    print_ip_statistics(
        "Top Source IP Addresses",
        source_ips
    )

    print_ip_statistics(
        "Top Destination IP Addresses",
        destination_ips
    )

    print_conversations(conversations)

    print_ports(
        "Top TCP Destination Ports",
        tcp_ports
    )

    print_ports(
        "Top UDP Destination Ports",
        udp_ports
    )

    print_packet_sizes(packet_sizes)
    print_capture_statistics(capture_stats)


if __name__ == "__main__":
    main()
