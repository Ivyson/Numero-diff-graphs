import numpy as np
import matplotlib.pyplot as plt

# Define the function f(t)
def f(t):
    return (2 + np.pi) / 4 + np.sum((((-1)**n - 1) / (np.pi * n**2)) * np.cos(n * t) for n in range(1, 101)) + np.sum((((1 - np.pi) * (-1)**n - 1) / (np.pi * n)) * np.sin(n * t) for n in range(1, 101))

# Create time values for plotting
t_values = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Evaluate f(t)
f_values = [f(t) for t in t_values]

# Plot f(t)
plt.figure(figsize=(8, 4))
plt.plot(t_values, f_values, label='$f(t)$')
plt.xlabel('$t$')
plt.ylabel('Function Value')
plt.title('Fourier Expansion of $f(t)$')
plt.grid(True)
plt.show()
