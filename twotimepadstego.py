#!/usr/bin/env python
import binascii
import os,sys

V5_HEADER_LEN = 138 

def xor(image1, image2, outfile):
    try:
        with open(image1, 'rb') as f:
	    #read and store hex string of bytes
	    _s1 = binascii.hexlify(f.read())
	    #create a list of bytes
	    bl1 = ':0x'.join((_s1)[i:i+2] for i in range(0, len(_s1), 2)).split(":")
	    #correct missing '0x'
	    bl1[0] = '0x42'
    except Exception as e:
	print "[!] {}".format(e)

    try:
	with open(image2, 'rb') as f:
	    #read and store hex string of bytes
	    _s2 = binascii.hexlify(f.read())
	    #create a list of bytes
	    bl2 = ':0x'.join((_s2)[i:i+2] for i in range(0, len(_s2), 2)).split(":")
	    #correct missing '0x'
	    bl2[0] = '0x42'
    except Exception as e:
	print "[!] {}".format(e)

    try:
	with open(outfile, 'wb') as f:
	    for i in range(0, len(bl1), 1):
		if i > V5_HEADER_LEN:
		    try:
			byte = hex(int(bl1[i], 16) ^ int(bl2[i], 16)).split('0x')[1]
			#add padding if length is odd
			if len(byte) % 2 != 0: byte = ''.join(('0', byte))
			f.write(binascii.unhexlify(byte))
                    except Exception as we:
                        print "{}".format(we)
                        break
                else:
		    #write binary data of hex value
                    f.write(binascii.unhexlify(bl1[i].split('0x')[1]))
    except Exception as e:
	print "[!] {}".format(e)

if __name__ == "__main__":
    print "[-] Removing old files (if exist)..."
    if os.path.isfile('out.bmp'): os.remove('out.bmp')

    print "[-] XOR'ing 2 encrypted images..."
    xor('enc1.bmp', 'enc2.bmp', 'out.bmp')
