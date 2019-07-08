import time
import similar

'''
ONLY FOR TESTING
Always watch the response, and exit if Similarweb limit reached! Sometimes Similarweb's response can be slow.

If you want to acces to a parent folder, change:

import similar

To:

import importlib
similar = importlib.import_module("Similarweb-free-API.similar")
'''

while 1:
    print(similar.similarGet('http://google.com'))
    time.sleep(3)