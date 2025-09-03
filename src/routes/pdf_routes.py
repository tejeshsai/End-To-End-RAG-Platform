from fastapi import UploadFile, APIRouter, Query
from src.pdfReader import PdfReader
import io

router = APIRouter()

@router.get("/")
def sucess_response():
    return {"message : Success"}

@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile):
    contents = await file.read()
    text = "None"
    try:
        # PdfReader expects raw bytes; it wraps internally as needed
        with PdfReader(contents) as r:
            text = r.get_text()
        message = "Pdf Uploaded successfully"
    except Exception as e:
        # Return graceful error payload instead of raising
        return {"filename": file.filename,
                "type": str(type(contents)),
                "message": "Wrong format",
                "text": str(e)}
        
    return {"filename": file.filename,
            "type": str(type(contents)),
            "message": message,
            "text": text}

@router.get("/search/")
async def search(query : str = (Query(..., description="Search Query"))):
    return {"query" : query,
            "results" : "Functionality not implemented"}