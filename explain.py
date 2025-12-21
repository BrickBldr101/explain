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
COMMANDS = {
    "ls": {
        "desc": "Lists the files and folders in the current directory",
        "flags": {
            "-l": "list in long format",
            "-a": "list hidden files as well",
            "-h": "show file sizes in human readable format",
            "-R": "list directories recursively",
        },
    },
    "pwd": {
        "desc": "Says what directory you are currently in",
        "flags": {
            "-L": "print the logical current directory",
            "-P": "print the physical directory without symlinks",
        },
    },
    "cd": {
        "desc": "Changes the current directory",
        "flags": {
            "-L": "follow symbolic links",
            "-P": "use the physical directory structure",
        },
    },
    "mkdir": {
        "desc": "Makes a directory in the current directory",
        "flags": {
            "-m": "set the permissions of the new directory",
            "-p": "create parent directories as needed",
            "-v": "print a message for each directory created",
            "-Z": "set the SELinux security context",
        },
    },
    "rmdir": {
        "desc": "Removes an empty directory",
        "flags": {
            "-p": "remove parent directories if they become empty",
            "-v": "output a message for each removed directory",
        },
    },
    "rm": {
        "desc": "Removes files or directories",
        "flags": {
            "-r": "remove directories recursively",
            "-f": "force removal",
            "-i": "prompt before removal",
            "-v": "explain what is being done",
        },
    },
    "cp": {
        "desc": "Copies files or directories",
        "flags": {
            "-r": "copy directories recursively",
            "-i": "prompt before overwrite",
            "-v": "explain what is being done",
            "-p": "preserve file attributes",
        },
    },
    "mv": {
        "desc": "Moves or renames files and directories",
        "flags": {
            "-i": "prompt before overwrite",
            "-v": "explain what is being done",
            "-n": "do not overwrite existing files",
        },
    },
    "touch": {
        "desc": "Creates an empty file or updates timestamps",
        "flags": {
            "-a": "change access time",
            "-m": "change modification time",
            "-t": "set a specific timestamp",
        },
    },
    "cat": {
        "desc": "Displays the contents of a file",
        "flags": {
            "-n": "number all lines",
            "-b": "number non-empty lines",
            "-s": "suppress repeated empty lines",
        },
    },
    "less": {
        "desc": "Views file contents one screen at a time",
        "flags": {
            "-N": "show line numbers",
            "-S": "disable line wrapping",
            "-F": "exit if content fits on screen",
        },
    },
    "head": {
        "desc": "Outputs the beginning of a file",
        "flags": {
            "-n": "number of lines",
            "-c": "number of bytes",
        },
    },
    "tail": {
        "desc": "Outputs the end of a file",
        "flags": {
            "-n": "number of lines",
            "-f": "follow file changes",
        },
    },
    "grep": {
        "desc": "Searches for text patterns in files",
        "flags": {
            "-i": "ignore case",
            "-r": "recursive search",
            "-n": "show line numbers",
            "-v": "invert match",
        },
    },
    "find": {
        "desc": "Searches for files and directories",
        "flags": {
            "-name": "search by name",
            "-type": "search by file type",
            "-size": "search by size",
            "-mtime": "search by modification time",
        },
    },
    "chmod": {
        "desc": "Changes file permissions",
        "flags": {
            "-R": "recursive",
            "-v": "verbose output",
        },
    },
    "chown": {
        "desc": "Changes file owner and group",
        "flags": {
            "-R": "recursive",
            "-v": "verbose output",
        },
    },
    "df": {
        "desc": "Shows disk space usage",
        "flags": {
            "-h": "human readable sizes",
            "-T": "show filesystem type",
        },
    },
    "du": {
        "desc": "Shows disk usage",
        "flags": {
            "-h": "human readable sizes",
            "-s": "summary only",
            "-a": "include files",
        },
    },
    "ps": {
        "desc": "Displays running processes",
        "flags": {
            "-e": "all processes",
            "-f": "full format",
            "-u": "user oriented",
        },
    },
    "kill": {
        "desc": "Sends a signal to a process",
        "flags": {
            "-9": "force kill",
            "-l": "list signals",
        },
    },
    "whoami": {
        "desc": "Shows the current user",
        "flags": {},
    },
    "id": {
        "desc": "Displays user and group IDs",
        "flags": {
            "-u": "user ID only",
            "-g": "group ID only",
            "-G": "all group IDs",
        },
    },
    "uname": {
        "desc": "Displays system information",
        "flags": {
            "-s": "kernel name",
            "-r": "kernel release",
            "-m": "machine type",
            "-a": "all system info",
        },
    },
    "date": {
        "desc": "Displays or sets the system date",
        "flags": {
            "-u": "use UTC",
            "-R": "RFC format",
            "+FORMAT": "custom output format",
        },
    },
    "echo": {
        "desc": "Prints text to the terminal",
        "flags": {
            "-n": "no trailing newline",
            "-e": "enable escape characters",
        },
    },
    "clear": {
        "desc": "Clears the terminal screen",
        "flags": {},
    },
    "history": {
        "desc": "Shows command history",
        "flags": {
            "-c": "clear history",
            "-d": "delete entry",
        },
    },
    "alias": {
        "desc": "Creates a command shortcut",
        "flags": {},
    },
    "unalias": {
        "desc": "Removes a command shortcut",
        "flags": {
            "-a": "remove all aliases",
        },
    },
    "top": {
        "desc": "Displays running processes in real time",
        "flags": {
            "-d": "refresh delay",
            "-p": "monitor process ID",
            "-u": "filter by user",
        },
    },
    "free": {
        "desc": "Displays memory usage",
        "flags": {
            "-h": "human readable",
            "-m": "megabytes",
            "-g": "gigabytes",
        },
    },
    "uptime": {
        "desc": "Shows system run time",
        "flags": {
            "-p": "pretty format",
            "-s": "start time",
        },
    },
    "ping": {
        "desc": "Checks network connectivity",
        "flags": {
            "-c": "count packets",
            "-i": "interval",
            "-t": "time to live",
        },
    },
    "curl": {
        "desc": "Transfers data from URLs",
        "flags": {
            "-O": "save to file",
            "-I": "headers only",
            "-L": "follow redirects",
        },
    },
    "wget": {
        "desc": "Downloads files",
        "flags": {
            "-O": "output file",
            "-c": "resume download",
            "-r": "recursive download",
        },
    },
    "tar": {
        "desc": "Creates or extracts archives",
        "flags": {
            "-c": "create archive",
            "-x": "extract archive",
            "-f": "archive file",
            "-v": "verbose",
        },
    },
    "zip": {
        "desc": "Creates zip archives",
        "flags": {
            "-r": "recursive",
            "-q": "quiet mode",
        },
    },
    "unzip": {
        "desc": "Extracts zip archives",
        "flags": {
            "-l": "list contents",
            "-o": "overwrite files",
        },
    },
    "mount": {
        "desc": "Mounts a filesystem",
        "flags": {
            "-t": "filesystem type",
            "-o": "mount options",
            "-r": "read only",
        },
    },
    "umount": {
        "desc": "Unmounts a filesystem",
        "flags": {
            "-f": "force",
            "-l": "lazy unmount",
        },
    },
    "lsblk": {
        "desc": "Lists block devices",
        "flags": {
            "-f": "filesystem info",
            "-a": "include empty devices",
        },
    },
    "shutdown": {
        "desc": "Shuts down or reboots the system",
        "flags": {
            "-r": "reboot",
            "-h": "halt",
            "-c": "cancel shutdown",
        },
    },
    "reboot": {
        "desc": "Restarts the system",
        "flags": {
            "-f": "force reboot",
        },
    },
    "poweroff": {
        "desc": "Powers off the system",
        "flags": {
            "-f": "force power off",
        },
    },
    "explain": {
        "desc": "Helps explain available commands, like this one",
        "flags": {
            "-c": "makes a cow do the explanation",
            "-l": "see the license for explain",
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