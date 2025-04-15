import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

#2 para 0 < x <= 2
def f_x(x):
    return np.where((0 < x) & (x <= 2), 2, 0)

# Define g(x)
def g_x(x):
    ramp = np.where((x >= 0) & (x <= 1), x, 0)  # Linear ramp from 0 to 1
    constant = np.where((x > 1) & (x <= 2), 1, 0)  # Constant 1 from 1 to 2
    return ramp + constant

# Define the range
t = np.linspace(-5, 5, 500)  # Time range
dt = t[1] - t[0]  # Time step

# funções
f_values = f_x(t)
g_values = g_x(t)

# Convolução
conv_result = convolve(f_values, g_values, mode='same') * dt

# eixo de tempo
t_conv = np.linspace(-5, 5, len(conv_result))

# funções
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