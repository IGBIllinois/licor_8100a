#!/usr/bin/env python

import sys
import os.path
from optparse import OptionParser


root_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(root_dir + "/lib")
from li8100a import li8100a
settings = {}
settings['port'] = "1526"
settings['ipaddress'] = ""
settings['utc'] = True


def main():

	usage = "Sets Date on Licor LI-8100A devices."
	parser = OptionParser(usage)

	parser.add_option("-i","--ipaddress",action='store', type="string",
		help="IP Address");
	parser.add_option("-p","--port",action='store',type="int",help="TCP/IP Port (default:" + settings['port'] + ")");
	(options,args) = parser.parse_args()
	if len(sys.argv) == 1:
		parser.print_help()
		quit(1)

	if (options.ipaddress == None):
		parser.error("Please specify a host with -h/--host")
		quit(1)
	else:
		settings['ipaddress'] = options.ipaddress
	if (options.port != None):
		settings['port'] = options.port


	print ("IPAddress: " + settings['ipaddress'])
	print ("Port: " + str(settings['port']))
	
	licor = li8100a(settings['ipaddress'],settings['port'])
	

if __name__ == '__main__':
	main()
