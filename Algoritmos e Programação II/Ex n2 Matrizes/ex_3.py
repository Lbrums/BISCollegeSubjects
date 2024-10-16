"""
Faça um algoritmo que lê valores para uma matriz M4X4 e um valor para a variável “a” 
(do tipo simples, pode ser: inteiro, float). 
Multiplicar cada valor contido na matriz pelo valor da variável e colocar os resultados num vetor(lista) V com 16 elementos. 
Mostre no final o vetor(lista).
"""

m4x4 = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
]
a = 2
results = []

for i in range(4):
    for j in range(4):
        results.append(m4x4[i][j] * a)

print(results)
