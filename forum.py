#! /bin/env/ python3

from event import Event
from user import User

import pickle
from cmd import Cmd
import tkinter as tk
from tkinter import *
from pathlib import Path


class FacilitiesForum(tk.Frame):
    
    event_queue = list() # of events
    users_db = dict()
    current_user = None
    
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pack(fill=tk.BOTH)
        
        # Load users database if it exists
        if Path("db/UR_connected_users_db").is_file():
            print("Reading data")
            data = pickle.load(open("db/UR_connected_users_db", "rb"))
            self.event_queue = data.get("events",list())
            self.users_db = data.get("users", dict())
        
        self.quit_button = tk.Button(self,
                         text="Exit", fg="red",
                         command= lambda: self.quit())
        self.quit_button.pack(side=tk.LEFT)
    
        self.login_button = tk.Button(self,
                         text="Login", fg="black",
                         command= lambda: self.login(self.uname_box.get(),self.pword_box.get()))
        self.login_button.pack(side=tk.LEFT)
        
        self.new_user_button = tk.Button(self,
                         text="Create user", fg="black",
                         command= lambda: self.create_user(self.uname_box.get(),self.pword_box.get()))
        self.new_user_button.pack(side=tk.LEFT)
    
        #self.bind("<Key>", self.key)
                
        self.uname_box = tk.Entry()
        self.uname_box.pack(side=tk.TOP)
        self.uname_box.insert(0, "username")
    
        self.pword_box = tk.Entry()
        self.pword_box.pack(side=tk.TOP)
        self.pword_box.insert(0, "password")
    
        self.text = Text()
        self.text.pack()
        self.text.delete('1.0', END)             # clear the widget's contents
        #self.text.insert(END, "astring")           # append astring to the widget's contents
        #somestring = t.get('1.0', END)
    
    def create_event(self):
        
        pass
        
    def get_event_by_name(self, name):
        pass
    
    def upvote_event(self, event_object):
        pass
    
    def login(self, username, password):
        hashstr = (str(username)+str((password)))
        try:
            if self.users_db[username] == hashstr:
                self.current_user_name = username
                self.text.delete('1.0', END)
                self.text.insert('1.0', "Login successful. %s" % str(username))
                self.current_user = User(str(username))
                self.pword_box.delete(0, tk.END)
                
                
            else:
                #self.text.delete('1.0', END)
                self.text.insert('1.0', "Invalid login credentials. Try again or create new user.\n")
        except:
            #self.text.delete('1.0', END)
            self.text.insert('1.0', "Invalid login credentials. Try again or create new user.\n")
        
    def logout(self):
        print("Logout successful. Exiting.")
        raise SystemExit
    
    def create_user(self, user_name = "Dummy user", user_pwd = "*****"):
        self.text.delete('1.0', END)
        self.text.insert('1.0', "Created new user: %s"%user_name)
        
        self.users_db[user_name] = (str(user_name)+str((user_pwd)))
        
        print(self.users_db)
        
        self.data_dump()
        
    def data_dump(self):
        data = dict()
        data["events"] = self.event_queue
        data["users"] = self.users_db
        with open("db/UR_connected_users_db", "wb") as f:
            pickle.dump(data, f)
        
if __name__ == '__main__':
    root = tk.Tk()
    #prompt = FacilitiesForum("")
    #prompt.prompt = 'UR Repaired! '
    FacilitiesForum(root).pack(side="top", fill="both", expand=True)
    try:
        root.mainloop()#'''
    #(C) Copyright 2018. Ting C., Hammad H., Yanish R., Aalok S.
    #This program comes with ABSOLUTELY NO WARRANTY.
    #This is free software, and you are welcome to redistribute it
    #under certain conditions. See the GNU LGPL 3 (The LESSER GPL).
    #''')
    except KeyboardInterrupt:
    	print("\nExiting due to KeyboardInterrupt")
    	raise SystemExit
