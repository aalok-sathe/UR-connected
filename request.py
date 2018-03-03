import time


class Request:

  message = ""
  location = ""
  currentTime = time.time() 
  keywords = list()
  timestamp = None

  
  def __init__(self, stringMessage, stringLocation):
    self.message = stringMessage
    self.location = stringLocation
    self.timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
   
