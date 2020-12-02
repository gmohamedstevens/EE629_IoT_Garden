import cv2
import datetime 
#face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
#ds_factor=0.6

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        # tae photo from camera
        success, image = self.video.read() # take photo from camera
        # add timestamp to photo
        xpos = 10
        ypos = 475
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontsize = 0.75
        color = (255, 255, 255)
        thickness = 2
        image = cv2.putText(image, str(datetime.datetime.now()), (xpos,ypos), font, fontsize, color, thickness, cv2.LINE_AA)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()