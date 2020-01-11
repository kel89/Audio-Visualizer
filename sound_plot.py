# sound_plot.py

"""
Quick and dirty script to plot from the microphone
"""

import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animate

CHUNK = 1024
RATE = 41400 

# Setup sound reader
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
				channels=1,
				rate=RATE,
				input=True,
				frames_per_buffer=CHUNK
			)

# Setup Plotting
fig, ax = plt.subplots(figsize=(10,6))
ax.set_xlim([0, CHUNK])
curve, = ax.plot([], [], lw=3)

# Plotting function
def plot(i):
	y = np.frombuffer(stream.read(CHUNK, exception_on_overflow=False),dtype=np.int16)
	ax.set_ylim([0, 100])
	curve.set_data(range(CHUNK), y)
	print(np.max(y), np.min(y))
	return curve,

# Animation
anim = animate.FuncAnimation(fig, plot, interval=200, blit=True)
plt.show()

