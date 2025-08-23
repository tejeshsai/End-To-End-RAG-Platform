from fastapi import UploadFile, APIRouter
from src.pdfReader import PdfReader
import io

router = APIRouter()

@router.get("/")
def test_response():
    return {"message : Success"}

@router.post("/uploadpdf/")
async def test_upload_pdf(file: UploadFile):
    contents = await file.read()
    try:
        pdf_stream = io.BytesIO(contents)  # Convert bytes to BytesIO
        with PdfReader(pdf_stream) as r:
            text = r.get_text()
    except Exception as e:
        text = str(e)
        raise Exception(f"Error while reading uploaded file")
    return {"filename": file.filename,
            "type":str(type(contents)),
            "text":text}