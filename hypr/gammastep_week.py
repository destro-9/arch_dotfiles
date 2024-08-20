#!/usr/bin/python
import datetime
import os

#######################
### 0 = Monday      ###
### 1 = Tuesday     ###
### 2 = Wednesday   ###
### 3 = Thursday    ###
### 4 = Friday      ###
### 5 = Saturday    ###
### 6 = Sunday      ###
#######################

def gammastep_on_custom_days():

    # --> bW[0,0,0,0,1,1,0] <--
    # bW[1] == 0 -> Default on Tuesday
    # bW[5] == 1 -> Saturday on config1
    # sets different custom file
    default = 'gammastep'
    config1 = 'gammastep -c /home/salem/.config/hypr/gammastep/gammas_conf1.ini'
    booleanWeek = [0,0,0,0,1,1,0]

    now = datetime.datetime.today().weekday()
    today = booleanWeek[now]

    if today == 0:
        os.system(default)
    elif today == 1:
        os.system(config1)
    else:
        os.system(default)

if __name__ == "__main__":
    gammastep_on_custom_days()
