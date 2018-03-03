#! /bin/env/ python3

#from request import Request
import pickle
from cmd import Cmd
import tkinter as tk


class FacilitiesForum(tk.Frame):
    
    request_queue = []
    
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        self.pack()
        
        self.button = tk.Button(self,
                         text="QUIT", fg="red",
                         command=self.quit)
        self.button.pack(side=tk.LEFT)
        
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
