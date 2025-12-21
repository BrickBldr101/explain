#!/usr/bin/env python3

"""
github repository (SSH): git@github.com:BrickBldr101/explain.git
------------------------------------------------------------------
when editing code please write comments
------------------------------------------------------------------
the command in the terminal its just 'explain <args>'
------------------------------------------------------------------
to make the python script: (will delete python file so you will have to re-pull after

chmod +x explain.py
sudo mv explain.py /usr/local/bin/explain

------------------------------------------------------------------
to run the command from the python script (testing purposes only, make sure you are in the same directory)

python3 explain.py <args>
------------------------------------------------------------------
yes, it is usable with cowsay

explain <args> | cowsay
"""

# man but for beginners basically

import sys
import os
import json

# this variable is for what the console prints
output = ""

cowsay_activated = False

flagstart = 2

version = 0.2

LICENSE = """
MIT License

Copyright (c) 2025 Noah McCracken

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

ERROR_CODES = {
    "-1":{
        "id": "-1",
        "desc": "unexpected error occured",
    },
    "1": {
        "id": "001",
        "desc": "command not found",
    },
    "2": {
        "id": "002",
        "desc": "flag not found",
    },
}

# for all of the commands, descriptions and flags
with open('/usr/local/share/explain/commands.json', 'r') as commands:
    COMMANDS = json.load(commands)


# exit with an error (requires an error code
def exit_with_error(error_code):
    if str(error_code) in ERROR_CODES:
        print(f"Error code {ERROR_CODES[str(error_code)]['id']}: {ERROR_CODES[str(error_code)]['desc']}")
        sys.exit(error_code)
    else:
        error_code = -1
        print(f"Error code {ERROR_CODES[str(error_code)]['id']}: {ERROR_CODES[str(error_code)]['desc']}")
        sys.exit(error_code)
        
    

# main function
def main():
    global output, cowsay_activated, flagstart
    
    # if the command is called without any arguments
    if len(sys.argv) == 1:
        print("usage: explain <command> <flags>")
        print("\n\nWelcome to explain! \nNote: this command is still in development is is very new")
        print("Another note: explain only has flags as extra arguments as of now")
        sys.exit(1)
    
    # this is pretty obvious, but sys.argv is the command called (sys.argv[0] would be the actual explain command)
    command = sys.argv[1]
    
    #explain help
    if command == "-h" or command == "--help":
        print("Usage: <command> <flags>")
        print("NOTE: As of now explain supports few commands and the only arguments it supports are flags")
        print("NOTE: Flags such as '--help', '-h', '--version' among others will not be included")
        sys.exit(1)
        
    elif command == "-v" or command == "--version":
        print(f"Explain version {str(version)} currently installed.")
        sys.exit(1)
        
    elif command == "-c" or command == "--cowsay":
        command = sys.argv[2]
        flagstart = 3
        cowsay_activated = True
        
    elif command == "--PRINT_ALL_COMMANDS":
        print(COMMANDS)
        sys.exit(1)
        
    elif command == "-l" or command == "--LICENSE":
        print(LICENSE)
        sys.exit(1)
        
    # actually get the command
    if command in COMMANDS:
        output = output + f"{command}: {COMMANDS[command]['desc']}"
            
        #flags if there are any
        if len(sys.argv) > flagstart:
            for flag in sys.argv[flagstart:]:
                try:
                        
                    output = output + f"\n{flag}: {COMMANDS[command]['flags'][flag]}"
                        
                except KeyError:
                    exit_with_error(2)
                    
        
    else:
        exit_with_error(1)
    
    if cowsay_activated == False:
        print(output)
    elif cowsay_activated == True:
        os.system(f"cowsay '{output}'")

if __name__ == "__main__":
    main()