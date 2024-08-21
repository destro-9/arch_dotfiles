#!/usr/bin/env python
import os
import random
import time

# Configurazione dei parametri
WAIT_TIME = 150 # 300  # Tempo di attesa in secondi prima di iniziare a cambiare lo sfondo
FPS = 75  # FPS della transizione
STEP = 45  # Step della transizione
PATH_TO_FOLDER = "/home/salem/Pictures/Wallpaper"  # Cartella contenente le immagini
TRANS_TIME = 3
TYPE = "random"
WAVE = '' #"20.0,20.0"

ENV_FPS = "SWWW_TRANSITION_FPS"
ENV_STEP = "SWWW_TRANSITION_STEP"
ENV_DURATION = "SWWW_TRANSITION_DURATION"
ENV_TYPE = "SWWW_TRANSITION_TYPE"

# Imposta i valori delle variabili d'ambiente
# os.environ[ENV_FPS] = str(FPS)
# os.environ[ENV_STEP] = str(STEP)
# os.environ[ENV_DURATION] = str(TRANS_TIME)
# os.environ[ENV_TYPE] = str(TYPE)
# os.system(set -Ux SWWW_TRANSITION_FPS 30)
# os.system(set -Ux SWWW_TRANSITION_STEP 10)

# Attendi X1 secondi prima di iniziare
time.sleep(WAIT_TIME)

# Loop per cambiare lo sfondo desktop
while True:
    # Seleziona una immagine casuale dalla cartella Y1
    image_files = os.listdir(PATH_TO_FOLDER)
    random_image = os.path.join(PATH_TO_FOLDER, random.choice(image_files))

    # Imposta lo sfondo desktop usando il comando swww
    if WAVE:
        os.system(f"swww img --transition-fps {FPS} \
                             --transition-duration {TRANS_TIME} \
                             --transition-step {STEP} \
                             --transition-type {TYPE} \
                             --transition-wave {WAVE} \
                             {random_image}")
    else:
        os.system(f"swww img --transition-fps {FPS} \
                             --transition-duration {TRANS_TIME} \
                             --transition-step {STEP} \
                             --transition-type {TYPE} \
                             {random_image}")
    #os.system(f"swww img -t {}")

    # Attendi X1 secondi prima di cambiare nuovamente lo sfondo
    time.sleep(WAIT_TIME)
