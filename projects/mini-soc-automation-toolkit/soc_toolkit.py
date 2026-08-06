"""
Mini SOC Automation Toolkit

Main command-line interface.
"""

import argparse

from core.config import ensure_directories
from core.validator import validate_ioc
from core.formatter import create_console_report
from core.correlator import calculate_risk
from core.report import (
    save_json_report,
    save_markdown_report
)
from core.logger import setup_logger

from api.virustotal import (
    lookup_ip,
    lookup_domain,
    lookup_hash,
    analyze_result as analyze_vt
)

from api.abuseipdb import (
    lookup_ip as abuse_lookup_ip,
    analyze_result as analyze_abuse
)


def parse_arguments():
    """
    CLI argument parser.
    """

    parser = argparse.ArgumentParser(
        description="Mini SOC Automation Toolkit"
    )

    parser.add_argument(
        "ioc",
        help="IP, domain, URL, or file hash"
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Generate JSON report"
    )

    parser.add_argument(
        "--markdown",
        action="store_true",
        help="Generate Markdown report"
    )

    return parser.parse_args()


def collect_threat_data(ioc_data, logger):
    """
    Collect intelligence based on IOC type.
    """

    vt_result = {}
    abuse_result = {}

    indicator = ioc_data["indicator"]
    ioc_type = ioc_data["type"]

    logger.info(
        f"Collecting intelligence for {indicator}"
    )

    if ioc_type == "IPv4":

        vt_result = analyze_vt(
            lookup_ip(indicator)
        )

        abuse_result = analyze_abuse(
            abuse_lookup_ip(indicator)
        )

    elif ioc_type == "Domain":

        vt_result = analyze_vt(
            lookup_domain(indicator)
        )

    elif ioc_type in (
        "MD5",
        "SHA1",
        "SHA256"
    ):

        vt_result = analyze_vt(
            lookup_hash(indicator)
        )

    return vt_result, abuse_result


def main():

    ensure_directories()

    logger = setup_logger()

    logger.info(
        "SOC Toolkit started"
    )

    args = parse_arguments()

    logger.info(
        f"Input received: {args.ioc}"
    )

    ioc_data = validate_ioc(
        args.ioc
    )

    if not ioc_data["valid"]:

        logger.warning(
            f"Invalid IOC format: {args.ioc}"
        )

        print(
            "[!] Invalid IOC format"
        )

        return


    vt_data, abuse_data = collect_threat_data(
        ioc_data,
        logger
    )


    risk = calculate_risk(
        vt_data,
        abuse_data
    )


    report_data = {

        "ioc": ioc_data["indicator"],

        "type": ioc_data["type"],

        "virustotal": vt_data,

        "abuseipdb": abuse_data,

        "risk": risk
    }


    print(
        create_console_report(
            ioc_data["indicator"],
            ioc_data["type"],
            vt_data,
            abuse_data,
            risk
        )
    )


    if args.json:

        json_report = save_json_report(
            report_data
        )

        print(
            "\nJSON:"
        )

        print(
            json_report
        )


    if args.markdown:

        markdown_report = save_markdown_report(
            report_data
        )

        print(
            "\nMarkdown:"
        )

        print(
            markdown_report
        )


    logger.info(
        f"IOC analyzed successfully: {args.ioc}"
    )

    logger.info(
        "SOC Toolkit completed successfully"
    )


if __name__ == "__main__":
    main()
