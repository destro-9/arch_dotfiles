#!/usr/bin/env python

import os
import random
import time

# directory dei file
directory = '/home/salem/Pictures/Wallpaper/'

# lista dei file nella cartella
files = os.listdir(directory)

# mescola i file in modo randomico
random.shuffle(files)

# stampa i file mescolati
while True:
    for f in files:
        time.sleep(600)
        if f == "vapor08.png" or f == "Wendigo01.jpg" :
            os.system("feh --bg-fill ~/Pictures/Wallpaper/"+f)
        else:
            os.system("feh --bg-scale ~/Pictures/Wallpaper/"+f)
        #time.sleep(10)
