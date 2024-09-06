#!/usr/bin/env python
import datetime
import os

defaultConf = 'gammastep'
config1 = 'gammastep -c /home/salem/.config/hypr/gammas_conf1.ini'

def is_weekend_config_time():
    now = datetime.datetime.now()
    weekday = now.weekday()
    current_time = now.time()
    # Venerdì dopo le 8:00
    if weekday == 4 and current_time >= datetime.time(8, 0):
        return True
    # Sabato
    elif weekday == 5:
        return True
    # Domenica prima delle 8:00
    elif weekday == 6 and current_time < datetime.time(8, 0):
        return True
    return False

if is_weekend_config_time():
    os.system(config1 + ' & disown')
else:
    os.system(defaultConf + ' & disown')
