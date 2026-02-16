from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.convert import router as convert_router
from app.api.upload import router as upload_router
from app.api.georef import router as georef_router
from app.api.digitise import router as digitise_router
from app.api.export import router as export_router
from fastapi.responses import FileResponse
import os



# Get absolute path to static folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, "static")



app = FastAPI(title="Plan2Ground API")

app.mount("/plans", StaticFiles(directory="app/uploads/plans"), name="plans")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

app.include_router(convert_router)
app.include_router(upload_router)
app.include_router(georef_router)
app.include_router(digitise_router)
app.include_router(export_router)


@app.get("/")
def read_index():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))
