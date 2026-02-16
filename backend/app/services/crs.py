from pyproj import Transformer

# Ghana National Grid → WGS84
ghana_to_wgs84 = Transformer.from_crs(
    "EPSG:2136",
    "EPSG:4326",
    always_xy=True
)

def to_wgs84(easting: float, northing: float):
    lon, lat = ghana_to_wgs84.transform(easting, northing)
    return {
        "latitude": lat,
        "longitude": lon
    }
