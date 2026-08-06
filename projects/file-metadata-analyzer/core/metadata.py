"""
Metadata extraction engine
"""

from pathlib import Path
from datetime import datetime
import mimetypes


def get_basic_metadata(file_path):

    path = Path(file_path)

    stats = path.stat()


    metadata = {

        "filename": path.name,

        "absolute_path": str(path.absolute()),

        "size_bytes": stats.st_size,

        "created":

            datetime.fromtimestamp(
                stats.st_ctime
            ).isoformat(),

        "modified":

            datetime.fromtimestamp(
                stats.st_mtime
            ).isoformat(),

        "mime_type":

            mimetypes.guess_type(
                file_path
            )[0]

    }


    return metadata


def extract_image_metadata(file_path):

    try:

        from PIL import Image


        image = Image.open(
            file_path
        )


        return {

            "format": image.format,

            "mode": image.mode,

            "size": image.size,

            "exif":

                dict(
                    image.getexif()
                )

        }


    except Exception:

        return {}
    

def extract_pdf_metadata(file_path):

    try:

        from PyPDF2 import PdfReader


        reader = PdfReader(
            file_path
        )


        return {

            "pdf_metadata":

                dict(
                    reader.metadata
                )

        }


    except Exception:

        return {}


def extract_office_metadata(file_path):

    metadata = {}


    try:

        if file_path.endswith(".docx"):

            from docx import Document


            doc = Document(
                file_path
            )


            metadata = {

                "author":
                doc.core_properties.author,

                "title":
                doc.core_properties.title

            }


    except Exception:

        pass


    return metadata
