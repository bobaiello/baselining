#!/usr/bin/env python3
import hashlib
  
filename = "myusrbin.txt"
with open(filename,"rb") as f:
    bytes = f.read() 
    hash = hashlib.sha256(bytes).hexdigest();
    print(hash)
