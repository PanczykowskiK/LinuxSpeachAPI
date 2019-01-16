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
import threading
usage_line = ' press <enter> to quit, +<enter> or -<enter> to change scaling '

from dictation.dictation_client import create_audio_stream, print_results
from dictation.service.dictation_settings import DictationSettings
from dictation.service.streaming_recognizer import StreamingRecognizer
from address_provider import AddressProvider
from os.path import join as opjoin
import action
import run_sarmata

class DictationArgs:
    address = None  # IP address and port (address:port) of a service the client will connect to.
    interim_results = False  # If set - messages with temporal results will be shown.
    max_alternatives = 3  # Maximum number of recognition hypotheses to be returned.
    mic = False  # Use microphone as an audio source (instead of wave file).
    no_input_timeout = 5000  # MRCP v2 no input timeout [ms].
    recognition_timeout = 5000  # MRCP v2 recognition timeout [ms].
    session_id = None  # Session ID to be passed to the service. If not specified, the service will generate a default session ID itself.
    single_utterance = False  # If set - the recognizer will detect a single spoken utterance.
    speech_complete_timeout = 5000  # MRCP v2 speech complete timeout [ms].
    speech_incomplete_timeout = 6000  # MRCP v2 speech incomplete timeout [ms].
    time_offsets = False  # If set - the recognizer will return also word time offsets.
    wave = None  # Path to wave file with speech to be recognized. Should be mono, 8kHz or 16kHz.

    def __init__(self, wav_filepath=None):
        ap = AddressProvider()
        if wav_filepath:
            self.wave = opjoin(wav_filepath)
        self.address = ap.get("dictation")

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


    audio_data = None

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
                file.write(audio_data)
                counter = 0
                while True:
                    counter +=1
                    data2 = q2.get()
                    file.write(data2)
                    try:
                        if int(10 * np.log10(np.sqrt(np.mean((data2 / 65535) ** 2)))) < -15:
                            print("stoprecording: " + filename)
                            one = state.state.getInstance()
                            one.state = False
                            break
                    except:
                        None
                if counter < 5:
                    result = run_sarmata.RunSarmata(filename)
                    action.action(result)
                else:
                    args = DictationArgs(filename)
                    args.mic = True

                    if args.wave is not None or args.mic:
                            with create_audio_stream(args) as stream:
                                settings = DictationSettings(args)
                                recognizer = StreamingRecognizer(args.address, settings)

                                print('Recognizing...')
                                results = recognizer.recognize(stream)
                                print_results(results)
                                import pyautogui
                                pyautogui.typewrite((str(results[0]['transcript'])))


    recording = False
    silence = 0
    filename = ""
    with sd.InputStream(device='pulse', channels=1,  callback=callback, blocksize=16, samplerate=44100,  dtype="int16"):

        while True:
            data = q.get()
            audio_data = data
            try:
                level = np.sqrt(np.mean((data/65535) **2))
                if level > 0.06:
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