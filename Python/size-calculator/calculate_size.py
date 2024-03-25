#!/usr/bin/env python

import os

def human_readable_size(size, decimal_places=2):
    """
    Converts a file size in bytes to a human-readable format (e.g., KB, MB, GB, TB).
    """
    units = ["B", "KB", "MB", "GB", "TB"]
    factor = 1024
    i = 0
    while size > factor and i < len(units) - 1:
        size /= factor
        i += 1
    return f"{size:.{decimal_places}f} {units[i]}"

# files.txt contains all the files for which combined size needs to be calculated.
total_size = 0
with open("files.txt", "r") as file:
  for line in file:
    filename = line.strip()  # Remove any trailing newline character
    if os.path.isfile(filename):
      total_size += os.path.getsize(filename)

# print(f"The combined size of the files is: {total_size} bytes")
print(f"The combined size of the files is: {human_readable_size(total_size)}")


