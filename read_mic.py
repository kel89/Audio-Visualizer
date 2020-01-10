# read_mic.py

"""
Code to read in audio from the microphone
"""

import pyaudio
import numpy as np

CHUNK = 1024 # how much to read at a time
RATE = 41400 # resolution of recording device, on mac from Audio MIDI setup (search it)

p = pyaudio.PyAudio() # start the pyaudio class
stream = p.open(format=pyaudio.paInt16,
				channels=1,
				rate=RATE,
				input=True,
				frames_per_buffer=CHUNK
				)

# create a numpy array holding a single read of audio data
for i in range(10): #to it a few times just to see
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    print(data)


# close the stream gracefully
stream.stop_stream()
stream.close()
p.terminate()
