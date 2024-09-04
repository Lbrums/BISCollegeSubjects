"""
Faça um algoritmo que lê 5 valores para uma variável do tipo vetor e
determine a média de todos os valores armazenados no vetor.
"""

import numpy as np

vetor = np.zeros(5)

for i in range(5):
    vetor[i] = float(input(f"Insira o valor da posição {i}: "))

soma = 0
for i in vetor:
    soma += i

media = soma / len(vetor)

print(f"Média do vetor é {media}")
