# alpha.py

"""
Alpha version, MVP 
"""

import pyaudio
import numpy as np
import scipy.fftpack as sc_fft
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
fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(6, 5))
ax_top = axs[0] # fft
ax_bot = axs[1] # wave

ax_top.set_xlim([0, RATE/2])

ax_top.set_yticks([])
ax_bot.set_yticks([])

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
	# Run the FFT
	N = data.shape[0]
	fft = sc_fft.fft(data)
	freq = sc_fft.fftfreq(N) * RATE

	# Truncate it
	fft = np.abs(fft[100:int(N//2)])
	freq = freq[100:int(N//2)]

	return fft, freq

def animate_plot(i):
	"""
	Animates the plot, at each step
	clears the axes and plots the wave and the fft
	"""
	wave_data = get_data()

	# Get FFT data
	fft, freq = get_fft(wave_data)

	ax_bot.clear()
	ax_bot.plot(range(wave_data.shape[0]), wave_data)

	# Plot FFT data
	ax_top.clear()
	ax_top.plot(freq, fft)

	ax_top.set_yticks([])
	ax_bot.set_yticks([])

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









