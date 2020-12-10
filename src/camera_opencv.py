import cv2
import datetime 

class VideoCamera(object):
    
    video = cv2.VideoCapture(0)
    image = None
    class_count = 0
    
    # Object initialization
    def __init__(self):
        self.instance_count = 0
        self.update_frame()

    # Release object
    def __del__(self):
        VideoCamera.video.release()
        
    def update_frame(self):
        success, VideoCamera.image = VideoCamera.video.read()
        xpos = 10
        ypos = 475
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontsize = 0.75
        color = (255, 255, 255)
        thickness = 2
        string = str(datetime.datetime.now())
        VideoCamera.image = cv2.putText(VideoCamera.image, string, (xpos - 2, ypos + 2), font, fontsize, (0, 0, 0), thickness, cv2.LINE_AA)
        VideoCamera.image = cv2.putText(VideoCamera.image, string, (xpos,ypos), font, fontsize, color, thickness, cv2.LINE_AA)
        
    # Get a frame from the USB camera; for use with Flask server genertor
    def get_frame(self):
        ret, jpeg = cv2.imencode('.jpg', VideoCamera.image)
        return jpeg.tobytes()
    
    def timelapse_photo(self):
        cv2.imwrite('img/' + str(datetime.datetime.now()) + '.jpg', VideoCamera.image)
