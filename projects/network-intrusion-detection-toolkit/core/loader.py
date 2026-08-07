"""
Packet capture loading module for the Network Intrusion Detection Toolkit.
"""

from pathlib import Path

from scapy.all import rdpcap


def validate_pcap(
    file_path
):
    """
    Validate packet capture file.

    Args:
        file_path (str): Capture file path.

    Returns:
        bool
    """

    path = Path(
        file_path
    )

    if not path.exists():

        raise FileNotFoundError(
            f"Capture file not found: {file_path}"
        )

    if path.suffix.lower() not in [
        ".pcap",
        ".pcapng",
    ]:

        raise ValueError(
            "Unsupported capture format. "
            "Use .pcap or .pcapng"
        )

    return True


def load_packets(
    file_path
):
    """
    Load packets from PCAP file.

    Args:
        file_path (str): PCAP path.

    Returns:
        list: Scapy packets.
    """

    validate_pcap(
        file_path
    )

    packets = rdpcap(
        file_path
    )

    return packets


def get_capture_information(
    packets
):
    """
    Return basic capture information.

    Args:
        packets (list): Scapy packets.

    Returns:
        dict
    """

    if not packets:

        return {
            "total_packets": 0,
            "first_packet": None,
            "last_packet": None,
        }

    return {
        "total_packets":
            len(packets),

        "first_packet":
            packets[0].time,

        "last_packet":
            packets[-1].time,
    }
