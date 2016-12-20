#!/usr/bin/python
from PIL import Image
import os, sys

path = "googlemak/game/images/backgrounds/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((1280,720), Image.ANTIALIAS)
            imResize.save(f + '_done.png', 'PNG', quality=90)

resize()
