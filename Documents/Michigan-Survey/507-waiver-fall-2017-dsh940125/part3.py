# these should be the only imports you need

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request

# write your code here
# usage should be python3 part3.py

def michigan_mostread():
	html = urlopen('http://www.michigandaily.com').read()
	soup = BeautifulSoup(html, "html.parser")

	content = soup.find(class_="panel-pane pane-mostread")
	if content.find(class_='item-list'): 
		for mostread in content.find(class_='item-list'):
			print (mostread.text.strip())
michigan_mostread()
