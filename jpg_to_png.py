""" This program convertes jpg images to png."""

import sys
import os
from pathlib import Path
from PIL import Image

first_arg = sys.argv[1]
second_arg = sys.argv[2]

# Check if New exists
if not os.path.exists(second_arg):
    os.mkdir(second_arg)

for img in os.listdir(first_arg):
    image = Image.open(f'{first_arg}{img}')
    print(image)
    png_name = os.path.splitext(img)[0] + ".png"
    png_path = os.path.join(second_arg, png_name)

    # Save as PNG in New
    image.save(png_path, "PNG")

