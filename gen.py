#!/usr/bin/env python3

from typing import List
import math
from PIL import Image
import sys

if len(sys.argv) < 1:
    print("pass it a path to a valid png")
    exit(1)
path = sys.argv[1]

color_map = []

try:
    im = Image.open(path)
except Exception as e:
    print(e)
    exit(1)

if len(im.getpixel((0,0))[:-1]) < 3:
    print('invalid png data')
    exit(1)

for x in range(im.height):
    for y in range(im.width):
        color_map.append("#%02x%02x%02x" % im.getpixel((y, x))[:-1])


def gen_cols_rows(num_pixels):
    elems = int(math.sqrt(num_pixels))
    n = 100 / math.sqrt(num_pixels)
    return f"{n}% " * elems


header = """
<html>
    <head>
        <style>
#app {{
    justify-content: center;
    position:absolute;
}}

.grid-container {{
    display: grid;
    justify-content: center;
    grid-template-columns: {0};
    grid-template-rows: {0};
    width: 1000px;
    height: 1000px;
}}

.grid-item {{
    height: 100%;
    width: 100%;
    text-align: center;
}}
        </style>
    </head>
    <body>
        <div class="app">
            <div class="grid-container">
""".format(
    gen_cols_rows(len(color_map))
)

footer = """
            </div>
        </div>
    </body>
</html>
"""


def gen_body(color_map: List) -> str:
    return "\n".join(
        [
            f'\t\t\t\t<div class="grid-item" style="background-color: {cc}"></div>'
            for cc in color_map
        ]
    )


with open("index.html", "w") as f:
    f.write(header)
    f.write(gen_body(color_map))
    f.write(footer)
