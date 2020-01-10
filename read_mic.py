# read_mic.py

"""
Code to read in audio from the microphone
"""

import pyaudio
import numpy as np
import matplotlib.pyplot as plt

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
# for i in range(10): #to it a few times just to see
# 	data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
# 	print(data)
# 	print(data.shape)




# # close the stream gracefully
# stream.stop_stream()
# stream.close()
# p.terminate()

# # Plot the last bit of data
# plt.plot(range(data.shape[0]), data)
# plt.show()


################################################################################
# Push the envelope
T = 10 # seconds -- how long we want to run
r = int(T * (RATE / CHUNK))

for i in range(r):
	data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
	peak=np.average(np.abs(data))*2
	bars="#"*int(50*peak/2**16)
	print("%04d %05d %s"%(i,peak,bars))

stream.stop_stream()
stream.close()
p.terminate()