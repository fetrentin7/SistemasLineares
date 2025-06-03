import matplotlib.pyplot as plt

# Parte (a) corrigida: F(s) = (s+2)/(s^2 + 6s + 25)
# Polos: raízes do denominador: s = -3 ± 4j
poles_a = [-3 + 4j, -3 - 4j]
# Zeros: raiz do numerador: s = -2
zeros_a = [-2]

# Parte (b): F(s) = (s^2 + 9)/(s(s^2 + 3s + 2))
# Zeros: raízes do numerador: s = ±3j
zeros_b = [3j, -3j]
# Polos: s = 0, -1, -2
poles_b = [0, -1, -2]

fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Plot Parte (a)
axs[0].scatter([z.real for z in zeros_a], [z.imag for z in zeros_a], color='blue', marker='o', label='Zeros')
axs[0].scatter([p.real for p in poles_a], [p.imag for p in poles_a], color='red', marker='x', label='Polos')
axs[0].axhline(0, color='black', linewidth=0.5)
axs[0].axvline(0, color='black', linewidth=0.5)
axs[0].set_title('Parte (a): (s+2)/(s²+6s+25)')
axs[0].set_xlabel('R')
axs[0].set_ylabel('Im')
axs[0].grid(True)
axs[0].legend()
axs[0].set_aspect('equal')

# Plot Parte (b)
axs[1].scatter([z.real for z in zeros_b], [z.imag for z in zeros_b], color='blue', marker='o', label='Zeros')
axs[1].scatter([p.real for p in poles_b], [p.imag for p in poles_b], color='red', marker='x', label='Polos')
axs[1].axhline(0, color='black', linewidth=0.5)
axs[1].axvline(0, color='black', linewidth=0.5)
axs[1].set_title('Parte (b): (s²+9)/(s(s²+3s+2))')
axs[1].set_xlabel('R')
axs[1].set_ylabel('Im')
axs[1].grid(True)
axs[1].legend()
axs[1].set_aspect('equal')

plt.tight_layout()
plt.show()
