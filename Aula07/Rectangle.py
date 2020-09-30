class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    
  def area(self):
    return (self.width * self.height)
  
  def print_me(self):
    return print(self.__dict__)
  