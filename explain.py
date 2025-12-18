import sys

output = ""

COMMANDS = {
    "ls": {
        "desc": "Lists the files and folders in the current directory",
        "flags": {
            "-l": "list in long format",
            "-a": "list hidden files aswell",
        },
    },
    "pwd": {
        "desc": "Lists the files and folders in the current directory",
        "flags": {
            "-l": "list in long format",
            "-a": "list hidden files aswell",
        },
    },
}

def exit_with_error(error_code):
    if error_code == 1:
        print("Exited with error code 001: command not found")
        sys.exit(1)
        
    elif error_code == 2:
        print("Exited with error code 002: flag not found")
        sys.exit(1)

def main():
    global output
    
    
    if len(sys.argv) == 1:
        print("usage: explain <command> <flag>")
        sys.exit(1)
        
    command = sys.argv[1]
    
    if command == "-h" or command == "--help":
        print("Note: if a flag makes a command behave the same as if without the flag , the flag will not be listed")
        sys.exit(1)

    if command in COMMANDS:
        #print(f"{command}: {COMMANDS[command]['desc']}")
        output = output + f"{command}: {COMMANDS[command]['desc']}\n"
        if len(sys.argv) > 2:
            for flag in sys.argv[2:]:
                try:
                    #print(f"{flag}: {COMMANDS[command]['flags'][flag]}")
                    
                    output = output + f"{flag}: {COMMANDS[command]['flags'][flag]}\n"
                    
                except KeyError:
                    exit_with_error(2)
                    
        
    else:
        exit_with_error(1)
        
    print(output)

if __name__ == "__main__":
    main()