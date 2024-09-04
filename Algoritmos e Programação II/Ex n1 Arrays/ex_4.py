"""
Faça um algoritmo que lê 5 valores para uma variável do tipo vetor e
determine o maior e o menor valor armazenado no vetor.
"""

import numpy as np

vetor = np.zeros(5)
vetormax = 0
for i in range(5):
    vetor[i] = float(input(f"Insira o valor da posição {i}: "))

for i in vetor:
    if i > vetormax:
        vetormax = i

vetormin = vetormax

for i in vetor:
    if i < vetormin:
        vetormin = i

print(f"Valor minimo {vetormin}, Valor máximo {vetormax}")
