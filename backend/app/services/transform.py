from pyproj import CRS, Transformer

ACCRA_GRID = CRS.from_proj4("""
+proj=tmerc
+lat_0=4.666666667
+lon_0=-1
+k=0.99975
+x_0=274320
+y_0=0
+a=6378300
+rf=296
+units=ft
+no_defs
""")


WGS84 = CRS.from_epsg(4326)

transformer = Transformer.from_crs(ACCRA_GRID, WGS84, always_xy=True)

def accra_to_wgs84(easting: float, northing: float):
    lon, lat = transformer.transform(easting, northing)
    return lat, lon
