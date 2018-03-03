#! /bin/env/ python3

from event import Event
import pickle
from cmd import Cmd
import tkinter as tk
from pathlib import Path


class FacilitiesForum(tk.Frame):
    
    request_queue = list()
    users_db = dict()
    current_user_name = None
    
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pack(fill=tk.BOTH)
        
        # Load users database if it exists
        if Path("UR_connected_users_db").is_file():
            self.users_db = pickle.load(open("UR_connected_users_db", "rb"))
        
        self.quit_button = tk.Button(self,
                         text="QUIT", fg="red",
                         command= lambda: self.quit()
                         )
        self.quit_button.pack(side=tk.LEFT)
        
    def login(self, username, password):
        hashstr = hash(str(username)+str(hash(password)))
        return users_db[username] == hashstr  
        
    def logout(self):
        print("Logout successful. Exiting.")
        raise SystemExit
    
    def create_user(self):
        user_name = "Dummy user"
        user_pwd = "*****"
        
        self.users_db[user_name] = hash(str(user_name)+str(hash(user_pwd)))
        
        pickle.dump(self.users_db, open("UR_connected_users_db", "wb"))
        
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
