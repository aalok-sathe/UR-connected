#! /bin/env/ python3

from request import Request
import pickle
from tkinter import *

class FacilitiesForum(Cmd):
    
    request_queue = []
     
    def __init__(self):
            
               
        
if __name__ == '__main__':
    prompt = FacilitiesForum("")
    prompt.prompt = 'UR Repaired! '
    try:
    	prompt.cmdloop('''
    (C) Copyright 2018. Ting C., Hammad H., Yanish R., Aalok S.
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions. See the GNU LGPL 3 (The LESSER GPL).
    ''')
    except KeyboardInterrupt:
    	print("\nExiting due to KeyboardInterrupt")
    	raise SystemExit
