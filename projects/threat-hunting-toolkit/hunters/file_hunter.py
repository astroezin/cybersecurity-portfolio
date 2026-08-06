"""
File Threat Hunter

Searches files for suspicious indicators
using hashes and file characteristics.
"""

import hashlib
from pathlib import Path


class FileHunter:
    """
    Performs file-based threat hunting.
    """


    def __init__(self, suspicious_hashes=None):

        self.suspicious_hashes = (
            suspicious_hashes or []
        )


    def calculate_sha256(self, filepath):
        """
        Calculate SHA256 hash of file.
        """

        sha256 = hashlib.sha256()

        with open(
            filepath,
            "rb"
        ) as file:

            while chunk := file.read(4096):

                sha256.update(chunk)


        return sha256.hexdigest()



    def analyze_file(self, filepath):
        """
        Analyze a single file.
        """

        path = Path(filepath)

        result = {

            "file":
                str(path),

            "exists":
                path.exists(),

            "sha256":
                None,

            "suspicious":
                False

        }


        if not path.exists():

            return result



        file_hash = (
            self.calculate_sha256(
                filepath
            )
        )


        result["sha256"] = file_hash



        if file_hash in self.suspicious_hashes:

            result["suspicious"] = True



        return result
