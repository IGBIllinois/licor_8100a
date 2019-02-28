import sys
import datetime
import socket
from xml.dom import minidom


class li8100a:


	def __init__(self,ipaddress,port):
		self.ipaddress = ipaddress
		self.port = int(port)
		self.buffer_size = 2048

	def send_data(self,in_data):
		data_length = len(in_data);
		a = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		#try:
		a.connect((self.ipaddress,self.port))
		send_length = a.send(in_data.encode())
		if (data_length != send_length):
			print ("Error sending data. Size sent does not match")
			return False

		received_data = a.recv(self.buffer_size).decode('utf-8')
		print ("Received Data: " + received_data)
		a.close()
		#except:
		print ("ERROR: Failed connecting to " + self.ipaddress + " on port " + str(self.port))
#		return False


		return received_data

	def set_date(self,utc):
		if (utc):
        	        current_time = datetime.datetime.utcnow().strftime("%H%M")
                	current_date = datetime.datetime.utcnow().strftime("%Y%m%d")
	        else:
	                current_time = datetime.datetime.now().strftime("%H%M")
        	        current_date = datetime.datetime.now().strftime("%Y%m%d")
		date_xml = "<SR><CFG><CLOCK><TIME>" + current_time + "</TIME><DATE>" + current_date + "</DATE></CLOCK></CFG></SR>";
		return_data = self.send_data(date_xml)
