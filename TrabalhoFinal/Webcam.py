import numpy as np
import cv2
import time

class Webcam: 
  
  webcam = None
  frame = None
  current_filter = 'no_filter'
  
  def __init__(self):
    self.webcam = cv2.VideoCapture(0) 
    
  def off(self):
    self.webcam = self.webcam.release()
    
  def getFrame(self):
    webcam_read = self.webcam.read()[1]
    if(self.current_filter == 'no_filter'):
      self.frame = webcam_read
    else:
      self.frame = self.frame_grayscale(webcam_read)
    
    return self.frame

  def frame_grayscale(self, frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_3_channels = np.zeros_like(frame)
    gray_3_channels[:, :, 0] = gray
    gray_3_channels[:, :, 1] = gray
    gray_3_channels[:, :, 2] = gray
    return gray_3_channels

  def frame_to_data(self, frame):
    return cv2.imencode('.png', frame)[1].tobytes()

  def applyFilter(self, event):
    self.current_filter = event

  def take_photo(self, imagesDir, filename):
    timestamp = str(int(time.time()))
    filename = f"{timestamp}_{filename}.jpg"
    try:
      cv2.imwrite((imagesDir + filename), self.frame)
    except Exception as error:
      print(error.args[1])