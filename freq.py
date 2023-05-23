import numpy as np
import matplotlib.pyplot as plt

# Generate sample signal
t = np.linspace(0, 1, 1000)  # Time vector
f = 5  # Frequency of the signal
signal = np.sin(2 * np.pi * f * t)

# Perform Fourier Transform
freq_spectrum = np.fft.fft(signal)

# Calculate corresponding frequencies
sampling_freq = 1 / (t[1] - t[0])
freq = np.fft.fftfreq(len(signal), d=1/sampling_freq)

# Plot the frequency spectrum
plt.plot(freq, np.abs(freq_spectrum))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Frequency Spectrum')
plt.grid(True)
plt.show()
