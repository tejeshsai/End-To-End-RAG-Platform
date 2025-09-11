from fastapi import UploadFile, APIRouter, Query, HTTPException
from src.pdfReader import PdfReader
from pydantic import BaseModel
from src.embeddings import embedder
from src.embeddings.vector_store import VectorStore
from src.utils.chunker import chunk_text

class UploadPdfResponse(BaseModel):
    filename : str
    message : str
    text : str
    chunks : int

class SearchQueryResult(BaseModel):
    query : str
    results : str

vector_store = VectorStore(name = "pdf_embeddings")

router = APIRouter()

@router.get("/")
def sucess_response():
    return {"message : Success"}

@router.post("/upload-pdf", response_model = UploadPdfResponse)
async def upload_pdf(file: UploadFile):
    contents = await file.read()
    text = "None"
    try:
        with PdfReader(contents) as r:
            text = r.get_text()
        message = "Pdf Uploaded successfully"
        chunks = chunk_text(text)
        for i, chunk in enumerate(chunks):
            embedding = embedder.embed_text(chunk)
            vector_store.add_documents(doc_id = f"{i}", text = chunk, embedding = embedding)

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing the file : {str(e)}")
     
    return {"filename": file.filename,
            "message": message,
            "text": text,
            "chunks": len(chunks)}

@router.get("/search/", response_model= SearchQueryResult)
async def search(query : str = (Query(..., description="Search Query"))):
    return {"query" : query,
            "results" : "Functionality not implemented"}

@router.get("/semantic-search/", response_model= SearchQueryResult)
async def semantic_search(q : str = (Query(..., description="Search Query"))):
    try:
        query_embedding = embedder.embed_text(q)
        vector_store_results = vector_store.query(query_embedding = query_embedding, k = 3)
        results = vector_store_results["documents"]
        return {"query" : q,
                "results" : results}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing the query : {str(e)}")

