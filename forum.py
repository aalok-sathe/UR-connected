#! /bin/env/ python3

from event import Event
import pickle
from cmd import Cmd
import tkinter as tk


class FacilitiesForum(tk.Frame):
    
    request_queue = []
    users_db = {}
    user_name = None
    
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pack(fill=tk.BOTH)
        
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
        pass
        
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
