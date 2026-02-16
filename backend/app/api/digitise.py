from fastapi import APIRouter, HTTPException
from app.models.schemas import ParcelDigitiseRequest
from app.api.georef import GEOREF_STORE
from app.services.digitiser import transform_points, compute_centroid

router = APIRouter()

@router.post("/digitise")
def digitise_parcel(data: ParcelDigitiseRequest):

    if data.image_id not in GEOREF_STORE:
        raise HTTPException(status_code=400, detail="Image not georeferenced")

    transform_data = GEOREF_STORE[data.image_id]

    pixel_points = [(p.x, p.y) for p in data.parcel_points]

    ground_coords = transform_points(pixel_points, transform_data)

    centroid = compute_centroid(ground_coords)

    return {
        "ground_coordinates": ground_coords,
        "centroid": centroid,
        "navigation_url": f"https://www.google.com/maps?q={centroid['latitude']},{centroid['longitude']}"
    }
   # navigation_url = f"https://www.google.com/maps?q={centroid['latitude']},{centroid['longitude']}"
