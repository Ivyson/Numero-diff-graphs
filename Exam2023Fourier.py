import numpy as np
import matplotlib.pyplot as plt
# Define the original function g(t)
def g(t):
    return np.where(t < -2, 0, np.where(t <= 0, 1 + t/2, np.where(t <= 2, 1 - t/2, 0)))
# Define the Fourier Transform G(jω)
def G(omega):
# Handle the case when ω is 0 to avoid division by zero
    return np.where(omega == 0, 2, (2 * np.sin(omega)**2) / omega**2)
# Values for t
t = np.linspace(-3, 3, 400)
# Values for omega
omega = np.linspace(-100, 100, 1000)
# Calculate g(t) and G(jω)
g_values = g(t)
G_values = G(omega)
# Plot g(t)
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
plt.plot(t, g_values, label='g(t)')
plt.title('Original Function $g(t)$')
plt.xlabel('$t$')
plt.ylabel('$g(t)$')
plt.grid(True)
plt.legend()
# Plot G(jω)
plt.subplot(1, 2, 2)
plt.plot(omega, G_values, label='$G(j\\omega)$')
plt.title('Fourier Transform $G(j\\omega)$')
plt.xlabel('$\\omega$')
plt.ylabel('$G(j\\omega)$')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()