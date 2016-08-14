#!/usr/bin/env python3
import os
import sys
import zipfile

def inception(index): 
    fh = "%s.docx" %(str(index))
    if os.path.isfile(fh):
        with zipfile.ZipFile(fh, "r") as z:
            try:
                z.extract("%s.docx" %(str(int(index)-1)))
                #have to delete old file b/c HDD will fill up due to large size
                os.remove(fh)
            except Exception as e:
                print("[!] {}".format(e))
    else:
        print("[!] File [{}] does not exist".format(fh))
        sys.exit(1)

def main():
    for i in range(249, 1, -1):
        inception(i)

if __name__ == "__main__":
    #unzip -p doc2.docx 249.docx >249.docx
    #unzip -p 1.docx key >key
    main()
