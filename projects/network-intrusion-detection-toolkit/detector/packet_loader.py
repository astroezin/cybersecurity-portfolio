"""
Packet loading utilities for the Network Intrusion Detection Toolkit.
"""

from pathlib import Path

from scapy.all import rdpcap


def load_packets(file_path):
    """
    Load packets from a PCAP file.

    Args:
        file_path (str): Path to the PCAP file.

    Returns:
        list: List of Scapy packets.

    Raises:
        FileNotFoundError: If the PCAP file does not exist.
        ValueError: If the PCAP file cannot be parsed.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"PCAP file not found: {path}"
        )

    if not path.is_file():
        raise FileNotFoundError(
            f"Not a file: {path}"
        )

    try:
        packets = rdpcap(str(path))
    except Exception as error:
        raise ValueError(
            f"Unable to load PCAP file: {error}"
        ) from error

    return list(packets)


def packet_count(packets):
    """
    Return the total number of packets.

    Args:
        packets (list): Loaded packets.

    Returns:
        int
    """

    return len(packets)


def total_bytes(packets):
    """
    Calculate the total number of bytes.

    Args:
        packets (list): Loaded packets.

    Returns:
        int
    """

    return sum(len(packet) for packet in packets)
