"""
Digital forensic evidence tracking
"""

from datetime import datetime
import uuid


def create_case():

    return {

        "case_id":

            "CASE-"
            +
            datetime.now()
            .strftime("%Y%m%d")
            +
            "-"
            +
            str(uuid.uuid4())[:8],

        "created":

            datetime.now()
            .isoformat()

    }



def create_evidence_record(file_path):

    return {

        "evidence_id":

            str(uuid.uuid4()),

        "file":

            file_path,

        "collected":

            datetime.now()
            .isoformat(),

        "chain_of_custody":

            [

                {

                    "action":
                    "Evidence collected",

                    "time":
                    datetime.now()
                    .isoformat()

                }

            ]

    }



def create_timeline(metadata):

    return [

        {

            "event":
            "File Created",

            "timestamp":
            metadata.get("created")

        },

        {

            "event":
            "File Modified",

            "timestamp":
            metadata.get("modified")

        }

    ]
