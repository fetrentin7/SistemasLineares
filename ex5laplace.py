import sympy as sp
import numpy as np
from matplotlib import pyplot as plt

# Definindo as variáveis simbólicas
t, s = sp.symbols('t s')
Y = sp.Function('Y')

# Expressão da transformada de Laplace da solução encontrada:
# y(t) = (1 - cos(sqrt(2)t) - sqrt(2) * sin(sqrt(2)t)) * u(t)
sqrt2 = sp.sqrt(2)
y_t = (1 - sp.cos(sqrt2 * t) - sqrt2 * sp.sin(sqrt2 * t))

# Convertendo para função numérica
y_func = sp.lambdify(t, y_t, modules=['numpy'])

# Valores de tempo para o gráfico
t_vals = np.linspace(0, 10, 400)
y_vals = y_func(t_vals)

# Plotando a resposta y(t)
plt.figure(figsize=(8, 5))
plt.plot(t_vals, y_vals, label=r'$y(t)$', color='blue')
plt.title(r"Solução da EDO da Questão 5(a): $y(t) = 1 - \ cos(\sqrt{2}t) - \sqrt{2}\sin(\sqrt{2}t)$")
plt.xlabel("Tempo (t)")
plt.ylabel("y(t)")
plt.grid(True)
plt.legend()
plt.show()
