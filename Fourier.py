import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Define the square wave function
def square_wave(x):
    return 1 if (x % (2 * np.pi)) < np.pi else -1

# Calculate the nth coefficient of the Fourier series
def fourier_coefficient(n, f, L):
    a0 = quad(lambda x: f(x), -L, L)[0] / (2 * L)
    an = quad(lambda x: f(x) * np.cos(n * np.pi * x / L), -L, L)[0] / L
    bn = quad(lambda x: f(x) * np.sin(n * np.pi * x / L), -L, L)[0] / L
    return a0, an, bn

# Number of terms in the Fourier series
N = 10
L = np.pi  # Period of the square wave

# Calculate coefficients
coefficients = [fourier_coefficient(n, square_wave, L) for n in range(N)]

# Construct the Fourier series
def fourier_series(x, coeffs):
    a0 = coeffs[0][0]
    series = a0 / 2
    for n in range(1, len(coeffs)):
        an, bn = coeffs[n][1], coeffs[n][2]
        series += an * np.cos(n * np.pi * x / L) + bn * np.sin(n * np.pi * x / L)
    return series

# Plotting
x_vals = np.linspace(-3 * np.pi, 3 * np.pi, 1000)
original = np.vectorize(square_wave)(x_vals)
approximation = fourier_series(x_vals, coefficients)

plt.plot(x_vals, original, label='Original Function')
plt.plot(x_vals, approximation, label='Fourier Series Approximation')
plt.legend()
plt.show()