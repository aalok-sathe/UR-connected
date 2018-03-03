import time

class Request: 

    keywords = list()
    timestamp = None
    message = ""
    location = ""
  
  def __init__(self, stringMessage, stringLocation):
    self.message = stringMessage
    self.location = stringLocation
    self.timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

