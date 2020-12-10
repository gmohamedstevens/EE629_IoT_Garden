import cv2
import datetime 

class VideoCamera(object):
    # Object initialization
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    # Release object
    def __del__(self):
        self.video.release()
    # Get a frame from the USB camera; for use with Flask server genertor
    def get_frame(self):
        # take photo from camera
        success, image = self.video.read() # take photo from camera
        # add timestamp to photo
        xpos = 10
        ypos = 475
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontsize = 0.75
        color = (255, 255, 255)
        thickness = 2
        image = cv2.putText(image, str(datetime.datetime.now()), (xpos,ypos), font, fontsize, color, thickness, cv2.LINE_AA)
        # Convert to acceptable image and return
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()