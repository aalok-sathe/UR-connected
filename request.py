import time

class Request:

  message = ""
  location = ""
  currentTime = time.time() 
  
  def __init__(self, stringMessage, stringLocation):
    self.message = stringMessage
    self.location = stringLocation


