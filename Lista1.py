import numpy as np
import matplotlib.pyplot as plt

def complex_function_1(omega):
    return 3 / (3 + 1j * omega)

def complex_function_2(omega):
    return 5 * (1j * omega) / (3 + 1j * omega)

# Valores de omega
omega = np.linspace(-10, 10, 400)

# Calculando módulo e argumento
z1_values = complex_function_1(omega)
z2_values = complex_function_2(omega)

magnitude_1 = np.abs(z1_values)
phase_1 = np.angle(z1_values)

magnitude_2 = np.abs(z2_values)
phase_2 = np.angle(z2_values)

# Criando os gráficos
fig, ax = plt.subplots(2, 2, figsize=(12, 8))

# Gráfico do módulo de z1
ax[0, 0].plot(omega, magnitude_1, label='|z1(ω)|', color='b')
ax[0, 0].set_title('Módulo de z1(ω)')
ax[0, 0].set_xlabel('ω')
ax[0, 0].set_ylabel('|z1(ω)|')
ax[0, 0].grid(True)
ax[0, 0].legend()

# Gráfico do argumento de z1
ax[0, 1].plot(omega, phase_1, label='arg(z1(ω))', color='r')
ax[0, 1].set_title('Argumento de z1(ω)')
ax[0, 1].set_xlabel('ω')
ax[0, 1].set_ylabel('Fase (radianos)')
ax[0, 1].grid(True)
ax[0, 1].legend()

# Gráfico do módulo de z2
ax[1, 0].plot(omega, magnitude_2, label='|z2(ω)|', color='g')
ax[1, 0].set_title('Módulo de z2(ω)')
ax[1, 0].set_xlabel('ω')
ax[1, 0].set_ylabel('|z2(ω)|')
ax[1, 0].grid(True)
ax[1, 0].legend()

# Gráfico do argumento de z2
ax[1, 1].plot(omega, phase_2, label='arg(z2(ω))', color='m')
ax[1, 1].set_title('Argumento de z2(ω)')
ax[1, 1].set_xlabel('ω')
ax[1, 1].set_ylabel('Fase (radianos)')
ax[1, 1].grid(True)
ax[1, 1].legend()

plt.tight_layout()
plt.show()