import os
import json
from flask import Flask, render_template, request, jsonify, send_file

app = Flask(__name__)
DATA_FILE = os.path.join("static", "path_data.json")

# Ensure data file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/update", methods=["POST"])
def update():
    data = request.get_json()
    with open(DATA_FILE, "r+") as f:
        path = json.load(f)
        path.append(data)
        f.seek(0)
        json.dump(path, f)
        f.truncate()
    return jsonify({"status": "success"})

@app.route("/export")
def export():
    with open(DATA_FILE, "r") as f:
        path = json.load(f)
    geojson = {
        "type": "Feature",
        "geometry": {
            "type": "LineString",
            "coordinates": [[pt["lng"], pt["lat"]] for pt in path]
        },
        "properties": {}
    }
    geojson_file = os.path.join("static", "boundary.geojson")
    with open(geojson_file, "w") as f:
        json.dump(geojson, f)
    return send_file(geojson_file, as_attachment=True)

@app.route("/reset", methods=["POST"])
def reset():
    with open(DATA_FILE, "w") as f:
        json.dump([], f)
    return jsonify({"status": "reset"})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)
