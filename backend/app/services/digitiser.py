import numpy as np
from app.services.georef import apply_affine, apply_projective
from app.services.crs import to_wgs84

def transform_points(points, transform_data):
    matrix = transform_data["matrix"]
    ttype = transform_data["type"]

    transformed = []

    for p in points:
        x, y = p

        if ttype == "AFFINE":
            gx, gy = apply_affine(matrix, (x, y))
        else:
            gx, gy = apply_projective(matrix, (x, y))

        wgs = to_wgs84(gx, gy)

        transformed.append({
            "easting": gx,
            "northing": gy,
            "latitude": wgs["latitude"],
            "longitude": wgs["longitude"]
        })

    return transformed



def compute_centroid(coords):
    xs = [c["easting"] for c in coords]
    ys = [c["northing"] for c in coords]

    cx = sum(xs) / len(xs)
    cy = sum(ys) / len(ys)

    wgs = to_wgs84(cx, cy)

    return {
        "easting": cx,
        "northing": cy,
        "latitude": wgs["latitude"],
        "longitude": wgs["longitude"]
    }
