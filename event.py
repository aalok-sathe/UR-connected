import time

class Event: 

    keywords = list()
    timestamp = None
    seconds = None
    body = None
    title = None
    location = None
    
    attendees = list()
    thumbs = list((0,0))
    expiry = None
  
    def __init__(self, title=None, body=None, location=None, user=None, keywords_dict=None):
        self.title = str(title)
        self.body = str(body)
        self.location = str(location)
        self.seconds = time.time()
        self.timestamp = datetime.datetime.fromtimestamp(self.seconds).strftime('%Y-%m-%d %H:%M:%S')
        
