#!/usr/bin/env python
import os
import shutil
import sys

from subprocess import call

def main():
    if os.path.isdir("xortool_out") and os.path.isfile("decoded_message"):
	print "[-] Deleting old files...\n"
	shutil.rmtree("xortool_out/")
	os.remove("decoded_message")

    try:
        print "[-] Creating new un-hex'd \"message\" file for xortool...\n"
        with open('message', 'r') as f:
	    with open('decoded_message', 'w') as nf:
	        nf.write(f.read().strip().decode('hex'))
    except Exception as fe:
	print "[!] {}".format(fe)

    try:
	print "[-] Running xortool frequency analysis...\n"
	# [space] is the most common character in a sentenance
	call(["xortool", "-c 20", "decoded_message"])
	print ""
    except Exception:
	print "[!] Error: xortool might not be installed. Use pip to install."

    key = '\x42\xc2\x92\x65\xc3\xb4\x6e\xc2\x9d\xc3\xb9'
    print "[-] Decoding... Using key length = 11\n"
    ciphertext = open('message', 'r').read().strip().decode('hex')
    print "".join(chr(ord(c) ^ ord(key[i % 11])) for i,c in enumerate(ciphertext))

    # xxd message
    #\x0b\xb6\xb5\x16\xe3\xd5\x0d\xb6\xe8\xa2\xd5\x2e\xb\xb2\x0e\xaa

    # using an ascii<->hex chart we can manipulate the numbers to get
    #\x49\x74\x27\x73\x20\x61\x63\x74\x75\x61\x6c\x6c\x79\x20\x6b\x69\x6e\x64

    # new key
    #\x42\xc2\x92\x65\xc3\xb4\x6e\xc2\x9d\xc3\xb9


if __name__ == "__main__":
    #message = "0bb6b516e3d50db6e8a2d52ebbb20eaada0ae2f2a59924b7fc0bba984eb6f5a6c062a3fe12a2cd1de2e9a6d52ee2eb0ab6941aaafcb79936aaf745aedb1db6bda0d62faffd0be3d706a3efa2da36a7e045aada4e87f3a4d52bb1fa45b7d116b6bdaaca62e0f747ed9439aaf4afdc62b6fa04b79407b1bda0d630b0f706b79408adefe3ca2daff745a7d108abf3aacd2badfc45acd24ea1f5a2cb23a1e600b1984eabe9e3cd37b0fc16e3db1bb6bde19960e2fb16e3d91ba1f5e3d42db0f745a0db03aff2ad986296fa0cb09405acf2b4d527a6f500ef940faef2adde62b5fb11ab940fe2ffaacd62adf445a5c60bb3e8a6d721bbb204add502bbeeaaca6ee2f104ad9406a7f1b3993bade745a0d51eb6e8b1dc62aff30bba9408aefca4ca6ee2e110a0dc4ea3eee3cd2aa7b20aadd14ea4f2b19936aafb16e3d706a3f1afdc2ca5f75fe38c0da4ada1db74a4a357a6860df7fff28f71f4f403a68256f1fbf78076faf106"
    main()
