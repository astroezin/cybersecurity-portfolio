#!/usr/bin/env python3

import argparse
import ipaddress
import json
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
import socket

SUSPICIOUS_KEYWORDS = [
    "login",
    "signin",
    "verify",
    "update",
    "secure",
    "account",
    "bank",
    "password",
    "confirm",
    "wallet",
    "paypal",
    "crypto",
    "reset",
    "invoice",
    "payment"
]

SUSPICIOUS_TLDS = [
    ".xyz",
    ".top",
    ".click",
    ".gq",
    ".cf",
    ".ml",
    ".tk",
    ".zip",
    ".review"
]

URL_SHORTENERS = [
    "bit.ly",
    "tinyurl.com",
    "t.co",
    "goo.gl",
    "ow.ly",
    "is.gd",
    "buff.ly",
    "cutt.ly",
    "rebrand.ly",
    "rb.gy"
]


def validate_url(url):
    """
    Validate URL format.
    """

    parsed = urlparse(url)

    if not parsed.scheme or not parsed.netloc:
        raise ValueError("Invalid URL.")

    return parsed


def is_ip_address(host):
    """
    Check whether the hostname is an IP address.
    """

    try:
        ipaddress.ip_address(host)
        return True
    except ValueError:
        return False


def count_subdomains(host):
    """
    Count subdomains.
    """

    parts = host.split(".")

    if len(parts) <= 2:
        return 0

    return len(parts) - 2


def detect_keywords(url):
    """
    Find suspicious keywords.
    """

    found = []

    lower = url.lower()

    for keyword in SUSPICIOUS_KEYWORDS:

        if keyword in lower:
            found.append(keyword)

    return found


def detect_tld(host):
    """
    Detect suspicious TLD.
    """

    for tld in SUSPICIOUS_TLDS:

        if host.endswith(tld):
            return tld

    return None


def detect_shortener(host):
    """
    Detect URL shortening services.
    """

    return host.lower() in URL_SHORTENERS


def calculate_risk(parsed):
    """
    Calculate heuristic risk score.
    """

    findings = []

    score = 0

    host = parsed.hostname or ""

    if parsed.scheme.lower() == "http":
        findings.append("Uses insecure HTTP")
        score += 20

    if is_ip_address(host):
        findings.append("Uses IP address instead of domain")
        score += 25

    if len(parsed.geturl()) > 100:
        findings.append("Very long URL")
        score += 15

    subdomains = count_subdomains(host)

    if subdomains >= 3:
        findings.append(
            f"Excessive subdomains ({subdomains})"
        )
        score += 15

    keywords = detect_keywords(parsed.geturl())

    if keywords:
        findings.append(
            "Suspicious keywords: "
            + ", ".join(keywords)
        )
        score += len(keywords) * 5

    suspicious_tld = detect_tld(host)

    if suspicious_tld:
        findings.append(
            f"Suspicious TLD ({suspicious_tld})"
        )
        score += 20

    if detect_shortener(host):
        findings.append(
            "Known URL shortener"
        )
        score += 15

    if score >= 60:
        verdict = "SUSPICIOUS"

    elif score >= 40:
        verdict = "HIGH RISK"

    elif score >= 20:
        verdict = "MEDIUM RISK"

    else:
        verdict = "LOW RISK"

    return {
        "score": score,
        "verdict": verdict,
        "findings": findings,
        "subdomains": subdomains,
        "keywords": keywords
    }


def save_report(report, output_file):
    """
    Save JSON report.
    """

    path = Path(output_file)

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with path.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            report,
            file,
            indent=4
        )

SUSPICIOUS_TLDS = {
    ".zip",
    ".xyz",
    ".top",
    ".gq",
    ".tk",
    ".ml",
    ".cf",
    ".ga"
}

URL_SHORTENERS = {
    "bit.ly",
    "tinyurl.com",
    "goo.gl",
    "t.co",
    "ow.ly",
    "is.gd",
    "buff.ly",
    "rebrand.ly"
}


def check_suspicious_tld(hostname):
    """
    Check whether the hostname uses
    a suspicious top-level domain.
    """

    for tld in SUSPICIOUS_TLDS:
        if hostname.endswith(tld):
            return True

    return False


def is_ip_url(hostname):
    """
    Determine whether the URL
    uses an IP address.
    """

    try:
        ipaddress.ip_address(hostname)
        return True

    except ValueError:
        return False


def check_shortener(hostname):
    """
    Detect common URL shortening services.
    """

    return hostname.lower() in URL_SHORTENERS


def calculate_score(
    suspicious_tld,
    ip_url,
    shortener,
    long_url,
    scheme
):
    """
    Calculate a simple reputation score.
    """

    score = 0

    if suspicious_tld:
        score += 30

    if ip_url:
        score += 30

    if shortener:
        score += 20

    if long_url:
        score += 10

    if scheme != "https":
        score += 10

    return min(score, 100)


def determine_risk(score):
    """
    Convert numeric score to
    a risk level.
    """

    if score >= 70:
        return "High"

    if score >= 40:
        return "Medium"

    return "Low"        
def display_report(report):
    """
    Display results to the console.
    """

    print("=" * 60)
    print("URL Reputation Checker")
    print("=" * 60)
    print(f"URL              : {report['url']}")
    print(f"Hostname         : {report['hostname']}")
    print(f"Scheme           : {report['scheme']}")
    print(f"HTTPS            : {report['https']}")
    print(f"IP Address       : {report['ip_address']}")
    print()

    print("Security Checks")
    print("-" * 60)
    print(f"Suspicious TLD   : {report['suspicious_tld']}")
    print(f"IP URL           : {report['ip_url']}")
    print(f"URL Shortener    : {report['url_shortener']}")
    print(f"Long URL         : {report['long_url']}")
    print()

    print(f"Risk Score       : {report['risk_score']}/100")
    print(f"Risk Level       : {report['risk_level']}")
    print()
    print(f"JSON Report      : {report['report_file']}")


def main():

    parser = argparse.ArgumentParser(
        description="URL Reputation Checker"
    )

    parser.add_argument(
        "-u",
        "--url",
        required=True,
        help="Target URL"
    )

    parser.add_argument(
        "-o",
        "--output",
        default="reports/url_report.json",
        help="Output JSON report"
    )

    args = parser.parse_args()

    try:

        parsed = urlparse(args.url)

        hostname = parsed.hostname

        if not hostname:
            raise ValueError("Invalid URL")

        ip_address = socket.gethostbyname(hostname)

        suspicious_tld = check_suspicious_tld(hostname)
        ip_url = is_ip_url(hostname)
        shortener = check_shortener(hostname)
        long_url = len(args.url) > 75

        score = calculate_score(
            suspicious_tld,
            ip_url,
            shortener,
            long_url,
            parsed.scheme
        )

        level = determine_risk(score)

        report = {
            "url": args.url,
            "hostname": hostname,
            "scheme": parsed.scheme,
            "https": parsed.scheme == "https",
            "ip_address": ip_address,
            "suspicious_tld": suspicious_tld,
            "ip_url": ip_url,
            "url_shortener": shortener,
            "long_url": long_url,
            "risk_score": score,
            "risk_level": level,
            "scan_time": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "report_file": args.output
        }

        save_report(
            report,
            args.output
        )

        display_report(report)

    except socket.gaierror:
        print("[ERROR] Unable to resolve hostname.")

    except ValueError as error:
        print(f"[ERROR] {error}")

    except Exception as error:
        print(f"[ERROR] {error}")


if __name__ == "__main__":
    main()
