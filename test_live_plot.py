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
fig, axs = plt.subplots(ncols=1, nrows=2, figsize=(10,6))
ax1 = axs[0]
ax2 = axs[1]

ax1.set_xlim([0, 2*np.pi])
ax2.set_xlim([0, 2*np.pi])
ax1.set_ylim([-1, 1])
ax2.set_ylim([-1, 1])
# ax.set_xlim([0, 2*np.pi])
# ax.set_ylim([-1.2, 1.2])

# curve, = ax.plot([], []) # comma unpacks the returned tuple
curve_top, = ax1.plot([], [])
curve_bot, = ax2.plot([], [])

# Function that will do the plotting
def plot(i):
	t = np.arange(0, 2*np.pi, .01)
	y = np.sin((t-(i/20)))
	y1 = np.cos(t-(i/20))

	curve_top.set_data(t, y)
	curve_bot.set_data(t, y1)
	return curve_top, curve_bot
	# plt.show()

anim = animate.FuncAnimation(fig, plot, interval=1, frames=400, blit=True, repeat=False)

plt.show()

