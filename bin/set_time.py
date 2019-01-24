#!/usr/bin/env python

import sys
import datetime
import socket
from optparse import OptionParser


settings = {}
settings['port'] = "1526"
settings['ipaddress'] = ""
settings['utc'] = True
buffer_size = 1024

def send_data(ipaddress,port,in_data):
        a = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
        	a.connect((ipaddress,port))
	        a.send(in_data)
        	received_data = a.recv(buffer_size)
	        a.close()
		return received_data
	except:
		print "ERROR: Failed connecting to " + ipaddress + " on port " + port
		return false

def main():

	usage = "Sets Date on Licor LI-8100A devices."
	parser = OptionParser(usage)

	parser.add_option("-i","--ipaddress",action='store', type="string",
		help="IP Address");
	parser.add_option("-p","--port",action='store',type="int",help="TCP/IP Port");
	parser.add_option("--utc",action='store_true',help="Set Time to UTC");
	parser.add_option("--local",action='store_true',help="Set Time to Local Time");
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
		settings['port'] = str(options.port)

	if (options.utc and not options.local):
		settings['utc'] = True
	elif (not options.utc and options.local):
		settings['utc'] = False
	elif (options.utc and options.local):
		parser.error("Specify --utc or --local")
		quit(1)

	print 'IPAddress: ' + settings['ipaddress']
	print 'Port: ' + settings['port']
	print 'UTC: ' + str(settings['utc'])

	if (settings['utc']):
	        current_time = datetime.datetime.utcnow().strftime("%H%M")
	        current_date = datetime.datetime.utcnow().strftime("%Y%m%d")
	else:
		current_time = datetime.datetime.now().strftime("%H%M")
		current_date = datetime.datetime.now().strftime("%Y%m%d")

	date_xml = "<CLOCK><TIME>" + current_time + "</TIME><DATE>" + current_date + "</DATE></CLOCK>";
	print "Date XML: " + date_xml
	data = send_data(settings['ipaddress'],int(settings['port']),date_xml)
	print "Received Data: " + data
if __name__ == '__main__':
	main()
