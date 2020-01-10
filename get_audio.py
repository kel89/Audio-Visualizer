# get_audio.py

"""
Function get get a chunk of real audio for us to do analysis on
Just a mini helper for testing
"""

import pyaudio
import numpy as np
import matplotlib.pyplot as plt

def get_audio(T):
	"""
	Returns a numpy array with audio sample of the desired length
	"""

	CHUNK = 1024 # how much to read at a time
	RATE = 41400 # resolution of recording device, on mac from Audio MIDI setup (search it)

	p = pyaudio.PyAudio() # start the pyaudio class
	stream = p.open(format=pyaudio.paInt16,
					channels=1,
					rate=RATE,
					input=True,
					frames_per_buffer=CHUNK
					)

	# Range to sample
	r = int(T * (RATE / CHUNK))

	# Initialize numpy array to store data
	data = np.zeros(r*CHUNK)

	# Collect the data
	l = 0
	for i in range(r):
		# Collect the new data
		new_data = np.frombuffer(stream.read(CHUNK),dtype=np.int16)

		# Save the new data
		data[l:(l + new_data.shape[0])] = new_data

		# Increment
		l += new_data.shape[0]

	output = {
		"chunk": CHUNK,
		"rate": RATE,
		"data": data
	}

	return output

if __name__ == "__main__":
	out = get_audio(5)
	print(out)

	# Plot the output
	y = out['data']
	plt.plot(range(y.shape[0]), y)
	plt.show()

"""
Your next steps are to:
	FFT the wave form in small chuncks and plot it
	Figure out how to do both with live data and show it
"""
