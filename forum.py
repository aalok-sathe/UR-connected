#! /bin/env/ python3

from request import Request

class FacilitiesForum(Cmd):
    
    def __init__(self):
        
        
    
        
        
if __name__ == '__main__':
    prompt = FacilitiesForum("")
    prompt.prompt = ':: '
    try:
    	prompt.cmdloop('''
    (C) 2018 Ting C., Hammad H., Yanish R., Aalok S.
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions. See the GNU LGPL 3 (The LESSER GPL).
    ''')
    except KeyboardInterrupt :
    	print("\nExiting due to KeyboardInterrupt")
    	raise SystemExit
