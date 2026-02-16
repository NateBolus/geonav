from pydantic import BaseModel

class CoordinateInput(BaseModel):
    easting: float
    northing: float

class CoordinateOutput(BaseModel):
    latitude: float
    longitude: float

class PixelPoint(BaseModel):
    x: float
    y: float

class GroundPoint(BaseModel):
    easting: float
    northing: float

class ControlPoint(BaseModel):
    pixel: PixelPoint
    ground: GroundPoint

class GeorefRequest(BaseModel):
    image_id: str
    transform_type: str  # "AFFINE" or "PROJECTIVE"
    control_points: list[ControlPoint]

class DigitisePoint(BaseModel):
    x: float
    y: float

class ParcelDigitiseRequest(BaseModel):
    image_id: str
    parcel_points: list[DigitisePoint]
