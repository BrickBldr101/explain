# install script

import os
import sys

def pre_install():
    print("[pre-install] installing dependency: cowsay")
    os.system("sudo apt-get install cowsay")
    
def install():
    print("pre-install complete")
    print("[install] making command executable")
    os.system("chmod +x explain.py")
    print("[install] moving command to bin")
    os.system("sudo mv explain.py /usr/local/bin/explain")
    print("install complete")

def post_install():
    print("[post-install] Removing extra files")
    os.system("rm -rf ../explain")

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

pre_install()
install()
post_install()
print("\n\nthe current directory has been deleted, please exit after the installation is comeplete\n")
print("\nsetup complete, explain installed successfully")
