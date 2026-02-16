from fastapi import APIRouter, HTTPException
from app.api.georef import GEOREF_STORE
from app.services.exporter import to_geojson, to_csv

router = APIRouter()

@router.post("/export")
def export_parcel(data: dict):
    coords = data.get("coordinates")

    if not coords:
        raise HTTPException(status_code=400, detail="No coordinates supplied")

    return {
        "geojson": to_geojson(coords),
        "csv": to_csv(coords)
    }
