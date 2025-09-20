from src.pdfReader import PdfReader
import os
import json
import io


def get_pdf_bytes(pdf_path: str):
    with open(pdf_path, "rb") as f:
        pdf_stream = f.read()
    return pdf_stream


def test_count():
    pdf_stream = get_pdf_bytes("data/sample-local-pdf.pdf")
    with PdfReader(pdf_stream) as r:
        length = r.get_page_count()
        assert length > 0
        assert length == 3, "Length is not correct"


def test_sample_json():
    pdf_stream = get_pdf_bytes("data/sample-local-pdf.pdf")
    with PdfReader(pdf_stream) as r:
        r.save_json("tests/test_output/sample.json")

        assert os.path.exists("tests/test_output/sample.json"), FileExistsError(
            "File not found"
        )

    with open("tests/test_output/sample.json", "r") as j:
        data = json.load(j)

    assert "length" in data
    assert "pages" in data

    assert "page_number" in data["pages"][0]
    assert "page_text" in data["pages"][0]


def test_text():
    pdf_stream = get_pdf_bytes("data/sample-local-pdf.pdf")
    with PdfReader(pdf_stream) as r:
        assert r.get_text() is not None
