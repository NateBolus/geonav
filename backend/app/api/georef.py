from fastapi import APIRouter
from pydantic import BaseModel
import numpy as np
import cv2
import os

router = APIRouter()

class GeorefRequest(BaseModel):
    points: list  # [[lat, lon], ...]

@router.post("/georeference")
def georeference(data: GeorefRequest):

    image_path = "app/uploads/plans/your_uploaded_file.png"
    image = cv2.imread(image_path)

    # Image pixel corners
    h, w = image.shape[:2]

    src_pts = np.float32([
        [0, 0],
        [w, 0],
        [w, h],
        [0, h]
    ])

    dst_pts = np.float32([
        [p[1], p[0]] for p in data.points
    ])

    matrix = cv2.getPerspectiveTransform(src_pts, dst_pts)

    warped = cv2.warpPerspective(image, matrix, (w, h))

    output_path = "app/uploads/plans/georef.png"
    cv2.imwrite(output_path, warped)

    return {
        "georef_image_url": "/plans/georef.png"
    }
