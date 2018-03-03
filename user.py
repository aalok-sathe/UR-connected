#! /bin/env/ python3
from event import Event

class User:

    user_name = ""
    user_events = list()
    user_upvoted = list()
    user_downvoted = list()

    def __init__(self, stringName = ""):
        self.user_name = stringName

    def addEvent(self, event):
    	self.user_events.add(event)

    def addUpvoted(self, event):
    	self.user_upvoted.add(event)

    def addDownvoted(self, event):
    	self.user_downvoted.add(event)
    	    	        
