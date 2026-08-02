#!/usr/bin/env python3

from scapy.all import sniff, IP, TCP, UDP, ICMP
import argparse

packet_count = 0


def get_protocol(packet):
    if packet.haslayer(TCP):
        return "TCP"
    elif packet.haslayer(UDP):
        return "UDP"
    elif packet.haslayer(ICMP):
        return "ICMP"
    return "OTHER"


def process_packet(packet):
    global packet_count
    packet_count += 1

    if not packet.haslayer(IP):
        return

    ip = packet[IP]

    print("=" * 60)
    print(f"Packet #{packet_count}")
    print("=" * 60)
    print(f"Source IP      : {ip.src}")
    print(f"Destination IP : {ip.dst}")
    print(f"Protocol       : {get_protocol(packet)}")
    print(f"Packet Length  : {len(packet)} bytes")


def main():
    parser = argparse.ArgumentParser(
        description="Simple Packet Sniffer using Scapy"
    )

    parser.add_argument(
        "-c",
        "--count",
        type=int,
        default=0,
        help="Number of packets to capture (0 = unlimited)"
    )

    args = parser.parse_args()

    print("=" * 60)
    print("Python Packet Sniffer")
    print("=" * 60)
    print("Press Ctrl+C to stop.\n")

    try:
        sniff(
            prn=process_packet,
            store=False,
            count=args.count
        )
    except KeyboardInterrupt:
        print("\nCapture stopped.")


if __name__ == "__main__":
    main()
