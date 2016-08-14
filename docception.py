#!/usr/bin/env python
import os
import sys
import zipfile

def inception(index):
    fh = "%s.docx" %(str(index))
    if os.path.isfile(fh):
        with zipfile.ZipFile(fh, "r") as z:
	    try:
	        z.extract("%s.docx" %(str(index-1)))
		#have to delete old file b/c HDD will fill up due to large size
		os.remove(fh)
	    except Exception as e:
	        print "[!] {}".format(e)
    else:
        print "[!] File [{}] does not exist".format(fh)
	sys.exit(1)

def main():
    for i in range(999, 1, -1):
	inception(i)

if __name__ == "__main__":
    #unzip -p docception.docx 999.docx >999.docx
    #unzip -p 1.docx flag >flag
    main()
