from flask import Flask, render_template, Response
from camera_opencv import VideoCamera

# Flask server manager object
class FlaskServer(object):
    app = Flask(__name__)
    # Use index.html to format Flask page
    @app.route('/')
    def index():
        # rendering webpage
        return render_template('index.html')
    # Generator for updating live video feed
    def gen(camera):
        while True:
            #get camera frame
            frame = camera.get_frame()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
           
    def gen_text():
        yield "a"
        yield "b"
    # Live video feed of USB camera
    @app.route('/video_feed')
    def video_feed():
        return Response(FlaskServer.gen(VideoCamera()),
                        mimetype='multipart/x-mixed-replace; boundary=frame')
    # Live feed of sensor readings
    @app.route('/text_feed')
    def text_feed():
        return Response(FlaskServer.gen_text(),
                        mimetype='multipart/x-mixed-replace; boundary=frame')


