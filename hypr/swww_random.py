#!/usr/bin/env python
import os
import random
import time
import sys

# Configurazione dei parametri
WAIT_TIME = 150 # 300
FPS = 75  # FPS della transizione
STEP = 45  # Step della transizione
PATH_TO_FOLDER = "/home/salem/Pictures/Wallpaper"
TRANS_TIME = 3  # Durata transizione
TYPE = "random"  # Tipo di effetto

try:
    outputs = sys.argv[1:]
except IndexError:
    outputs = ''
swww = "swww img {} --transition-fps {} \
                    --transition-duration {} \
                    --transition-step {} \
                    --transition-type {} \
                    {}"
image_files = os.listdir(PATH_TO_FOLDER)
while True:
    if not outputs:
        # Seleziona una immagine casuale dalla cartella
        random_image = os.path.join(PATH_TO_FOLDER, random.choice(image_files))
        os.system(swww.format('',FPS,TRANS_TIME, \
                              STEP, TYPE, random_image))
    else:
        for monitor in outputs:
            random_image = os.path.join(PATH_TO_FOLDER, random.choice(image_files))
            output_flag = f'-o {monitor}'
            os.system(swww.format(output_flag, FPS, TRANS_TIME, \
                                  STEP, TYPE, random_image))

    time.sleep(WAIT_TIME)
