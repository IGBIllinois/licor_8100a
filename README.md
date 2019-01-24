# Licor LI-9100A Scripts
- Various scripts to help download data and set the time on LI-9100A Devices

## Requirements
* Python 2.7 or Greater
* lftp (https://lftp.yar.ru/)

## Scripts
* bin/set_time.py - Sets the time 
** Usage
Usage: Sets Date on Licor LI-8100A devices.

Options:
  -h, --help            show this help message and exit
  -i IPADDRESS, --ipaddress=IPADDRESS
                        IP Address
  -p PORT, --port=PORT  TCP/IP Port
  --utc                 Set Time to UTC
  --local               Set Time to Local Time
```
* Specify an IP Address, port number (default 1526), UTC or Local time

