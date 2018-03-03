#! /bin/env/ python3
from event import Event

class User:

    user_name = ""
    user_events = list()
    user_upvoted = list()
<<<<<<< HEAD
    #user_downvoted = list()
    #user_attending = list()
    
=======
    user_downvoted = list()
>>>>>>> d051f3032e5cb72bed08f5f9dce263602a1acae3

    def __init__(self, stringName = ""):
        self.user_name = stringName

    def addEvent(self, event):
    	self.user_events.add(event)

    def addUpvoted(self, event):
    	self.user_upvoted.add(event)

    def addDownvoted(self, event):
    	self.user_downvoted.add(event)
    	    	        
