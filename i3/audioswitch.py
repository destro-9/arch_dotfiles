#!/usr/bin/env python
import os
import subprocess

selected = subprocess.check_output("pactl get-default-sink", shell=True)
print(selected)
if selected == b'alsa_output.pci-0000_00_1b.0.analog-stereo\n' :
    os.system('pacmd set-default-sink 1')
else :
    os.system('pacmd set-default-sink 2')