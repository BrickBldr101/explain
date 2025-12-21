#!/usr/bin

echo "In order to install explain you need to install the following dependencies: cowsay"
echo "In order to install explain you need to install the main script to /usr/local/bin"
echo "Continue? [y/n]"

read continue

if [ "$continue" = "y" ]; then
sudo apt update && sudo apt install cowsay -y
chmod +x explain.py
sudo mv explain.py /usr/local/bin/explain
else
echo "Abort."
fi

