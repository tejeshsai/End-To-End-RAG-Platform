from fastapi.testclient import TestClient
from pathlib import Path
from unittest.mock import patch
from src.main import app

client = TestClient(app)

def test_upload_pdf():
    # Mock embeddings to match Chroma's expected dimension (1536)
    with patch("src.embeddings.embedder.embed_text", return_value = [0.0] * 1536):
        pdf_path = Path("data/sample-local-pdf.pdf")
        with pdf_path.open("rb") as f:
            response = client.post(
                "/upload-pdf", files = {"file":("sample-local-pdf.pdf", f, "application/pdf")}
            )
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["filename"] == "sample-local-pdf.pdf"
    assert "Pdf Uploaded successfully" in json_data["message"]
    assert "This PDF is three pages long. Three long pages. Or three short pages" in json_data["text"]
    assert json_data["chunks"] == 18

def test_search_query():
    response = client.get(
        "/search?query=python"
    )
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["query"] == "python"
    assert "results" in json_data