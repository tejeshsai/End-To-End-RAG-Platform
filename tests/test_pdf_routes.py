from fastapi.testclient import TestClient
from pathlib import Path
from unittest.mock import patch
from src.main import app

client = TestClient(app)


def test_upload_pdf():
    # Mock embeddings to match Chroma's expected dimension (1536)
    with patch("src.embeddings.embedder.embed_text", return_value=[0.0] * 1536):
        pdf_path = Path("data/sample-local-pdf.pdf")
        with pdf_path.open("rb") as f:
            response = client.post(
                "/upload-pdf",
                files={"file": ("sample-local-pdf.pdf", f, "application/pdf")},
            )
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["filename"] == "sample-local-pdf.pdf"
    assert "Pdf Uploaded successfully" in json_data["message"]
    assert (
        "This PDF is three pages long. Three long pages. Or three short pages"
        in json_data["text"]
    )
    assert json_data["chunks"] == 18


def test_search_query():
    response = client.get("/search?query=python")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["query"] == "python"
    assert "results" in json_data


def test_ask_query():
    with patch("src.services.rag_service.create_retrieval_chain") as mock_chain:
        # Mock the chain response
        mock_chain.return_value.invoke.return_value = {
            "answer": "Returned Test Answer"}
        response = client.get("/ask?q=who%20is%20the%20author?")
        # TEMP: Debug the 400 error
        if response.status_code != 200:
            print(f"Status: {response.status_code}")
            print(f"Response: {response.text}")
            assert False, f"Expected 200, got {response.status_code}: {response.text}"
        assert response.status_code == 200
        json_data = response.json()
        assert json_data["results"] == "Returned Test Answer"
