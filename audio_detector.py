#!/usr/bin/env python3
"""Show a text-mode spectrogram using live microphone data."""
import argparse
import math
import numpy as np
import shutil
import sys
import  state
import queue
import soundfile as sf
import time
import matplotlib.pyplot as plt
import threading
from wave import    open
import run_sarmata
from scipy.io.wavfile import  read, write
import action
usage_line = ' press <enter> to quit, +<enter> or -<enter> to change scaling '


def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

try:
    columns, _ = shutil.get_terminal_size()
except AttributeError:
    columns = 80

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('-l', '--list-devices', action='store_true',
                    help='list audio devices and exit')
parser.add_argument('-b', '--block-duration', type=float,
                    metavar='DURATION', default=50,
                    help='block size (default %(default)s milliseconds)')
parser.add_argument('-c', '--columns', type=int, default=columns,
                    help='width of spectrogram')
parser.add_argument('-d', '--device', type=int_or_str,
                    help='input device (numeric ID or substring)')
parser.add_argument('-g', '--gain', type=float, default=10,
                    help='initial gain factor (default %(default)s)')
parser.add_argument('-r', '--range', type=float, nargs=2,
                    metavar=('LOW', 'HIGH'), default=[100, 2000],
                    help='frequency range (default %(default)s Hz)')
args = parser.parse_args()

def rms(data):
    try:
        return int( 10* np.log10(np.mean(abs(data / 65535) ** 2)))
    except: return -100

try:
    import sounddevice as sd

    q = queue.Queue()




    def callback(indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)

        q.put(indata)





    sd.default.device = "hw:1,0"

        #print(int( 10* np.log10(np.mean(abs(indata / 65535) ** 2))))

    def record(filename):
        q2 = queue.Queue()

        def callback2(indata, frames, time, status):
            if status:
                print(status, file=sys.stderr)
            q2.put(indata)
        silence = 0
        with sf.SoundFile(filename, mode='x', samplerate=44100, channels=1, subtype='PCM_16') as file:
            with sd.InputStream(device='pulse', channels=1, callback=callback2, blocksize=44100, samplerate=44100,
                                dtype="int16"):
                #file.write(data_in)
                while True:
                    data2 = q2.get()
                    file.write(data2)
                    try:
                        level = int(10 * np.log10(np.sqrt(np.mean((data2 / 65535) ** 2))))
                        if level > -20:
                            silence = 0
                        #elif silence < 250:
                            #silence += 1
                        else:
                            silence = 0
                            print("stoprecording: " + filename)
                            one = state.state.getInstance()
                            one.state = False


                            break
                    except:
                        None


                result = run_sarmata.RunSarmata(filename)
                action.action(result )

    audio_data = []
    recording = False
    silence = 0
    filename = ""
    with sd.InputStream(device='pulse', channels=1,  callback=callback, blocksize=16, samplerate=44100,  dtype="int16"):

        while True:
            data = q.get()
            try:
                level = np.log10(np.sqrt(np.mean((data/65535) **2)))
                if level > -1.2:

                    filename = "records/" + str(time.time()) + ".wav"
                    t = threading.Thread(target=record, args={filename})
                    t.start()
                    print("recording")
                    one = state.state.getInstance()
                    one.state = True
                    while one.state:
                        None
            except: None
            #else: print(level)


    plt.plot(np.ndarray.tolist(data))
    plt.show()


except KeyboardInterrupt:
    parser.exit('Interrupted by user')
except Exception as e:
    parser.exit(type(e).__name__ + ': ' + str(e))