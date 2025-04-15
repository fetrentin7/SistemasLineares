import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

# Vetor de tempo
t = np.linspace(-5, 5, 1000)
dt = t[1] - t[0]

# f(t) = e^(-2t) * u(t)
def f_t(t):
    return np.where(t >= 0, np.exp(-2 * t), 0)

# h(t) = u(t + 1)
def h_t(t):
    return np.where(t >= -1, 1, 0)

# Avaliando as funções
f_values = f_t(t)
h_values = h_t(t)

# Convolução
conv_result = convolve(f_values, h_values, mode='same') * dt

# Eixo de tempo da convolução
t_conv = np.linspace(-5, 5, len(conv_result))

# Plotagem
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(t, f_values, label="f(t) = $e^{-2t}u(t)$", color="blue")
plt.title("Função f(t)")
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, h_values, label="h(t) = $u(t+1)$", color="green")
plt.title("Função h(t)")
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t_conv, conv_result, label="f * h", color="red")
plt.title("Convolução f(t) * h(t)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
