# test_live_plot.py

"""
Script to test live plotting with matplotlib

In the future, I Think this is a great resource:
https://towardsdatascience.com/animations-with-matplotlib-d96375c5442c
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animate
import numpy as np

# Create the figure
fig, ax = plt.subplots(figsize=(10,5))
ax.set_xlim([0, 2*np.pi])
ax.set_ylim([-1.2, 1.2])

curve, = ax.plot([], []) # comma unpacks the returned tuple

def init_curve():
	curve.set_data([], [])
	return curve

# Function that will do the plotting
def plot(i):
	t = np.arange(0, 2*np.pi, .01)
	y = np.sin((t-(i/20)))

	curve.set_data(t, y)
	return curve,
	# plt.show()

anim = animate.FuncAnimation(fig, plot, interval=1, frames=400, blit=True, repeat=False)
plt.show()

