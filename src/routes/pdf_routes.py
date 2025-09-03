from fastapi import UploadFile, APIRouter, Query, HTTPException
from src.pdfReader import PdfReader
from pydantic import BaseModel

class UploadPdfResponse(BaseModel):
    filename : str
    type : str
    message : str
    text : str

class SearchQueryResult(BaseModel):
    query : str
    results : str

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
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing the file : {str(e)}")
     
    return {"filename": file.filename,
            "type": str(type(contents)),
            "message": message,
            "text": text}

@router.get("/search/", response_model= SearchQueryResult)
async def search(query : str = (Query(..., description="Search Query"))):
    return {"query" : query,
            "results" : "Functionality not implemented"}