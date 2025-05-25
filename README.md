
# 🗺️ GPS Boundary Tracker Web App

This project is a **real-time GPS tracking web app** built with **Flask + Leaflet.js**. It allows a mobile device to track its live GPS location and draw a connected line on a map — useful for marking field boundaries (e.g., for robots or drones).

> ✅ Designed for use in the field — walk around with your phone and create a geo-boundary in real-time.

---

## 🚀 Features

- 📍 Live GPS location tracking via browser
- 🧭 Connected path visualization on OpenStreetMap
- 💾 Real-time storage of GPS points on the backend
- 📁 Export tracked path as GeoJSON file
- 🔄 Reset and start tracking again
- ⚙️ Backend powered by Flask (Python)
- 🗺️ Frontend built using Leaflet.js

---

## 📦 Project Structure

```
robot_boundary_render_app/
├── app.py                  # Flask server
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Leaflet map UI
├── static/
│   └── path_data.json      # Server-side storage of GPS points
```

---

## 🌐 Live Deployment (Optional)

You can deploy this app on [Render](https://render.com/) or any platform that supports Flask apps.

---

## 💻 Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/gps-boundary-tracker.git
cd gps-boundary-tracker
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask App

```bash
python app.py
```

Then open `http://localhost:5000` on your mobile browser with GPS enabled.

---

## 📲 How It Works

1. The mobile browser uses `navigator.geolocation.watchPosition()` to request the device’s location.
2. Location points are sent via POST request to the Flask backend (`/update`).
3. The path is drawn in real-time on the map using Leaflet.
4. You can reset or export the path as GeoJSON.

---

## 📁 API Endpoints

| Route         | Method | Description                    |
|---------------|--------|--------------------------------|
| `/`           | GET    | Main map UI                    |
| `/update`     | POST   | Add a GPS point to backend     |
| `/reset`      | POST   | Clear saved points             |
| `/export`     | GET    | Download boundary as GeoJSON   |

---

## 🛠 Future Improvements

- Save sessions with timestamps
- Add WebSocket for real-time sync
- Convert to PWA for offline use
- Build native mobile app for millisecond-level updates

---

## 🧠 Use Cases

- Defining outdoor robot movement boundaries
- Field survey and mapping
- Agricultural fencing/planning
- Personal fitness tracking

---

## 📄 License

MIT License

---

## ✨ Author

Made with ❤️ for prototyping GPS-based boundary mapping.
