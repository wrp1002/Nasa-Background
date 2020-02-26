# -*- coding: utf-8 -*-
"""
NASA Background installer and uninstaller
"""

import psutil
import shutil
import os
import signal
import time
import sys

processName = "NASA Background.exe"
bootDrive = os.getenv("SystemDrive")
user = str(os.getlogin()).strip()
startupFolder = os.path.join(bootDrive, "/Users/", user, "AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/")

def Install():
	print("Checking current installation...")
	Uninstall()
	
	try:
		print("Startup folder location: '" + startupFolder + "'")
		
		if not os.path.exists(processName):
			print("'" + processName + "' not found")
			input("Press enter to exit...")
			quit()
		
		if not os.path.exists(startupFolder):
			print("Startup folder not found. Creating one...")
			os.mkdir(startupFolder)
		
		print("Copying '" + processName + "' to startup folder...")
		shutil.copy(processName, startupFolder)
		
		print("Starting process...")
		os.startfile(os.path.join(startupFolder, processName))
		
		print("Done!")

	except FileNotFoundError:
		print("Couldn't find '" + processName + "' in startup folder. Maybe try again?")
		input("Press enter to exit...")
		quit()
	except:
		print("Unexpected error:", sys.exc_info()[0])
		input("Press enter to exit...")
		quit()
	

def Uninstall():
	try:
		didAnything = False
		for proc in psutil.process_iter():
			try:
				if proc.name() == processName:
					time.sleep(1)
					proc.kill()
					print("'" + proc.name() + "' killed")
					didAnything = True
			except psutil.AccessDenied:
				pass
			except:
				print("Unexpeced error:", sys.exec_info()[0]);
		
		time.sleep(2)
		
		if os.path.exists(os.path.join(startupFolder, processName)):
			print("Removing '" + processName + "' from startup folder...")
			os.remove(os.path.join(startupFolder, processName))
			didAnything = True
		
		if didAnything:
			print("Done!")
		else:
			print("Nothing to uninstall")

	except:
		print("Unexpected error:", sys.exc_info()[0])
		input("Press enter to exit...")
		quit()



if __name__ == "__main__":
	ans = -1
	print("Would you like to install or uninstall NASA Background?")
	print("1. Install")
	print("2. Uninstall")
	while ans < 1 or ans > 2:
		try:
			ans = int(input(">"))
		except ValueError:
			print("Invalid input")
		
		
	if ans == 1:
		print("Installing...")
		Install()
	elif ans == 2:
		print("Uninstalling...")
		Uninstall()
		
	time.sleep(3)
	