# alpha.py

"""
Alpha version, MVP 
"""

import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animate

# Setup Steam ------------------------------------------------------------------
p = pyaudio.PyAudio()

RATE = 44100
CHUNK = 1024
FORMAT = pyaudio.paInt16

s = p.open(	format=FORMAT,
			channels=1,
			rate=RATE,
			input=True,
			frames_per_buffer=CHUNK)

# Setup Plot -------------------------------------------------------------------
fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(7, 8))
ax_top = axs[0]
ax_bot = axs[1]

REFRESH = 100 # miliseconds
num_loops = int((REFRESH/1000) * (RATE / CHUNK))

def get_data():
	"""
	Returns a half second of data
	"""
	data = np.array([])
	for i in range(num_loops):
		new = np.frombuffer(s.read(CHUNK, exception_on_overflow=False), dtype=np.int16)
		data = np.concatenate([data, new])
	return data

def get_fft(data):
	"""
	Takes in some wave data and returns
	fft frequencies, and amplitudes (double return)
	"""
	# TODO 
	return

def animate_plot(i):
	"""
	Animates the plot, at each step
	clears the axes and plots the wave and the fft
	"""
	wave_data = get_data()

	# Get FFT data

	ax_top.clear()
	ax_top.plot(range(wave_data.shape[0]), wave_data)

	# Plot FFT data

try:
	# Animate the plot
	anim = animate.FuncAnimation(fig, animate_plot, interval=REFRESH)
	plt.show()
except KeyboardInterrupt:
	print("Program Stopped via key")
finally:
	# clean up
	s.stop_stream()
	s.close()
	p.terminate()









