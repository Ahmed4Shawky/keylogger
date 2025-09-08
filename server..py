from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

UPLOAD_FOLDER = "received_logs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/api/logs", methods=["POST"])
def receive_logs():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    # Save the encrypted log file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    save_path = os.path.join(UPLOAD_FOLDER, f"log_{timestamp}.dat")
    file.save(save_path)

    return jsonify({"status": "success", "path": save_path}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # Render uses port 10000
