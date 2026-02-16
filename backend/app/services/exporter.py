import csv
import io

def to_geojson(coords):
    return {
        "type": "Feature",
        "geometry": {
            "type": "Polygon",
            "coordinates": [[
                [c["longitude"], c["latitude"]] for c in coords
            ]]
        },
        "properties": {}
    }


def to_csv(coords):
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["easting", "northing", "latitude", "longitude"])

    for c in coords:
        writer.writerow([
            c["easting"],
            c["northing"],
            c["latitude"],
            c["longitude"]
        ])

    return output.getvalue()
