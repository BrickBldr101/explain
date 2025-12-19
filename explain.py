#!/usr/bin/env python3

"""
github repository: git@github.com:BrickBldr101/explain.git
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

import sys

# this variable is for what the console prints
output = ""

cowsay_activated = False

version = 0.01

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
COMMANDS = {
    "ls": {
        "desc": "Lists the files and folders in the current directory",
        "flags": {
            "-l": "list in long format",
            "-a": "list hidden files aswell",
        },
    },
    "pwd": {
        "desc": "Says what directory you are currently in",
        "flags": {
            "-L": "list in long format",
            "-a": "list hidden files aswell",
        },
    },
    "mkdir":{
        "desc": "Makes a directory in the current directory",
        "flags": {
            "-m": "Sets the permissions of the new directory",
            "-p": "Create parent directories as needed to avoid errors",
            "-v": "Print a message for each directory created",
            "-Z": "Set the SELinux security context for the directory",
        },
    },
    "explain": {
        "desc": "Helps explain available commands, like this one",
        "flags": {
        },
    },
}

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
    global output, cowsay_activated
    
    # if the command is called without any arguments
    if len(sys.argv) == 1:
        print("usage: explain <command> <flag>")
        sys.exit(1)
    
    # this is pretty obvious, but sys.argv is the command called (sys.argv[0] would be the actual explain command)
    command = sys.argv[1]
    
    #explain help
    if command == "-h" or command == "--help":
        print("NOTE: Flags such as '--help', '-h', '--version' among others will not be included")
        sys.exit(1)
        
    elif command == "-v" or command == "--version":
        print(f"Explain version {str(version)} currently installed.")
        sys.exit(1)
        
    elif command == "-c" or command == "--cowsay":
        command = sys.argv[2]
        cowsay_activated = True

    # actually get the command
    if command in COMMANDS:
        output = output + f"{command}: {COMMANDS[command]['desc']}\n"
        
        # flags if there are any
        if len(sys.argv) > 2:
            for flag in sys.argv[2:]:
                try:
                    
                    output = output + f"{flag}: {COMMANDS[command]['flags'][flag]}\n"
                    
                except KeyError:
                    exit_with_error(2)
                    
        
    else:
        exit_with_error(1)
    
    if cowsay_activated == False:
        print(output)
    elif cowsay_activated == True:
        print (output + " | cowsay")

if __name__ == "__main__":
    main()