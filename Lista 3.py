import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

# Define the corrected f(x) which is 2 for 0 < x <= 2
def f_x(x):
    return np.where((0 < x) & (x <= 2), 2, 0)

# Define g(x) with a ramp and a constant value
def g_x(x):
    ramp = np.where((x >= 0) & (x <= 1), x, 0)  # Linear ramp from 0 to 1
    constant = np.where((x > 1) & (x <= 2), 1, 0)  # Constant 1 from 1 to 2
    return ramp + constant

# Define the range
t = np.linspace(-5, 5, 500)  # Time range
dt = t[1] - t[0]  # Time step

# Compute the functions
f_values = f_x(t)
g_values = g_x(t)

# Compute convolution
conv_result = convolve(f_values, g_values, mode='same') * dt

# Create a new time axis for convolution result
t_conv = np.linspace(-5, 5, len(conv_result))

# Plot the functions and convolution result
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(t, f_values, label="f(x) - Rectangular (0 < x <= 2, Value = 2)", color="blue")
plt.title("Function f(x)")
plt.grid()
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, g_values, label="g(x) - Ramp + Constant", color="orange")
plt.title("Function g(x)")
plt.grid()
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t_conv, conv_result, label="Convolution f * g", color="red")
plt.title("Convolution of f(x) and g(x)")
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()