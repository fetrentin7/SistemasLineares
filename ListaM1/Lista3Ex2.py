import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

# f(t) = e^(-2t)
def f_t(t):
    return np.where(t >= 0, np.exp(-2 * t), 0)

# h(t) = u(t) - u(t - 1)
def h_t(t):
    return np.where((t >= 0) & (t <= 1), 1, 0)

# vetor de tempo para avaliar as funções
t = np.linspace(-1, 5, 1000)
dt = t[1] - t[0]

# define as funcoes
f_values = f_t(t)
h_values = h_t(t)

# convolução
conv_result = convolve(f_values, h_values, mode='same') * dt
t_conv = t

# Grafico
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(t, f_values, label="f(t) = e^(-2t)u(t)", color="blue")
plt.title("Function f(t)")
plt.grid()
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, h_values, label="h(t) = unit pulse (0 ≤ t ≤ 1)", color="orange")
plt.title("Function h(t)")
plt.grid()
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t_conv, conv_result, label="Convolution f * h", color="red")
plt.title("Convolution of f(t) and h(t)")
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()