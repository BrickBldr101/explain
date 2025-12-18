#!/usr/bin/env python3

import sys

# this variable is for what the console prints
output = ""

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
}

# exit with an error (requires an error code
def exit_with_error(error_code):
    # if the command is not found
    if error_code == 1:
        print("Exited with error code 001: command not found")
        sys.exit(1)
        
    # if the flag is not found
    elif error_code == 2:
        print("Exited with error code 002: flag not found")
        sys.exit(1)

# main function
def main():
    global output
    
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
        
    print(output)

if __name__ == "__main__":
    main()