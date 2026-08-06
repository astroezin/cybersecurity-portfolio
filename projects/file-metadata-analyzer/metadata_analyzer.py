"""
File Metadata Analyzer

Professional digital forensic analysis CLI.
"""

import argparse
import logging


from core.config import (
    ensure_directories,
    LOG_FILE
)

from core.metadata import (
    get_basic_metadata,
    extract_image_metadata,
    extract_pdf_metadata,
    extract_office_metadata
)

from core.hashing import (
    calculate_hashes
)

from core.malware import (
    calculate_entropy,
    yara_scan,
    virustotal_lookup
)

from core.forensic import (
    create_case,
    create_evidence_record,
    create_timeline
)

from core.detection import (
    detect_suspicious_metadata
)

from core.reporter import (
    generate_report
)



def parse_arguments():

    parser = argparse.ArgumentParser(
        description="File Metadata Analyzer"
    )


    parser.add_argument(
        "file",
        help="File to analyze"
    )


    return parser.parse_args()



def setup_logging():

    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format=(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(message)s"
        )
    )



def collect_extra_metadata(
        file_path,
        mime_type
):

    extra_metadata = {}


    try:

        if mime_type:

            if "image" in mime_type:

                extra_metadata.update(
                    extract_image_metadata(
                        file_path
                    )
                )


            elif "pdf" in mime_type:

                extra_metadata.update(
                    extract_pdf_metadata(
                        file_path
                    )
                )


        office_metadata = extract_office_metadata(
            file_path
        )


        extra_metadata.update(
            office_metadata
        )


    except Exception as error:

        extra_metadata = {

            "error":
            str(error)

        }


    return extra_metadata



def main():

    ensure_directories()

    setup_logging()


    logging.info(
        "File Metadata Analyzer started"
    )


    args = parse_arguments()


    file_path = args.file


    logging.info(
        f"Analyzing file: {file_path}"
    )


    metadata = get_basic_metadata(
        file_path
    )


    hashes = calculate_hashes(
        file_path
    )


    logging.info(
        "Hash calculation completed"
    )


    entropy = calculate_entropy(
        file_path
    )


    analysis = {

        "entropy":
            entropy,


        "yara":
            yara_scan(
                file_path
            ),


        "virustotal":
            virustotal_lookup(
                hashes["sha256"]
            ),


        "suspicious_metadata":
            detect_suspicious_metadata(
                file_path,
                entropy
            )

    }


    extra_metadata = collect_extra_metadata(
        file_path,
        metadata["mime_type"]
    )


    case = create_case()


    evidence = create_evidence_record(
        file_path
    )


    timeline = create_timeline(
        metadata
    )


    report_data = {

        "case":
            case,


        "evidence":
            evidence,


        "metadata":
            metadata,


        "extra_metadata":
            extra_metadata,


        "hashes":
            hashes,


        "analysis":
            analysis,


        "timeline":
            timeline

    }


    report = generate_report(
        report_data
    )


    logging.info(
        "Report generated successfully"
    )


    print(
        "=" * 60
    )

    print(
        "FILE METADATA ANALYZER"
    )

    print(
        "=" * 60
    )


    print()

    print(
        f"File: {file_path}"
    )


    print(
        f"SHA256: {hashes['sha256']}"
    )


    print(
        f"Entropy: {entropy}"
    )


    print()

    print(
        "Suspicious Findings:"
    )


    if analysis["suspicious_metadata"]:

        for finding in analysis["suspicious_metadata"]:

            print(
                f"- {finding}"
            )


    else:

        print(
            "- None"
        )


    print()

    print(
        "Reports Generated:"
    )


    print(
        f"JSON: {report['json']}"
    )


    print(
        f"Markdown: {report['markdown']}"
    )


    logging.info(
        "File Metadata Analyzer completed"
    )



if __name__ == "__main__":

    main()
