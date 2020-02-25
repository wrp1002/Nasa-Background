# -*- coding: utf-8 -*-
"""
Spyder Editor

Automatic NASA background image program
icon from https://icon-icons.com/icon/satelite-space/86323
"""

from bs4 import BeautifulSoup as bs
import requests
import os
import tempfile
import ctypes
from datetime import datetime
import time
import re

tempDir = tempfile.gettempdir() + "\\"
fullUrl = "https://apod.nasa.gov/apod/astropix.html"
url = fullUrl[:fullUrl.rfind("/") + 1]

print(tempDir)
print(os.getcwd())

def UpdateBackground(pageUrl):
	print("Updating background...")
	backButtonUrl = pageUrl
	
	try:
		response = requests.get(pageUrl)
		soup = bs(response.text, "html.parser")
		
		#print(response.text)
		backButtonUrl = soup.find("a", string="<")["href"]
		print("backButton:", backButtonUrl)
		
		img = soup.find("img")
		a = img.find_parent("a")
		imgUrl = url + a["href"]
		
		print("Image URL:", imgUrl)
		
		response = requests.get(imgUrl)
		if response.status_code == 200:
			with open(tempDir + "background.jpg", 'wb') as f:
				f.write(response.content)
				
		#ctypes.windll.user32.SystemParametersInfoW(20, 0, tempDir + "background.jpg", 3)
		
	except AttributeError:
		print("No new image found today")
		print("Going to", backButtonUrl)
		UpdateBackground(url + backButtonUrl)
	except:
		print("Error getting image")
	


if __name__=="__main__":
	UpdateBackground(fullUrl)	# Check for new images on startup

	while False:	
		print("Waiting an hour...")
		while datetime.now().hour != 4:
			time.sleep(3600)
		
		UpdateBackground()
		
		
		
		
		
		
		
		
		
		
		
		