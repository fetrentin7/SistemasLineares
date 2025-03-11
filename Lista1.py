import numpy as np
import matplotlib.pyplot as plt

def complex_function(omega):
    return 3 / (3 + 1j * omega)

# Valores de omega
omega = np.linspace(-10, 10, 400)

# Calculando módulo e argumento
z_values = complex_function(omega)
magnitude = np.abs(z_values)
phase = np.angle(z_values)

# Criando os gráficos
fig, ax = plt.subplots(2, 1, figsize=(8, 6))

# Gráfico do módulo
ax[0].plot(omega, magnitude, label='|z1(ω)|', color='b')
ax[0].set_title('Módulo de z1(ω)')
ax[0].set_xlabel('ω')
ax[0].set_ylabel('|z1(ω)|')
ax[0].grid(True)
ax[0].legend()

# Gráfico do argumento
ax[1].plot(omega, phase, label='arg(z1(ω))', color='r')
ax[1].set_title('Argumento de z1(ω)')
ax[1].set_xlabel('ω')
ax[1].set_ylabel('Fase (radianos)')
ax[1].grid(True)
ax[1].legend()

plt.tight_layout()
plt.show()
