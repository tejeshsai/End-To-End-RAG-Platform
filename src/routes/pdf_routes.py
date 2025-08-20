from fastapi import UploadFile, APIRouter

router = APIRouter(prefix="/pdf")

@router.get("/")
def test_response():
    return {"message : Success"}