"""
Faça um algoritmo que lê 10 valores para uma variável do tipo vetor e
mostre qual a posição está armazenado o maior e o menor valor no vetor.
"""

import numpy as np

vetor = np.zeros(10)
vetormax = 0
for i in range(10):
    vetor[i] = float(input(f"Insira o valor da posição {i}: "))

for i in vetor:
    if i > vetormax:
        vetormax = i

vetormin = vetormax

for i in vetor:
    if i < vetormin:
        vetormin = i

for i in range(10):
    if vetor[i] == vetormin:
        print(f"Posição do menor valor é {i}")

for i in range(10):
    if vetor[i] == vetormax:
        print(f"Posição do maior valor é {i}")
