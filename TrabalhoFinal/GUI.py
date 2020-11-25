import PySimpleGUI as sg
import random

class GUI:
  
  appTitle = None
  
  themes = sg.theme_list()
  
  menuOptions = [
    ['Arquivo', 
      ['Fechar']
    ],      
    ['Editar', 
      [ 'Temas', 
        themes
      ], 
    ],
    ['Ajuda', 
      ['Sobre']
    ], 
  ]   
  
  camFilters = [
    { "label": 'Sem filtro', "value": 'no_filter' }, 
    { "label": 'Preto e branco', "value": 'black_white' } 
  ]
  
  layout = [
    [ sg.Menu(menuOptions, tearoff=False, pad=(200, 1)) ],
    [ sg.Image(filename='', key='image', size=(500, 500)) ],
    [ sg.HorizontalSeparator(pad=(0, 10)) ],
    [ sg.Text("Selecione um filtro") ],
    [ sg.Radio(item['label'], group_id='filter', enable_events=True, key=item['value']) for item in camFilters ],
    [ sg.HorizontalSeparator(pad=(0, 10)) ],
    [ sg.Button('Tirar Foto'), sg.Button('Fechar') ]
  ]
    
  def __init__(self, appTitle):
    self.appTitle = appTitle
    self.build()
    
  def build(self):
    self.applyTheme(random.choice(self.themes))
    self.window = sg.Window(self.appTitle, self.layout)
    
  def applyTheme(self, theme):
    sg.theme(theme)
    
  def close(self):
    return self.window.Close()
  
  def getEvents(self):
    return self.window.Read(timeout=20, timeout_key='timeout')
  
  def loadFrame(self, frame):
    self.window.FindElement('image').Update(data=frame)
    
  def inputFilename(self):
    hasName = False
    while hasName == False:
      name = sg.popup_get_text('Nome da imagem')
      if(name != ''):
        hasName = True
          
    if (name == None):
      return False
      
    return name
  
  def about(self):
    sg.popup('Sobre o programa', 'Version 0.1', 'FaceCam')   
    
    