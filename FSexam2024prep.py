import numpy as np
import matplotlib.pyplot as plt
import time

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

# Measure the time taken for a smaller number of terms
small_num_terms = 100
start_time = time.time()
f_fourier_small = fourier_series(t, small_num_terms)
end_time = time.time()

time_taken_small = end_time - start_time
print(f"Time taken for {small_num_terms} terms: {time_taken_small:.4f} seconds")

# Estimate the time for 10 million terms
estimated_time = (time_taken_small / small_num_terms) * 10000000
print(f"Estimated time for 10 million terms: {estimated_time / 3600:.2f} hours")

# Plot the piecewise function
plt.plot(t, f_piecewise, label="Piecewise function f(t)")

# Plot the Fourier series approximation for small number of terms
plt.plot(t, f_fourier_small, label=f"Fourier series (first {small_num_terms} terms)", linestyle='--')

# Add labels and title
plt.title("Piecewise Function and Its Fourier Series Approximation")
plt.xlabel("t")
plt.ylabel("f(t)")
plt.legend()
plt.grid(True)
plt.ylim(-2, 10)

# Show the plot
plt.show()
