#!/usr/bin/env python
#Author: Slime
#Website: https://skumsoft.ltd/slimenet/
#dependencies: xclip, xsel, tk, python, imgmagik, curl, python-argparse
import subprocess
import os
from sys import exit


try:
	os.system("yay -S xclip xsel tk imagemagick curl python-argparse")
except:
	print("ERROR INSTALLING DEPENDENCIES")
	print("Please install xclip, xsel, tk, python, imgmagik, and curl.  Also try running this script as sudo")
	input()
	exit()

print("=========")
try:

	os.system("sudo cp -v skumup /usr/bin")
	os.system("sudo cp -v slimeshot /usr/bin")
except :
	print("Try running this script as sudo")
	input()
	exit()

print("=========")
print("SUCCESS, you can now run SlimeShot with the command 'slimeshot'")
input()