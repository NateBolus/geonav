let map = L.map('map').setView([5.6037, -0.1870], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap'
}).addTo(map);

let uploadedImageLayer = null;
let georefPoints = [];
let parcelPoints = [];
let georefMode = false;
let digitiseMode = false;

// USER LOCATION
if (navigator.geolocation) {
    navigator.geolocation.watchPosition(function(position) {
        let lat = position.coords.latitude;
        let lon = position.coords.longitude;

        if (!window.userMarker) {
            window.userMarker = L.marker([lat, lon]).addTo(map)
                .bindPopup("You are here");
        } else {
            window.userMarker.setLatLng([lat, lon]);
        }
    });
}

// =====================
// UPLOAD PLAN
// =====================
async function uploadPlan() {
    const fileInput = document.getElementById('planUpload');
    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    const response = await fetch("/upload-plan", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    overlayImage(data.image_url);
}

function overlayImage(url) {
    if (uploadedImageLayer) {
        map.removeLayer(uploadedImageLayer);
    }

    let bounds = [[5.5, -0.3], [5.7, 0.0]]; // temporary bounds
    uploadedImageLayer = L.imageOverlay(url, bounds).addTo(map);
    map.fitBounds(bounds);
}

// =====================
// GEOREFERENCE
// =====================
function startGeoref() {
    georefMode = true;
    digitiseMode = false;
    georefPoints = [];
    alert("Click 4 known control points on the image.");
}

function startDigitise() {
    digitiseMode = true;
    georefMode = false;
    parcelPoints = [];
    alert("Click parcel corner points.");
}

map.on("click", async function(e) {

    if (georefMode) {
        georefPoints.push([e.latlng.lat, e.latlng.lng]);
        L.circleMarker(e.latlng).addTo(map);

        if (georefPoints.length === 4) {
            georefMode = false;

            const response = await fetch("/georeference", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({ points: georefPoints })
            });

            const result = await response.json();

            overlayImage(result.georef_image_url);
            alert("Georeferencing completed.");
        }
    }

    if (digitiseMode) {
        parcelPoints.push([e.latlng.lat, e.latlng.lng]);
        L.circleMarker(e.latlng, {color: "yellow"}).addTo(map);
    }
});

// =====================
// EXPORT
// =====================
async function exportParcel() {
    const response = await fetch("/export", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ parcel: parcelPoints })
    });

    const data = await response.json();

    alert("Coordinates exported successfully.");
}

// =====================
// NAVIGATE TO PARCEL
// =====================
function navigateToParcel() {
    if (!parcelPoints.length) return;

    let center = parcelPoints[0];

    if (window.userMarker) {
        let userLatLng = window.userMarker.getLatLng();

        let routeUrl = `https://www.google.com/maps/dir/${userLatLng.lat},${userLatLng.lng}/${center[0]},${center[1]}`;
        window.open(routeUrl, "_blank");
    }
}
