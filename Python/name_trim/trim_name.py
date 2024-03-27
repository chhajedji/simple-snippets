#!/usr/bin/env python3

import os
import string

# Change the value here as per your use.
total_max_len = 15
directory = "../size-calculator/test/"

def trim_filename(filename):
    # Empty filenames
  if not filename:
      return filename

  if len(filename) <= int(total_max_len):
      return filename

  trimmed_name = filename[:int(total_max_len/2)] + filename[-int(total_max_len/2):]

  # Remove all special characters except alphanumeric, underscore, period, and hyphen
  valid_chars = string.ascii_letters + string.digits + "_" + "-" + "."
  cleaned_name = ''.join(c for c in trimmed_name if c in valid_chars)

  # Avoid unnecessary renaming
  if filename != cleaned_name:
      # Build the full path with trimmed name
    filepath = os.path.join(os.path.dirname(filename), cleaned_name)

    os.rename(filename, filepath)

  return cleaned_name

os.chdir(directory)

for filename in os.listdir():
    trimmed_name = trim_filename(filename)

print("Finished trimming filenames.")
