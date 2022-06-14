#!/usr/bin/env python3

import os, sys

if len(sys.argv) > 1:
    cwd = sys.argv[1]
else:
    cwd = './'

all_files = []

def list_files(base_dir):
    global all_files
    # print("base_dir: ", base_dir)
    for entry in os.listdir(base_dir):
        if os.path.isdir(os.path.join(base_dir, entry)):

            list_files(os.path.join(base_dir, entry))
        elif os.path.isfile(os.path.join(base_dir, entry)):
            # print(entry, " is a file.")
            # print("Found a file: ", entry, "\tAppending: ", os.path.join(base_dir, entry))
            all_files.append(os.path.join(base_dir, entry))
        # print("****\nentry: {}\nall_files: {}\n****\n".format(entry, all_files))
    # return all_files


list_files(cwd)
print("==========")
for entry in all_files:
    print(entry)
print("==========")
