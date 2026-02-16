from fastapi import APIRouter
from pydantic import BaseModel
from pyproj import Transformer

router = APIRouter()

class ConvertRequest(BaseModel):
    parcel: list  # [[lat, lon], ...]

@router.post("/export")
def convert_coordinates(data: ConvertRequest):

    transformer = Transformer.from_crs("EPSG:4326", "EPSG:2136", always_xy=True)

    transformed = []

    for lat, lon in data.parcel:
        x, y = transformer.transform(lon, lat)
        transformed.append({
            "easting": x,
            "northing": y
        })

    return {
        "coordinates": transformed
    }
