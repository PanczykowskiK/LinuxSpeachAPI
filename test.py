#File for testing new code or new idea
import threading
import subprocess
import sys
import time
import os
import signal
class action:

    def one():
        p = subprocess.Popen('chromium', stdout=subprocess.PIPE)
        time.sleep(2)

        h = subprocess.Popen('chromium', stdout=subprocess.PIPE)
        time.sleep(6)

        os.kill(p.pid, signal.SIGTERM)
        time.sleep(2)


import os

str = 'hello wworld i am  23'
h = str.split()
print(h)