#!/usr/bin/env python3

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
	
