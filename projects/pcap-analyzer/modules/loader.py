"""
loader.py

Loads PCAP files.
"""

import sys

from scapy.all import rdpcap


def load_pcap(file_path):
    """
    Load packets from a PCAP file.

    Args:
        file_path (str): Path to the PCAP file.

    Returns:
        PacketList: Scapy packet list.
    """
    try:
        return rdpcap(file_path)

    except Exception as error:
        print(f"[ERROR] Failed to read PCAP:\n{error}")
        sys.exit(1)
