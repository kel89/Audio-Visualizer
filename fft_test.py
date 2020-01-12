# fft_test.py

import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as sc_fft

# Test signal
sampling_rate = 100
t = np.arange(0, 8 * np.pi, 1/sampling_rate)
s = np.sin(5*t) + .2 * np.sin(4*5*t)

# Run the transform
fft = sc_fft.fft(s)
freq = sc_fft.fftfreq(t.shape[0]) * sampling_rate

# Trim to be positive
N = t.shape[0]
fft = fft[0: int(N//2)]
freq = freq[0: int(N//2)]


fig, ax = plt.subplots(nrows=2, ncols=1)
ax1 = ax[0]
ax2 = ax[1]

ax2.plot(t, s)
ax1.stem(freq, np.abs(fft))
ax1.set_xlim([0, sampling_rate/2])
plt.show()

"""
Some things worth noting:
+ we want to determine a sampling rate
+ we use the samplign rate to determine frequencies
+ we use the sampling rate to set the plot axis
"""