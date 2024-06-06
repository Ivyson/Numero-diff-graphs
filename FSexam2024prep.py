import numpy as np
import matplotlib.pyplot as plt

# Define the function f(t)
def f(t):
    if -np.pi < t < 0:
        return 1
    elif 0 < t < np.pi:
        return t
    else:
        return 0

# Define the Fourier expansion terms
def fourier_expansion(t, num_terms=100):
    result = (2 + np.pi) / 4  # Constant term
    for n in range(1, num_terms + 1):
        cos_term = ((-1)**(n - 1)) / (np.pi * n**2) * np.cos(n * t)
        sin_term = (((1 - np.pi) * (-1)**(n - 1)) / (np.pi * n)) * np.sin(n * t)
        result += cos_term + sin_term
    return result

# Create time values for plotting
t_values = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Evaluate f(t) and its Fourier expansion
f_values = [f(t) for t in t_values]
expansion_values = [fourier_expansion(t) for t in t_values]

# Plot f(t) and its Fourier expansion
plt.figure(figsize=(10, 4))
plt.plot(t_values, f_values, label='$f(t)$')
plt.plot(t_values, expansion_values, label='Fourier Expansion')
plt.xlabel('$t$')
plt.ylabel('Function Value')
plt.title('Fourier Expansion of $f(t)$')
plt.legend()
plt.grid(True)
plt.show()
