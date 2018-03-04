#import time
import pickle
from pathlib import Path

class Event:

    keywords = list()
    timestamp = None
    seconds = None
    body = None
    title = None
    location = None
    identity = None
    thumbs_up_users = set()
    thumbs_down_users = set()
    expiry = None

    def __init__(self, identity, title, body, location, user, keywords_list):

        self.identity = identity
        self.title = str(title)
        self.body = str(body)
        self.location = str(location)
        #self.seconds = time.time()
        self.keywords = keywords_list
        #self.timestamp = datetime.datetime.fromtimestamp(self.seconds).strftime('%Y-%m-%d %H:%M:%S')

    def get_num_upvotes(self):
        return len(self.thumbs_up_users)

    def get_num_downvotes(self):
        return len(self.thumbs_up_users)

    def thumb_up(self, user_name):
        self.thumbs_up_users.add(user_name)
        self.thumbs_down_users.remove(user_name)
        self.dump_data()

    def thumb_down(self, user_name):
        self.thumbs_down_users.add(user_name)
        self.thumbs_up_users.remove(user_name)
        self.dump_data()

    def read_data(self, event_name=None):
        if Path("events_db/" + str(event_name)).is_file():
            data_dict = pickle.load(open("events_db/" + str(event_name), "rb"))
            self.thumbs_up_users = data_dict.get("thumbups")
            self.thumbs_down_users = data_dict.get("thumbdowns")
            #self.attendees = data_dict.get("attendees")

    def dump_data(self):
            data_dict = dict()
            data_dict["thumbups"] = self.thumbs_up_users
            data_dict["thumbdowns"] = self.thumbs_down_users

