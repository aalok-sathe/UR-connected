import time

class Request: 

    keywords = list()
    timestamp = None
  
  def __init__(self, stringMessage):
    self.message = stringMessage

    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
