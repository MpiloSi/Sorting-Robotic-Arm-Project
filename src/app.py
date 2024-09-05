from flask import Flask, render_template, jsonify, request
from api.camera_api import CameraAPI
from api.control_api import ControlAPI

app = Flask(__name__)

# Initialize APIs
camera_api = CameraAPI()
control_api = ControlAPI()

# Main route for frontend UI
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/control-panel')
def control_panel():
    return render_template('control_panel.html')

# API route for camera feed
@app.route('/api/camera-feed', methods=['GET'])
def get_camera_feed():
    frame = camera_api.capture_image()
    return jsonify({"image": frame})



# API route for starting and stopping the robotic arm
@app.route('/api/start-sorting', methods=['POST'])
def start_sorting():
    control_api.start_sorting()
    return jsonify({"status": "Sorting started"})

@app.route('/api/stop-sorting', methods=['POST'])
def stop_sorting():
    control_api.stop_sorting()
    return jsonify({"status": "Sorting stopped"})

if __name__ == '__main__':
    app.run(debug=True)
