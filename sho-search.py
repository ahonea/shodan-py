#!/bin/python
# Author: Panderz
# Shodanhq search script

from shodan import WebAPI
import sys

SHODAN_API_KEY = ""

api = WebAPI(SHODAN_API_KEY)
userdef = raw_input ("What do you want to look for: ") 
print ("Be carefull what you search for...")

class fileout(object):
        def __init__(self, filename="search.txt"):
            self.terminal = sys.stdout
            self.log = open(filename, "a")

        def write(self, message):
            self.terminal.write(message)
            self.log.write(message)

sys.stdout = fileout("shosearch.txt")


try:
		results = api.search(userdef)
		
		print 'Results found: %s' % results['total']
		for result in results['matches']:
				print 'IP: %s' % result['ip']
				print result['data']
				print ''
except Exception, e:
		print 'Error: %s' % e
		
		
