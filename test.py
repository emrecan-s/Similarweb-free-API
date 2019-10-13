import time
import similar

from urllib.request import urlopen
with open('links.txt') as f:
    contents = f.read().splitlines()


'''
ONLY FOR TESTING
Always watch the response, and exit if Similarweb limit reached! Sometimes Similarweb's response can be slow.

If you want to acces to a parent folder, change:

import similar

To:

import importlib
similar = importlib.import_module("Similarweb-free-API.similar")
'''

for content in contents: 
	print(similar.similarGet(content))
	time.sleep(3)

  