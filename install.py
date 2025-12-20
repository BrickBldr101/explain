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

print("[pre-install] installing dependency: cowsay")
os.system("sudo apt-get install cowsay")
print("pre-install complete")
print("[install] making command executable")
os.system("chmod +x explain.py")
print("[install] moving command to bin")
os.system("sudo mv explain.py /usr/local/bin/explain")
print("install complete")

print("[post-install] Removing extra files")
os.system("rm -rf ../explain")
print("[post-install] changing directory")
os.system("cd ..")
print("\nsetup complete, explain installed successfully")
