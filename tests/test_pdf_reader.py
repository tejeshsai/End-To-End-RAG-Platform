from src.pdfReader import PdfReader
import pytest
import os

def test_count():
    with PdfReader("data/sample-local-pdf.pdf") as r:
        length = r.get_page_count()
        assert length > 0

def test_sample_json():
    with PdfReader("data/sample-local-pdf.pdf") as r:
        r.save_json("tests/test_output/sample.json")
    
        assert os.path.exists("tests/test_output/sample.json"), FileExistsError("File not found")
