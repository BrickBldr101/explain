# install script

import os
import sys

print("In order to install explain you need to: install the command to bin and install cowsay")
yn = input("Continue? [y/n]")

if yn == "y":
    pass
elif yn == "n":
    print("Abort")
    sys.exit(1)
else:
    print("Invalid. Abort")
    sys.exit(1)

os.system("sudo apt-get install cowsay")
os.system("chmod +x explain.py")
os.system("sudo mv explain.py /usr/local/bin/explain")

print("setup complete, explain installed successfully")