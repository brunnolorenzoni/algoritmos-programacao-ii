import os
from GUI import GUI
from Webcam import Webcam

class FaceCam:
  
  path = os.path.abspath(os.getcwd())
  imagesFolderName = 'images'
  imagesDir = None
  appTitle = 'FaceCam'
  
  def __init__(self):
    self.createFolder(self.imagesFolderName)
    self.startup()
  
  def createFolder(self, dirName):
    if not os.path.exists(dirName):
      os.makedirs(dirName)
      
    self.imagesDir = f"{self.path}/{self.imagesFolderName}/"
    print(self.imagesDir)
      
  def startup(self):
       
    gui = GUI(self.appTitle)
    webcam = Webcam()
    
    while True:
      frame = webcam.getFrame()
      event, values = gui.getEvents() 
      
      gui.loadFrame(webcam.frame_to_data(frame))
    
      if(event == 'Tirar Foto'):
        filename = gui.inputFilename()
        
        if(filename):
          webcam.take_photo(self.imagesDir, filename)
    
      if([event for item in gui.camFilters if item['value'] == event]):
        webcam.applyFilter(event)
        
      if event == 'Sobre':   
        gui.about()   
        
      if ([event for tema in gui.themes if tema == event]):   
        gui.applyTheme(event)
      
      if (event is None or event == 'Fechar'):
        webcam = webcam.off()
        break
      
    gui = gui.close()