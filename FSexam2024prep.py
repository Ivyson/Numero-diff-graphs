import numpy as np
import matplotlib.pyplot as plt

# Define the piecewise function f(t)
def piecewise_function(t):
    t = np.mod(t + np.pi, 2 * np.pi) - np.pi  # Adjusting t to be within the interval [-pi, pi]
    return np.where((-np.pi < t) & (t < 0), 1, np.where((0 < t) & (t < np.pi), t, 0))

# Define the Fourier series approximation function
def fourier_series(t, num_terms):
    f_t = 1/2 + np.pi/4
    for n in range(1, num_terms):
        a_n = -2 * (1 - (-1)**n) / (n**2 * np.pi)
        b_n = (1 - np.pi) * (-1)**n / n
        f_t += a_n * np.cos(n * t) + b_n * np.sin(n * t)
    return f_t

# Define the range of t values
t = np.linspace(-2 * np.pi, 2 * np.pi, 800)

# Calculate the piecewise function values
f_piecewise = piecewise_function(t)

# Calculate the Fourier series approximation values
num_terms = 10000000
f_fourier = fourier_series(t, num_terms)

# Plot the piecewise function
plt.plot(t, f_piecewise, label="Piecewise function f(t)")

# Plot the Fourier series approximation
plt.plot(t, f_fourier, label=f"Fourier series (first {num_terms} terms)", linestyle='--')

# Add labels and title
plt.title("Piecewise Function and Its Fourier Series Approximation")
plt.xlabel("t")
plt.ylabel("f(t)")
plt.legend()
plt.grid(True)
plt.ylim(-2, 10)

# Show the plot
plt.show()