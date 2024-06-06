import numpy as np
import matplotlib.pyplot as plt

# Define the range of t values
t = np.linspace(-2*np.pi, 2 * np.pi, 400)

# Initialize the function with the constant term
f_t = (2 + np.pi) / 4

# Number of terms to include in the series
num_terms = 7

# Compute the Fourier series sum
for n in range(1, num_terms):
    cosine_term = (np.power(-1, n) - 1) / (np.pi * n**2) * np.cos(n * t)
    sine_term = ((1 - np.pi) * np.power(-1, n) - 1) / (np.pi * n) * np.sin(n * t)
    f_t += cosine_term + sine_term

# Plot the resulting function
plt.plot(t, f_t, label=f"First {num_terms} terms")
plt.title("Fourier Series Approximation")
plt.xlabel("t")
plt.ylabel("f(t)")
plt.legend()
plt.grid(True)
plt.show()