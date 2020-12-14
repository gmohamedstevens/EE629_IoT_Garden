from flask import Flask, render_template, Response, current_app
from camera_opencv import VideoCamera
from sensor import *

# Flask server manager object
class FlaskServer(object):
    app = Flask(__name__)
    app.camera_generator = None
    
    app.light_sensor = MCPSensor(0)
    app.moisture_sensor = MCPSensor(1)
    
    app.pump_relay = Pump("GPIO25")
    app.lamp_relay = Lamp("GPIO24")
    
    # Object initialization
    def __init__(self, cam):
        FlaskServer.app.camera_generator = cam
    
    # Use index.html to format Flask page
    @app.route('/')
    def index():
        # rendering webpage
        return render_template('index.html')
    # Generator for updating live video feed
    def gen(camera):
        while True:
            #get camera frame
            camera.update_frame()
            frame = camera.get_frame()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    
    def gen_text(sensor):
        while True:
            yield str(sensor.read())
            yield 'a'
    # Live video feed of USB camera
    @app.route('/video_feed')
    def video_feed():
        return Response(FlaskServer.gen(current_app.camera_generator),
                        mimetype='multipart/x-mixed-replace; boundary=frame')
    # Live feed of sensor readings
    @app.route('/light_sensor_feed')
    def light_sensor_feed():
        return current_app.light_sensor.return_percentage(0.98, 0.001, 1)
    
    @app.route('/moisture_sensor_feed')
    def moisture_sensor_feed():
        return current_app.moisture_sensor.return_percentage(0.9, 0.25, 1)


