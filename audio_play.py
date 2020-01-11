# audio_play.py

"""
Just playing with the PyAudio package to understand it better
"""

import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animate

import code # for jumping to interactive

p = pyaudio.PyAudio()

RATE = 44100
CHUNK = 1024
FORMAT = pyaudio.paInt16

s = p.open(	format=FORMAT,
			channels=1,
			rate=RATE,
			input=True,
			frames_per_buffer=CHUNK)

if (False):

	print("*recording")

	"""
	So lets thnik about this, we are recording at 44100 samples per second
	I am reading in chunks of 1024 samples, so on seconds will require
		44100/1024 readings for 1 second of recording
	"""

	# Get a second of recording
	data = []
	num_loops = int(1 * (RATE / CHUNK) ) # where the 1 is seconds desired
	for i in range(num_loops):
		new = list(np.frombuffer(s.read(CHUNK), dtype=np.int16)) # <---- the issue seems to be i idnd't specify dtype befre!!!
		data = data + new

	print("Done recording *")

	print(len(data))

	# Print a chunk
	# data = s.read(CHUNK)
	# decoded = np.frombuffer(data)
	# print(decoded)

	s.stop_stream()
	s.close()
	p.terminate()

	# code.interact(local=locals())
	# Plot that
	plt.plot(range(len(data)), data)
	plt.show()

if (True):
	# Okay, in the above we know how to record 1 second of data and plot it
	# Now, how can we figure out how to keep doing that in an animation?

	fig, ax = plt.subplots(figsize=(10, 5))

	# Half second of data requires how many iterations?
	refresh = 100 # in miliseconds
	num_loops = int((refresh/1000) * (RATE / CHUNK))

	def get_data():
		"""
		Returns a half second of data
		"""
		data = np.array([])
		for i in range(num_loops):
			new = np.frombuffer(s.read(CHUNK, exception_on_overflow=False), dtype=np.int16)
			data = np.concatenate([data, new])
		return data

	def anim_plot(i):
		"""
		Plot animation,
		gets the new data, plots it
		"""
		new_data = np.array(get_data())
		ax.clear()
		ax.plot(range(new_data.shape[0]), new_data)

	# Make the animation
	anim = animate.FuncAnimation(fig, anim_plot, interval=refresh)
	plt.show()
