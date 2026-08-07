# Network Intrusion Detection Toolkit (NIDS)

A professional network security analysis toolkit that performs offline packet capture analysis, detects suspicious network activities, extracts indicators of compromise (IOCs), maps findings to MITRE ATT&CK techniques, and generates forensic investigation reports.

This project simulates a simplified SOC analyst workflow for network monitoring and incident investigation.

---

# Features

## Packet Capture Analysis

Supports:

- PCAP file analysis
- PCAPNG file analysis
- Packet statistics
- Network traffic inspection
- Timeline generation


---

# Intrusion Detection

Detects suspicious activities:

## SYN Scan Detection

Identifies:

- Multiple TCP SYN requests
- Potential reconnaissance activity
- Network scanning behavior


## Port Scan Detection

Detects:

- Sequential port connection attempts
- Suspicious service enumeration


## ARP Spoofing Detection

Analyzes:

- ARP traffic anomalies
- Possible man-in-the-middle activity


## HTTP Activity Detection

Identifies:

- HTTP requests
- Suspicious web activity


---

# Threat Intelligence Features

## IOC Extraction

Extracts:

- Source IP addresses
- Destination IP addresses
- Domains


## MITRE ATT&CK Mapping

Maps detected activity to techniques:

Examples:

```

T1046 - Network Service Scanning

T1071.001 - Web Protocols

T1071.004 - DNS

T1557.002 - ARP Cache Poisoning

```


---

# Reporting

Generates forensic JSON reports containing:

- Case ID
- Capture information
- Packet statistics
- Detection alerts
- IOC information
- Timeline events
- Investigation metadata


Example:

```

reports/

└── nids_report_20260807_005644.json

```


---

# Technologies Used

- Python 3
- Scapy
- Packet Analysis
- Network Security
- MITRE ATT&CK Framework
- JSON Reporting
- Linux CLI


---

# Installation

Clone repository:

```bash
git clone https://github.com/astroezin/cybersecurity-portfolio.git
```

Navigate:

```bash
cd cybersecurity-portfolio/projects/network-intrusion-detection-toolkit
```

Create virtual environment:

```bash
python3 -m venv venv
```

Activate:

Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Usage

Analyze a packet capture:

```bash
python nids_analyzer.py samples/network_capture.pcap
```

Example output:

```
============================================================
NETWORK INTRUSION DETECTION TOOLKIT
============================================================

Packets analyzed: 7

Alerts detected: 1

Alert Summary
----------------------------------------
LOW: 1

Report Generated:

reports/nids_report_20260807_005644.json
```

---

# Project Structure

```
network-intrusion-detection-toolkit/

├── core/
│   ├── config.py
│   ├── loader.py
│   ├── logger.py
│   ├── reporter.py
│   └── statistics.py
│
├── detector/
│   ├── arp_detector.py
│   ├── http_detector.py
│   ├── ioc_extractor.py
│   ├── scan_detector.py
│   └── timeline.py
│
├── samples/
│   └── network_capture.pcap
│
├── reports/
│   └── nids_report.json
│
├── logs/
│
├── screenshots/
│
├── nids_analyzer.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

# Skills Demonstrated

This project demonstrates:

* Network traffic analysis
* Intrusion detection concepts
* Packet inspection
* Python security automation
* IOC extraction
* MITRE ATT&CK mapping
* SOC analyst workflow
* Digital investigation reporting

---

# Future Improvements

Possible improvements:

* Real-time packet monitoring
* Web dashboard interface
* Machine learning anomaly detection
* Integration with Elasticsearch/Kibana
* Threat intelligence APIs
* Automated alert correlation
* PCAP visualization

---

# Security Notice

This tool is designed for:

* Defensive security research
* Authorized network analysis
* Cybersecurity learning
* SOC analyst training

Only analyze network traffic that you have permission to investigate.

---

# License

MIT License

Copyright (c) 2026 Rejin Lama
