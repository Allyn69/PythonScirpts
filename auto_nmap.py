#!/usr/bin/env python3
"""
Creator: Avery Kleeman
This script will automate nmap scans with the help of Python3 nmap. You must have nmap3 installed on your computer for python 3
Simply run the script with with an IP next the the command you wish to scan.
Eventually the ability to scan more hosts will be implenmented into the script.

Example Data Collection:

{'127.0.0.1': [
{'host': '127.0.0.1', 'protocol': 'tcp', 'portid': '21', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '0', 'service': {'name': 'ftp', 'method': 'table', 'conf': '3'}}, 
{'host': '127.0.0.1', 'protocol': 'tcp', 'portid': '22', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '0', 'service': {'name': 'ssh', 'method': 'table', 'conf': '3'}}, 
{'host': '127.0.0.1', 'protocol': 'tcp', 'portid': '23', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '0', 'service': {'name': 'telnet', 'method': 'table', 'conf': '3'}}, 
{'host': '127.0.0.1', 'protocol': 'tcp', 'portid': '80', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '0', 'service': {'name': 'http', 'method': 'table', 'conf': '3'}}, 
{'host': '127.0.0.1', 'protocol': 'tcp', 'portid': '111', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '0', 'service': {'name': 'rpcbind', 'method': 'table', 'conf': '3'}}, 
{'host': '127.0.0.1', 'protocol': 'tcp', 'portid': '139', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '0', 'service': {'name': 'netbios-ssn', 'method': 'table', 'conf': '3'}}, 
{'host': '127.0.0.1', 'protocol': 'tcp', 'portid': '445', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '0', 'service': {'name': 'microsoft-ds', 'method': 'table', 'conf': '3'}}, 
{'host': '127.0.0.1', 'protocol': 'tcp', 'portid': '3389', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '0', 'service': {'name': 'ms-wbt-server', 'method': 'table', 'conf': '3'}}, 
{'host': '127.0.0.1', 'protocol': 'tcp', 'portid': '5901', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '0', 'service': {'name': 'vnc-1', 'method': 'table', 'conf': '3'}}, 
{'host': '127.0.0.1', 'protocol': 'tcp', 'portid': '12345', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '0', 'service': {'name': 'netbus', 'method': 'table', 'conf': '3'}}]

"""
import os
import sys
import nmap3

"""
Script Tests
"""
if os.getenv("SUDO_USER") is None:
	exit("{} must be ran as root!".format(sys.argv[0]))

if len(sys.argv) < 2
	exit("Syntax for auto-nmap is sudo {} <IP Address>".format(sys.argv[0]))
	
"""
Script Arguments
"""
ip = sys.argv[1]

"""
Nmap Scans set up
"""
nmap = nmap3.Nmap()
ports = nmap.scan_top_ports(ip, default="65535")

"""
Variables
"""
host = ports.keys()[1]

"""
Output
"""
print("""---------------
{}
-----------------
Proto/Port:        Service:""".format(host))
for x in range(0,len(ports[ip])):
	port = ports[ip][x][portid]
	protocol = ports[ip][x][protocol]
	service = ports[ip][x]['service']['name']
	print("""{}/{}        {}""".format(protocol,port,service))
	
