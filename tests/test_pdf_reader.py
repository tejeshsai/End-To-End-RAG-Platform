from src.pdfReader import PdfReader
import os
import json

def test_count():
    with PdfReader("data/sample-local-pdf.pdf") as r:
        length = r.get_page_count()
        assert length > 0
        assert length == 3, "Length is not correct"

def test_sample_json():
    with PdfReader("data/sample-local-pdf.pdf") as r:
        r.save_json("tests/test_output/sample.json")
    
        assert os.path.exists("tests/test_output/sample.json"), FileExistsError("File not found")

    with open("tests/test_output/sample.json", "r") as j:
        data = json.load(j)

    assert "pdf_file_path" in data
    assert "length" in data
    assert "pages" in data

    assert "page_number" in data["pages"][0]
    assert "page_text" in data["pages"][0]

def test_text():
    with PdfReader("data/sample-local-pdf.pdf") as r:
        assert r.get_text() is not None

