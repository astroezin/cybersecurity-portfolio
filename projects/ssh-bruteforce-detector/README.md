# SSH Brute Force Detector

A Python tool that analyzes Linux SSH authentication logs to detect failed login attempts, successful logins, and potential brute-force activity.

This project demonstrates practical blue-team skills used in SOC environments for monitoring and investigating authentication events.

---

## Features

- Parse Linux SSH authentication logs
- Detect failed login attempts
- Detect successful logins
- Count failed attempts by IP address
- Count failed attempts by username
- Display summary statistics
- Command-line interface using argparse

---

## Technologies Used

- Python 3
- argparse
- re (regular expressions)
- collections.Counter

---

## Installation

No external dependencies are required.

```bash
python3 brute_detector.py sample_auth.log
```

---

## Usage

Analyze a log file:

```bash
python3 brute_detector.py sample_auth.log
```

---

## Example Output

```text
Failed Login Attempts by IP

203.0.113.10      5
198.51.100.22     3

Failed Login Attempts by Username

root              4
admin             3
ubuntu            1

Successful Logins

kali
ubuntu
```

---

## Project Structure

```text
ssh-bruteforce-detector/
├── brute_detector.py
├── sample_auth.log
├── README.md
├── requirements.txt
├── .gitignore
└── screenshots/
```

---

## Skills Demonstrated

- Log analysis
- Blue-team monitoring
- SSH authentication analysis
- Regular expressions
- Python automation
- Incident detection

---

## Future Improvements

- Threshold-based brute-force alerts
- CSV and JSON export
- Timeline analysis
- IP reputation integration
- GeoIP lookups
- Interactive HTML report
- Real-time log monitoring (`tail -f` style)

---

## License

MIT License
