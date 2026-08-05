"""
analysis.py

Functions responsible for analyzing packets.
"""

from collections import Counter
from datetime import datetime

from scapy.all import ICMP, IP, TCP, UDP


def analyze_protocols(packets):
    protocols = Counter()

    for packet in packets:
        if packet.haslayer(TCP):
            protocols["TCP"] += 1
        elif packet.haslayer(UDP):
            protocols["UDP"] += 1
        elif packet.haslayer(ICMP):
            protocols["ICMP"] += 1
        elif packet.haslayer(IP):
            protocols["Other IP"] += 1
        else:
            protocols["Non-IP"] += 1

    return protocols


def analyze_ip_addresses(packets):
    source_ips = Counter()
    destination_ips = Counter()

    for packet in packets:
        if packet.haslayer(IP):
            source_ips[packet[IP].src] += 1
            destination_ips[packet[IP].dst] += 1

    return source_ips, destination_ips


def analyze_conversations(packets):
    conversations = Counter()

    for packet in packets:
        if packet.haslayer(IP):
            conversations[(packet[IP].src, packet[IP].dst)] += 1

    return conversations


def analyze_ports(packets):
    tcp_ports = Counter()
    udp_ports = Counter()

    for packet in packets:
        if packet.haslayer(TCP):
            tcp_ports[packet[TCP].dport] += 1
        elif packet.haslayer(UDP):
            udp_ports[packet[UDP].dport] += 1

    return tcp_ports, udp_ports


def analyze_packet_sizes(packets):
    if not packets:
        return {
            "total_bytes": 0,
            "smallest": 0,
            "largest": 0,
            "average": 0.0,
        }

    sizes = [len(packet) for packet in packets]

    return {
        "total_bytes": sum(sizes),
        "smallest": min(sizes),
        "largest": max(sizes),
        "average": sum(sizes) / len(sizes),
    }


def analyze_capture_statistics(packets):
    """
    Calculate capture timing statistics.
    """
    if not packets:
        return None

    start = float(packets[0].time)
    end = float(packets[-1].time)

    duration = end - start

    if duration <= 0:
        duration = 1e-6

    total_packets = len(packets)
    total_bytes = sum(len(packet) for packet in packets)

    return {
        "start": datetime.fromtimestamp(start),
        "end": datetime.fromtimestamp(end),
        "duration": duration,
        "pps": total_packets / duration,
        "bps": total_bytes / duration,
    }
