import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

# Define input and impulse response
t = np.linspace(0, 10, 1000)
x = np.heaviside(t, 1)  # Unit step function
h = np.exp(-t) * np.heaviside(t, 1)  # Exponential decay

# Compute convolution
y = convolve(x, h, mode='full')[:len(t)] * (t[1] - t[0])

# Plot
plt.figure(figsize=(10, 6))
plt.plot(t, x, label='Input: x(t) (Unit Step)')
plt.plot(t, h, label='Impulse Response: h(t) (Exponential Decay)')
plt.plot(t, y, label='Output: y(t) (Convolution)')
plt.legend()
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.title('Convolution of x(t) and h(t)')
plt.grid()
plt.show()
