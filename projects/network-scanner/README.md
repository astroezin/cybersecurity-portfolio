# Multi-Threaded Network Scanner

A Python-based multi-threaded TCP port scanner that quickly identifies open ports and common services on a target host.

---

## Features

- Multi-threaded TCP scanning
- Adjustable port range
- Configurable number of worker threads
- Common service detection
- Fast scanning using ThreadPoolExecutor
- Simple command-line interface

---

## Technologies Used

- Python 3
- socket
- argparse
- concurrent.futures

---

## Installation

### Clone the repository

```bash
git clone https://github.com/astroezin/cybersecurity-portfolio.git
```

### Navigate to the project

```bash
cd cybersecurity-portfolio/projects/network-scanner
```

No external dependencies are required.

---

## Usage

Scan the default ports (1–1024)

```bash
python3 network_scanner.py scanme.nmap.org
```

Scan a custom port range

```bash
python3 network_scanner.py scanme.nmap.org --start 20 --end 100
```

Increase the number of scanning threads

```bash
python3 network_scanner.py scanme.nmap.org --threads 200
```

---

## Example Output

```text
============================================================
Scanning scanme.nmap.org
============================================================

[OPEN ] 22     SSH
[OPEN ] 80     HTTP
```

---

## Project Structure

```text
network-scanner/
│
├── network_scanner.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Skills Demonstrated

- Python Networking
- TCP Port Scanning
- Multi-threading
- Concurrent Programming
- Service Identification
- Command-Line Interfaces
- Network Reconnaissance

---

## Interview Questions

### Why use multiple threads?

Multiple threads allow many ports to be scanned simultaneously, significantly reducing scan time compared to scanning one port at a time.

### What is `ThreadPoolExecutor`?

It manages a pool of worker threads, making concurrent programming simpler and more efficient.

### What does `socket.connect_ex()` return?

It attempts to connect to a TCP port and returns `0` if the connection succeeds. Other return values indicate connection failures or errors.

### Why are socket timeouts important?

Timeouts prevent the scanner from waiting too long for unresponsive ports, making scans faster and more reliable.

---

## Future Improvements

- Banner grabbing
- Hostname resolution
- CSV export
- JSON export
- Progress indicator
- IPv6 support
- UDP scanning
- Colored output
- Scan timing statistics
- Operating system detection (limited)

---

## Disclaimer

This project is intended for educational purposes and authorized security testing only.
