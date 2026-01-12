""" This program convertes jpg images to png."""

import sys
import os
from pathlib import Path
from PIL import Image

first_arg = sys.argv[1]
folder_path = Path('D:\Python-Programs\old_images')

parent_dir = os.path.dirname(first_arg)
second_arg = "New"

# Full path of New inside first_arg
second_arg_path = os.path.join(parent_dir, second_arg)

# Check if New exists
if os.path.isdir(second_arg_path):
    print("Folder New already exists.")
else:
    os.mkdir(second_arg_path)
    print("Folder New created successfully.")

for img in folder_path.iterdir():
    image = Image.open(img)
    print(image)