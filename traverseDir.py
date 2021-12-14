#!/usr/bin/env python3
# traverse dir

import os

input_path = "/var/www/html"

for dir_path, subdir_list, file_list in os.walk(input_path):
    for fname in file_list:
        full_path = os.path.join(dir_path, fname)
        print(full_path)

