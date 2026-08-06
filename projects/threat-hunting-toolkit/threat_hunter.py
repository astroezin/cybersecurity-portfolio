"""
Threat Hunting Toolkit

Main CLI interface.
"""

import argparse

from hunters.file_hunter import FileHunter
from hunters.ioc_hunter import IOCHunter
from hunters.log_hunter import LogHunter
from core.reporter import HuntReporter
from core.logger import setup_logger


def parse_arguments():

    parser = argparse.ArgumentParser(
        description="Threat Hunting Toolkit"
    )

    parser.add_argument(
        "--file",
        help="Analyze file"
    )

    parser.add_argument(
        "--log",
        help="Analyze log file"
    )

    parser.add_argument(
        "--ioc-file",
        help="Search IOC file"
    )

    return parser.parse_args()


def main():

    logger = setup_logger()

    logger.info(
        "Threat hunting started"
    )


    args = parse_arguments()

    findings = []


    if args.file:

        logger.info(
            f"Analyzing file: {args.file}"
        )

        hunter = FileHunter()

        result = hunter.analyze_file(
            args.file
        )

        findings.append(
            {
                "type": "file_analysis",
                "result": result
            }
        )


    if args.log:

        logger.info(
            f"Analyzing log: {args.log}"
        )

        hunter = LogHunter()

        results = hunter.hunt(
            args.log
        )

        findings.extend(
            results
        )


    if args.ioc_file:

        logger.info(
            f"Searching IOC file: {args.ioc_file}"
        )

        with open(
            args.ioc_file
        ) as file:

            content = file.read()


        hunter = IOCHunter(
            []
        )

        results = hunter.extract_iocs(
            content
        )

        findings.append(
            {
                "type": "ioc_extraction",
                "result": results
            }
        )


    if not findings:

        logger.warning(
            "No findings generated"
        )

        print(
            "[!] No hunting source provided"
        )

        return


    logger.info(
        f"Findings detected: {len(findings)}"
    )


    reporter = HuntReporter()

    report = reporter.generate_report(
        findings
    )


    logger.info(
        "Report generated successfully"
    )


    print(
        "=" * 50
    )

    print(
        "THREAT HUNTING REPORT"
    )

    print(
        "=" * 50
    )

    print()

    print(
        f"Findings: {len(findings)}"
    )

    print()

    print(
        "Reports Generated:"
    )

    print()

    print(
        f"JSON Report: {report['json']}"
    )

    print(
        f"Markdown Report: {report['markdown']}"
    )


if __name__ == "__main__":

    main()
