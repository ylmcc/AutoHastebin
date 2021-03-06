#!/usr/bin/env python3
import requests
import sys

def upload(text,url):
	r = requests.post(url+'/documents',text)
	r = r.json()
	print("Your url is: {}".format(url+'/'+ r['key']))
	

def check():
	try:
		with open(sys.argv[1], 'r') as file:
			text = file.read()
			url = 'https://paste.redbrick.dcu.ie'  # This can be changed to any hastebin hosted site.
			upload(text,url)
	
	except IndexError:
			print('Syntax: haste <file>')

	except FileNotFoundError:
			sys.argv[1] = input("File not found.\nEnter filename: ")
			check()

	

if __name__ == '__main__':
	check()
