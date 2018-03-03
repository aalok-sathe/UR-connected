import time

class Request:

  keywords = list()
  timestamp = None
  seconds = None
  message = ""
  location = ""
  
  
    def __init__(self, stringMessage, stringLocation):
        self.message = stringMessage
        self.location = stringLocation
        self.seconds = time.time()
        self.timestamp = datetime.datetime.fromtimestamp(self.seconds).strftime('%Y-%m-%d %H:%M:%S')

