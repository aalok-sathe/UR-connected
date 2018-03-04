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
    listbox = None
    
    def __init__(self, parent, *args, **kwargs):
        #'''
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.grid()#fill=tk.BOTH)
        #'''
        # Load users database if it exists
        if Path("db/UR_connected_users_db").is_file():
            print("Reading data")
            data = pickle.load(open("db/UR_connected_users_db", "rb"))
            self.event_queue = data.get("events",list())
            self.users_db = data.get("users", dict())
        
        self.quit_button = tk.Button(self,
                         text="Exit", fg="red",
                         command= lambda: self.quit())
        self.quit_button.grid(row=0, column=0)#side=tk.LEFT)
    
        self.login_button = tk.Button(self,
                         text="Login", fg="black",
                         command= lambda: self.login(self.uname_box.get(),self.pword_box.get()))
        self.login_button.grid(row=0, column=1)#side=tk.LEFT)
        
        self.new_user_button = tk.Button(self,
                         text="Create user", fg="black",
                         command= lambda: self.create_user(self.uname_box.get(),self.pword_box.get()))
        self.new_user_button.grid(row=0, column=2)#(side=tk.LEFT)
    
        #self.bind("<Key>", self.key)
                
        self.uname_box = tk.Entry()
        self.uname_box.grid(row=1,column=0)
        self.uname_box.insert(0, "username")
        self.uname_box.bind("<Button-1>", lambda super: self.uname_box.delete(0, tk.END))
    
        self.pword_box = tk.Entry()
        self.pword_box.grid(row=2,column=0)
        self.pword_box.insert(0, "password")
        self.pword_box.bind("<Button-1>", lambda super: self.pword_box.delete(0, tk.END))
    
        self.text = Text()
        self.text.grid(row=3,column=0)
        self.text.delete('1.0', END)             # clear the widget's contents
        
        
    def create_event(self):#, title, body, location, keywords):
        #self.event_queue.append(Event(len(event_queue), title, body, location, current_user, keywords_dict))
        
        self.title_box = tk.Entry()
        self.title_box.grid(row=3,column=0)
        self.title_box.insert(0, "title")
        self.title_box.bind("<Button-1>", lambda super: self.title_box.delete(0, tk.END))
        
        self.body_box = tk.Entry()
        self.body_box.grid(row=3,column=1)
        self.body_box.insert(0, "body")
        self.body_box.bind("<Button-1>", lambda super: self.body_box.delete(0, tk.END))
        
        self.location_box = tk.Entry()
        self.location_box.grid(row=3,column=2)
        self.location_box.insert(0, "location")
        self.location_box.bind("<Button-1>", lambda super: self.location_box.delete(0, tk.END))
        
        self.keyword_box = tk.Entry()
        self.keyword_box.grid(row=3,column=3)
        self.keyword_box.insert(0, "comma separated keywords")
        self.keyword_box.bind("<Button-1>", lambda super: self.keyword_box.delete(0, tk.END))
        
        self.submit_event = tk.Button(self,
                         text="Submit event", fg="green",
                         command= lambda: self.submit_event_data())
        self.submit_event.grid(row=4, column=0)
        
    def submit_event_data(self):
        
        #print("!!!!!!!!!!!!!!!!!!!!!\n",len(self.event_queue), self.title_box.get(), self.body_box.get(), self.location_box.get(), self.current_user, self.keyword_box.get().split(','))
        
        e = list((len(self.event_queue), self.title_box.get(), self.body_box.get(), self.location_box.get(), self.current_user,  self.keyword_box.get().split(',')))
        
        self.event_queue.append(e)
        self.submit_event.destroy()
        
        self.title_box.destroy()
        self.body_box.destroy()
        self.location_box.destroy()
        self.keyword_box.destroy()
        
        self.update_list()
        
    #def get_event_by_name(self, name):
    #    pass
    
    def upvote_event(self, event_object, user):
        event_object.thumb_up(user)
        self.update_list()
    
    def login(self, username, password):
        #hashstr = (str(username)+str((password)))
        try:
            print(self.users_db)
            if False or self.users_db[username] == password:
                self.current_user_name = username
                self.text.delete('1.0', END)
                self.text.insert('1.0', "Login successful. %s" % str(username))
                
                self.current_user = User(str(username))
                
                self.pword_box.destroy()
                self.uname_box.destroy()
                self.login_button.destroy()
                self.new_user_button.destroy()
                self.text.destroy()
                
                #self.pword_box = tk.Button(self,
                #         text="Logout", fg="red",
                #         command= lambda: self.logout()).grid(row=0, column=3)
                
                #self.grid()
                self.listbox = tk.Listbox(width=150)
                self.listbox.bind("<Double-Button-1>", self.OnDouble)
                self.show_forum()
                
                
            else:
                self.text.delete('1.0', END)
                self.text.insert('1.0', "Invalid login credentials. Try again or create new user.\n")
        except:
            self.text.delete('1.0', END)
            self.text.insert('1.0', "Invalid login credentials. Try again or create new user.\n")
    
    def OnDouble(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        
        print ("!!!!!!!!!!!!!!!!!!\n", value)
    
        self.upvote_button = tk.Button(self,
                         text="Upvote?", fg="blue",
                         command= lambda: self.upvote_event(value, self.current_user))
        self.upvote_button.grid(row=6, column=0)#side=tk.LEFT)
    
    def show_forum(self):
        
        self.create_button = tk.Button(self,
                         text="Create event", fg="black",
                         command= lambda: self.create_event()).grid(row=2, column=0)#side=tk.BOTTOM)
        
        
        self.listbox.grid(row=5,column=5)
        self.update_list(self)
        
        
        
        #self.forum = Frame(self.parent)
        #self.forum.pack(fill=tk.BOTH)
      
    def update_list(self):
        self.listbox.delete(0,tk.END)
        for item in self.event_queue:
            self.listbox.insert(tk.END, item)#self.event_queue[-1])
        self.listbox.grid(row=5,column=5)
        
    def logout(self):
        print("Logout successful. Exiting.")
        raise SystemExit
    
    def create_user(self, user_name = "Dummy user", user_pwd = "*****"):
        self.text.delete('1.0', END)
        self.text.insert('1.0', "Created new user: %s"%user_name)
        
        self.users_db[user_name] = user_pwd
        
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
    FacilitiesForum(root).grid()#side="top", fill="both", expand=True)
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
