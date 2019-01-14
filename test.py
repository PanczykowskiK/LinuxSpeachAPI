import threading
import subprocess
import sys
import time
import os
import signal
import recorder

def one():
    p = subprocess.Popen('chromium', stdout=subprocess.PIPE)
    time.sleep(2)

    h = subprocess.Popen('chromium', stdout=subprocess.PIPE)
    time.sleep(6)

    os.kill(p.pid, signal.SIGTERM)
    time.sleep(2)


import sounddevice as sd

#print(sd.query_devices())
#sd.default.device= "hw:1,0"
#print(sd.query_devices())

import bpy

def ShowMessageBox(message = "", title = "Message Box", icon = 'INFO'):

    def draw(self, context):
        self.layout.label(message)

    bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)

ShowMessageBox("Hello")