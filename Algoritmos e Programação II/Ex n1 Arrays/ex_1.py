"""
Faça um algoritmo que lê 10 valores para uma variável do tipo vetor de nome x
e mostra os 10 valores armazenados na estrutura.
"""

import numpy as np

x = np.zeros(10)

for i in range(10):
    x[i] = float(input(f"Insira o valor da posição {i}: "))

print(x)
