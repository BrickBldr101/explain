# install script

import os
import sys

print("In order to install explain you need to: install the command to bin and install cowsay")
con = input("Continue? [y/n] ").lower()

print("\nAfter installation the explain folder will be deleted")
delete = input("Continue? [y/n] ").lower()

if con == "y":
    pass
elif con == "n":
    print("Abort")
    sys.exit(1)
else:
    print("Invalid. Abort")
    sys.exit(1)
    
if delete == "y":
    pass
elif delete == "n":
    print("Abort")
    sys.exit(1)
else:
    print("Invalid. Abort")
    sys.exit(1)

os.system("sudo apt-get install cowsay")
os.system("chmod +x explain.py")
os.system("sudo mv explain.py /usr/local/bin/explain")

os.system("rm -rf ../explain")
print("setup complete, explain installed successfully")