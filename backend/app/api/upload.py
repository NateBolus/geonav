from fastapi import APIRouter, UploadFile, File
import shutil
import os

router = APIRouter()

UPLOAD_DIR = "app/uploads/plans"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload-plan")
async def upload_plan(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "image_url": f"/plans/{file.filename}"
    }
