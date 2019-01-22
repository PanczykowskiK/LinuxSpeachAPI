#File for testing new code or new idea
import threading
import subprocess
import sys
import time
import os
import signal
import state
from dictation.dictation_client import create_audio_stream, print_results
from dictation.service.dictation_settings import DictationSettings
from dictation.service.streaming_recognizer import StreamingRecognizer


import queue
q2 = queue.Queue()

def callback2(indata, frames, time, status):
    q2.put_nowait(indata)
    q2.join()

silence = 0
import soundfile as sf
import sounddevice as sd
import numpy as np
import notify.notification as notify
def rms(data):
    return(10*np.log10(np.sqrt(np.mean((data)**2))))

from address_provider import AddressProvider
from os.path import join as opjoin
import time


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

def Recognize(filename):
    import run_sarmata
    import action
    result = run_sarmata.RunSarmata(filename)
    if result:
        if len(result) > 1:
            action.action(result)
        else:
            Dictation(filename)
    else:
        Dictation(filename)

def Dictation(filename):
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
            pyautogui.typewrite(("{}".format(results[0]['transcript'])))
            pyautogui.press('enter')

def read():
        audio_data = []
        old_data = []
        one = state.state.getInstance()
        while True:
            if not q2.empty():
                data = q2.get()
                q2.task_done()
                level = int(rms(data))
                one.AddLevel(level)
                if level > -15:
                    recorded = 0
                    counter = 0
                    silence = 0
                    one.state = True
                    for i in data:
                        audio_data.append(float(i))
                    old_data = data
                    while counter < 100:
                        data = q2.get()
                        q2.task_done()
                        level = int(rms(data))
                        one.AddLevel(level)
                        if True:
                            for i in data:
                                audio_data.append(float(i))
                            if level > -15:
                                counter = 0
                                recorded +=1
                            else:
                                counter += 1
                                silence += 1
                            old_data = data
                            time.sleep(0.005)
                    one.state = False

                    #import matplotlib.pyplot as plt
                    #plt.plot(audio_data)
                    #plt.title(one.GetRecordedLevel())
                    #plt.show()


                    with sf.SoundFile("records/{}.wav".format(time.time()), mode='x', samplerate=44100, channels=1, subtype='PCM_16') as file:
                        file.write(audio_data)
                        if 5*recorded > silence:
                            if len(audio_data) < 44100*3:
                                print("Sarmata")
                                t = threading.Thread(target=Recognize, args={file.name})
                                t.start()
                            else:
                                print("Dictation")
                                t = threading.Thread(target=Dictation, args={file.name})
                                t.start()
                        del audio_data[:]



                else:
                    time.sleep(0.001)
                    del audio_data[:]


def start_listening():
    with sd.InputStream(device='hw:2,0', channels=1, callback=callback2, blocksize=256, samplerate=44100, dtype="float32"):
        t = threading.Thread(target=read())
        t.start()
        while True:
            None


