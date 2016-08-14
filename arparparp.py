#!/usr/bin/env python
import sys
from scapy.all import *

#define packet type value
UDP = 2048

def process(input_file):
    try:
	with open(input_file, 'r') as f:
            try:
		flag = ""
                pkts = rdpcap(input_file)
		for p in pkts:
		    if p.type == UDP and p.src == '54:be:f7:51:9b:05':
			flag += p.load
		return flag
	    except Exception as e:
	        print "[!] {}.".format(e)
    except:
	print "[!] Error opening file"

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print "{}".format(process(sys.argv[1]))
    else:
	print "[!] Usage: {} <pcap>".format(__file__)
