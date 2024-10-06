import threading
from flask import Flask, render_template, Response
from flask_socketio import SocketIO
import cv2
import time
from lane_detection_stream import process_single_frame, cap # all camera functions are in lane_detection_stream.py
from motor_functions import init, forward # all movement functions are in motor_functions.py
from globals import left_dist, right_dist #left_dist and right_dist are in globals.py

app = Flask(__name__)
socketio = SocketIO(app)

# Global flag to control the car loop
running = True

def car_control_loop():
    global running
    init()  # Initialize GPIO
    while running:
        left, right = left_dist, right_dist
        if left == 'N/A' or right == 'N/A':
            forward()
        # Compare the left and right distances
        elif left < right:
            #move to the right
            pass
        elif right < left:
            #move to the left
            pass
        else:
            forward()
        time.sleep(0.5)  # Small delay to prevent overwhelming the system

def generate_frames():
    while True:
        frame= process_single_frame()
        if frame is None:
            break
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # Start the car control loop in a separate thread
    car_thread = threading.Thread(target=car_control_loop)
    car_thread.start()

    # Run the Flask app
    try:
        socketio.run(app, host='0.0.0.0', port=5000, debug=False)
    finally:
        running = False  # Stop the car control loop
        car_thread.join()  # Wait for the car control thread to finish
        #stop()  # Stop the motors
        cap.release()  # Release the camera
        cv2.destroyAllWindows()