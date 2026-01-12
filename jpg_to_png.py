""" This program convertes jpg images to png."""

import sys
import os
from PIL import Image

first_arg = sys.argv[1]

parent_dir = os.path.dirname(first_arg)
second_arg = "C"

# Full path of C inside A
second_arg_path = os.path.join(parent_dir, second_arg)

# Check if C exists
if os.path.isdir(second_arg_path):
    print("Folder C already exists.")
else:
    os.mkdir(second_arg_path)
    print("Folder C created successfully.")