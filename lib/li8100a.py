import sys
import datetime
import socket
from crc32 import *

class li8100a:


	ipaddress = None
	port = 1524
	buffer_size = 4096
	connection = None

	def __init__(self,ipaddress,port):
		self.ipaddress = ipaddress
		self.port = int(port)
		self.connect()

	def connect(self):
		try:
			self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			self.connection.connect((self.ipaddress,self.port))
			return True
		except:
			return False

	def close(self):
		try:
			self.connection.close()
			return True
		except:
			return False


	def send_data(self,in_data):
		print ('Send Data: ' + in_data)
		data_length = len(in_data);
		send_length = self.connection.send(in_data.encode())
		if (data_length != send_length):
			print ("Error sending data. Size sent does not match")
			return False

		received_data = self.connection.recv(self.buffer_size).decode('utf-8')
		print ("Received Data: " + received_data)
		received_crc = self._strip_crc(received_data)
		calc_crc = self._calc_crc(received_data)
		print('Received CRC: ' + str(received_crc))
		print('Calc CRC: ' + str(calc_crc))
		if (received_crc != calc_crc):
			print('CRC do not match!')
			return False
		else:
			print('CRC match')
		return received_data

	def set_date(self,utc):
		if (utc):
        	        current_time = datetime.datetime.utcnow().strftime("%H%M")
                	current_date = datetime.datetime.utcnow().strftime("%Y%m%d")
		else:
	                current_time = datetime.datetime.now().strftime("%H%M")
        	        current_date = datetime.datetime.now().strftime("%Y%m%d")
		xml = "<SR><CFG><CLOCK><TIME>" + current_time + "</TIME><DATE>" + current_date + "</DATE></CLOCK></CFG></SR>\r\n";
		return_data = self.send_data(xml)
		

	def enable_crc(self):
		xml = "<SR><IP><ENABLECRC>TRUE</ENABLECRC></IP></SR>\r\n"
		self.send_data(xml)
		
	def enable_transfer_mode(self):
		xml = "<SR><CMD><TRANSFER>START</TRANSFER></CMD></SR>\r\n"
		self.send_data(xml)

	def transfer_measurement(self,measurement):
		xml = "<SR><TRANSFER><NAME>" + measurement + "</TRANSFER></SR>\r\n"
		received_data = self.send_data(xml)




############Private Functions#################

	def _strip_crc(self,xml):
		crc_start = xml.find('<CRC>')
		crc_end = xml.find('</CRC>')
		crc_xml = xml[crc_start+5:crc_end]
		return int(crc_xml)
	
	def _calc_crc(self,xml):
		crc_start = xml.find('<CRC>')
		data_xml = xml[0:crc_start]
		print('data xml: ' + data_xml)
		print('length: ' + str(len(data_xml)))
		return memcrc(data_xml)		

