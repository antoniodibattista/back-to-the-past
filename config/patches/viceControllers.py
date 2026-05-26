#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# PATCH Back To The Past:
# Batocera V5.25 va in crash all'avvio dei giochi C64 (vice) se NON c'e' un
# joypad collegato: 'listVice' veniva definito solo dentro il ciclo sui
# controller, quindi senza controller -> UnboundLocalError.
# Fix: inizializzare listVice = [] prima del ciclo (riga marcata sotto).
#
# Deploy su Asem: copiare in
#   /usr/lib/python2.7/site-packages/configgen/generators/vice/viceControllers.py
# rimuovere il .pyc accanto, poi `batocera-save-overlay` per renderlo permanente.

import batoceraFiles
import os
from Emulator import Emulator
import ConfigParser

viceJoystick = {
            "up":               "0 1 # 1 1 1",
            "down":             "0 1 # 1 1 2",
            "left":             "0 1 # 1 1 4",
            "right":            "0 1 # 1 1 8",
            "select":           "0 1 # 5 Virtual keyboard",
            "start":            "0 1 # 4",
            "hotkey":           "0 1 # 5 Quit emulator",
            "a":                "0 1 # 1 1 16",
            "b":                "0 1 # 2 0 1",
            "x":                "0 1 # 2 7 4",
            "y":                "0 1 # 2 7 7",
            "pagedown":         "0 1 # 2 4 7",
            "pageup":           "0 1 # 2 3 1"
        }

# Create the controller configuration file
def generateControllerConfig(viceConfigFile, playersControllers):
    # vjm file
    viceFile = viceConfigFile + "/sdl-joymap.vjm"

    if not os.path.exists(os.path.dirname(viceFile)):
        os.makedirs(os.path.dirname(viceFile))

    nplayer = 1
    listVice = []  # <-- FIX Back To The Past: evita il crash senza joypad
    for playercontroller, pad in sorted(playersControllers.items()):
        if nplayer == 1:
            listVice = []
            listVice.append("!CLEAR")
            # joystick1right
            listVice.append("0 0 0 1 1 8")
            # joystick1left
            listVice.append("0 0 1 1 1 4")
            # joystick1down
            listVice.append("0 0 2 1 1 2")
            # joystick1up
            listVice.append("0 0 3 1 1 1")

            # joystick2right
            listVice.append("0 0 6 1 1 8")
            # joystick2left
            listVice.append("0 0 7 1 1 4")
            # joystick2down
            listVice.append("0 0 8 2 0 7")
            # joystick2up
            listVice.append("0 0 9 2 0 7")

            for indexName, indexValue in viceJoystick.items():
                listVice.append(indexValue.replace('#', pad.inputs[indexName].id, 1))
            nplayer += 1

    f = open(viceFile, 'w')
    for i in range(len(listVice)):
        f.write(str(listVice[i]) + "\n")
    f.write
    f.close()
