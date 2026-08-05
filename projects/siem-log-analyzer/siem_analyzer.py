#!/usr/bin/env python3

"""
SIEM Log Analyzer

A Python-based security monitoring tool that analyzes
Linux authentication logs and detects suspicious activity.

Author: Rejin Lama
Purpose: Cybersecurity Portfolio Project
"""

import argparse
import json
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


def load_log_file(file_path):
    """
    Load log file contents.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    with path.open("r") as file:
        return file.readlines()


def parse_log_line(line):
    """
    Convert raw authentication log lines
    into structured security events.
    """

    event = {
        "raw": line.strip(),
        "type": "UNKNOWN",
        "username": None,
        "ip": None,
        "timestamp": None
    }

    timestamp = re.match(
        r"([A-Z][a-z]{2}\s+\d+\s+\d+:\d+:\d+)",
        line
    )

    if timestamp:
        event["timestamp"] = timestamp.group(1)

    failed_login = re.search(
        r"Failed password for (?:invalid user )?(\w+).*from ([0-9.]+)",
        line
    )

    if failed_login:
        event["type"] = "FAILED_LOGIN"
        event["username"] = failed_login.group(1)
        event["ip"] = failed_login.group(2)

    successful_login = re.search(
        r"Accepted password for (\w+) from ([0-9.]+)",
        line
    )

    if successful_login:
        event["type"] = "SUCCESS_LOGIN"
        event["username"] = successful_login.group(1)
        event["ip"] = successful_login.group(2)

    privilege = re.search(
        r"sudo:\s+(\w+).*USER=root.*COMMAND=(.*)",
        line
    )

    if privilege:
        event["type"] = "PRIVILEGE_ESCALATION"
        event["username"] = privilege.group(1)
        event["command"] = privilege.group(2)

    return event


def analyze_logs(lines):
    """
    Parse all log lines.
    """

    events = []

    for line in lines:
        events.append(parse_log_line(line))

    return events


def detect_threats(events, threshold=5):
    """
    Analyze normalized events and generate alerts.
    """

    alerts = []

    failed_attempts = defaultdict(int)
    root_attempts = defaultdict(int)
    successful_ips = set()

    for event in events:

        if event["type"] == "FAILED_LOGIN":
            failed_attempts[event["ip"]] += 1

        if event["type"] == "SUCCESS_LOGIN":
            successful_ips.add(event["ip"])

        if (
            event["type"] == "FAILED_LOGIN"
            and event["username"] == "root"
        ):
            root_attempts[event["ip"]] += 1

        if event["type"] == "PRIVILEGE_ESCALATION":
            alerts.append({
                "severity": "MEDIUM",
                "type": "PRIVILEGE_ESCALATION",
                "message": "Sudo command executed with root privileges",
                "user": event["username"],
                "command": event["command"]
            })

    for ip, count in failed_attempts.items():

        if count >= threshold:

            alerts.append({
                "severity": "HIGH",
                "type": "BRUTE_FORCE",
                "message": "Possible SSH brute force attack",
                "ip": ip,
                "failed_attempts": count
            })

            if ip in successful_ips:

                alerts.append({
                    "severity": "CRITICAL",
                    "type": "ACCOUNT_COMPROMISE",
                    "message": "Successful login after brute force attempts",
                    "ip": ip
                })

    for ip, count in root_attempts.items():

        alerts.append({
            "severity": "MEDIUM",
            "type": "ROOT_LOGIN_ATTEMPT",
            "message": "Multiple root account login attempts detected",
            "ip": ip,
            "attempts": count
        })

    return alerts


def generate_report(events, alerts, output_file):
    """
    Generate JSON security report.
    """

    report = {
        "scan_time": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "total_events": len(events),
        "alerts_found": len(alerts),
        "alerts": alerts
    }

    path = Path(output_file)

    with path.open("w") as file:
        json.dump(
            report,
            file,
            indent=4
        )

    return path


def severity_summary(alerts):
    """
    Count alerts by severity.
    """

    summary = Counter()

    for alert in alerts:
        summary[alert["severity"]] += 1

    return summary
def display_alerts(alerts):
    """
    Display alerts in SOC analyst format.
    """

    print("\nSecurity Alerts:")
    print("=" * 60)

    for alert in alerts:

        print(
            f"\n[{alert['severity']}] {alert['type']}"
        )

        print("-" * 60)

        print(
            f"Message: {alert['message']}"
        )

        if "ip" in alert:
            print(
                f"Source IP: {alert['ip']}"
            )

        if "failed_attempts" in alert:
            print(
                f"Failed Attempts: {alert['failed_attempts']}"
            )

        if "attempts" in alert:
            print(
                f"Attempts: {alert['attempts']}"
            )

        if "user" in alert:
            print(
                f"User: {alert['user']}"
            )

        if "command" in alert:
            print(
                f"Command: {alert['command']}"
            )

        print()

def main():

    parser = argparse.ArgumentParser(
        description=(
        "SIEM Log Analyzer - Detect suspicious activity "
        "from Linux authentication logs"
        ))

    parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="Authentication log file"
    )

    parser.add_argument(
        "-o",
        "--output",
        default="reports/security_report.json",
        help="Output JSON report path"
    )

    args = parser.parse_args()

    try:

        logs = load_log_file(args.file)

        events = analyze_logs(logs)

        alerts = detect_threats(events)

        summary = severity_summary(alerts)

        report = generate_report(
            events,
            alerts,
            args.output
        )

        print(f"\n[+] Report saved: {report}")

        print("\nSeverity Summary:")
        print("=" * 60)

        for level, count in summary.items():
            print(f"{level}: {count}")

        display_alerts(alerts)

        print("\nEvent Analysis Complete")
        print("=" * 60)
        print(f"Processed Events: {len(events)}")

    except Exception as error:
        print(f"[ERROR] {error}")


if __name__ == "__main__":
    main()
