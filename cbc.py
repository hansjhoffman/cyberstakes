#!/usr/bin/env python
from Crypto.Cipher import AES

def decrypt(ciphertext, key, iv):
    return AES.new(key, AES.MODE_CBC, IV=iv).decrypt(ciphertext)

if __name__ == "__main__":
    ciphertext = "\x36\x4a\x13\xe0\x21\xce\xc0\x4b\x23\xb6\x8c\x8c\x94\x5f\x07\xc1\xa4\x50\x7d\xb6\x96\xb5\xf7\xad\x8c\x2d\x00\x96\x0a\xca\xad\x74"
    key = "\x5c\x00\x34\x5f\xba\xe1\xec\xe7\xf1\xbe\xb4\x25\x6f\xda\x0a\x33"
    iv = "\x15\xff\xfc\xc0\x42\xbf\x9c\x9d\xcc\x14\x92\xdb\x38\xb7\xbe\x90"

    plaintext = decrypt(ciphertext, key, iv)
    print "\n{}\n".format(plaintext)
