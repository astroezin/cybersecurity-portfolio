"""
Log Correlation Engine

Main CLI application.

Analyzes security logs,
detects threats,
correlates incidents,
and generates reports.
"""


import argparse

from core.config import ensure_directories
from core.parser import LogParser
from core.rules import DetectionRules
from core.correlator import CorrelationEngine
from core.scoring import RiskScorer
from core.alert import AlertManager
from core.timeline import TimelineBuilder
from core.reporter import ReportGenerator



def parse_arguments():
    """
    CLI argument parser.
    """

    parser = argparse.ArgumentParser(
        description="Log Correlation Engine"
    )

    parser.add_argument(
        "logfile",
        help="Path to security log file"
    )

    return parser.parse_args()



def main():

    ensure_directories()

    args = parse_arguments()


    parser = LogParser()

    rules = DetectionRules()

    correlator = CorrelationEngine()

    scorer = RiskScorer()

    alert_manager = AlertManager()

    timeline = TimelineBuilder()

    reporter = ReportGenerator()



    print("=" * 50)

    print(
        "LOG CORRELATION ENGINE"
    )

    print("=" * 50)



    print(
        f"\nAnalyzing: {args.logfile}\n"
    )



    with open(args.logfile) as file:


        for line in file:


            event = (
                parser.parse_auth_log(
                    line
                )
            )


            correlator.add_event(
                event
            )


            timeline.add_event(
                event
            )


            alerts = (
                rules.analyze_event(
                    event
                )
            )


            for alert in alerts:

                print(
                    "[ALERT]",
                    alert
                )



    incidents = (
        correlator.analyze()
    )


    if not incidents:


        print(
            "\nNo incidents detected."
        )

        return



    incident = incidents[0]


    risk = scorer.analyze(
        incident
    )


    alert = alert_manager.create_alert(
        incident,
        risk
    )


    timeline_data = (
        timeline.generate()
    )



    report_data = {

        "incident":
            incident,

        "alert":
            alert,

        "timeline":
            timeline_data

    }



    json_report = (
        reporter.save_json(
            report_data
        )
    )


    markdown_report = (
        reporter.save_markdown(
            report_data
        )
    )



    print("\n")

    print("=" * 50)

    print(
        "INCIDENT DETECTED"
    )

    print("=" * 50)



    print(
        f"""
Title:
{incident['incident']}

Severity:
{incident['severity']}

Risk:
{risk['score']}/100

Risk Level:
{risk['risk']}

MITRE ATT&CK:
"""
    )


    for technique in incident["mitre"]:

        print(
            technique
        )


    print("\nReports Generated:")

    print(
        "JSON:",
        json_report
    )

    print(
        "Markdown:",
        markdown_report
    )

    print("=" * 50)



if __name__ == "__main__":

    main()
