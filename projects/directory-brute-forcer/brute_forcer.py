#!/usr/bin/env python3

import argparse
import json
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin

DEFAULT_USER_AGENT = (
    "DirectoryBruteForcer/1.0 "
    "(Cybersecurity Portfolio Project)"
)


def load_wordlist(wordlist_file):
    """
    Load directory names from a wordlist.
    """

    path = Path(wordlist_file)

    if not path.exists():
        raise FileNotFoundError(
            f"Wordlist not found: {wordlist_file}"
        )

    with path.open("r", encoding="utf-8") as file:
        return [
            line.strip()
            for line in file
            if line.strip()
        ]


def scan_directory(target, directory, timeout, user_agent):
    """
    Scan a single directory.
    """

    url = urljoin(target.rstrip("/") + "/", directory)

    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": user_agent
        }
    )

    try:
        with urllib.request.urlopen(
            request,
            timeout=timeout
        ) as response:

            return {
                "url": url,
                "status": response.status,
                "length": response.headers.get(
                    "Content-Length",
                    "Unknown"
                )
            }

    except urllib.error.HTTPError as error:

        return {
            "url": url,
            "status": error.code,
            "length": "Unknown"
        }

    except urllib.error.URLError:
        return None


def save_report(results, output_file):
    """
    Save results as JSON.
    """

    report = {
        "scan_time": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "total_requests": len(results),
        "interesting_results": [
            result
            for result in results
            if result["status"] != 404
        ]
    }

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

    return path


def main():

    parser = argparse.ArgumentParser(
        description=(
            "Directory Brute Forcer - "
            "Discover hidden web directories"
        )
    )

    parser.add_argument(
        "-u",
        "--url",
        required=True,
        help="Target URL"
    )

    parser.add_argument(
        "-w",
        "--wordlist",
        required=True,
        help="Wordlist path"
    )

    parser.add_argument(
        "-t",
        "--timeout",
        type=int,
        default=5,
        help="HTTP timeout in seconds"
    )

    parser.add_argument(
        "-T",
        "--threads",
        type=int,
        default=10,
        help="Number of worker threads"
    )

    parser.add_argument(
        "-o",
        "--output",
        default="reports/scan_results.json",
        help="Output JSON report"
    )

    parser.add_argument(
        "--user-agent",
        default=DEFAULT_USER_AGENT,
        help="Custom User-Agent"
    )

    args = parser.parse_args()

    try:

        words = load_wordlist(args.wordlist)

        print("=" * 60)
        print("Directory Brute Forcer")
        print("=" * 60)
        print(f"Target   : {args.url}")
        print(f"Wordlist : {args.wordlist}")
        print(f"Entries  : {len(words)}")
        print(f"Threads  : {args.threads}")
        print("=" * 60)

        results = []

        with ThreadPoolExecutor(
            max_workers=args.threads
        ) as executor:

            futures = [
                executor.submit(
                    scan_directory,
                    args.url,
                    word,
                    args.timeout,
                    args.user_agent
                )
                for word in words
            ]

            for future in as_completed(futures):

                result = future.result()

                if result is None:
                    continue

                results.append(result)

                if result["status"] != 404:

                    print(
                        f"[{result['status']}] "
                        f"{result['url']} "
                        f"(Length: {result['length']})"
                    )

        report = save_report(
            results,
            args.output
        )

        interesting = [
            result
            for result in results
            if result["status"] != 404
        ]

        print("\n" + "=" * 60)
        print("Scan Summary")
        print("=" * 60)
        print(f"Total Requests      : {len(results)}")
        print(f"Interesting Results : {len(interesting)}")
        print(f"JSON Report         : {report}")

    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user.")

    except Exception as error:
        print(f"[ERROR] {error}")


if __name__ == "__main__":
    main()
