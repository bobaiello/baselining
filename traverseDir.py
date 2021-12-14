#!/usr/bin/env python3
# traverse dir

import os
import hashlib

def calcsha(arg1):
    print ("inside function" + str(arg1))
    value = 3;
    return value;

input_path = "/var/www/html"

mysha1 = calcsha(8)

print("function value is" + str(mysha1))


exit()

fo = open("filelistDec142021.lis", "w")

for dir_path, subdir_list, file_list in os.walk(input_path):
    for fname in file_list:
        full_path = os.path.join(dir_path, fname)
        print(full_path)
        fo.write(full_path)

fo.close()


filename = "myusrbin.txt"
with open(filename,"rb") as f:
    bytes = f.read()
    hash = hashlib.sha256(bytes).hexdigest();
    print(hash)

