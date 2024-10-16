"""
Faça um algoritmo que lê uma matriz M5X5 e 
crie 2 vetores(listas) SL (soma das linhas) e SC (soma das colunas)com 5 posições cada.
Adicionar aos vetores o resultado da soma das linhas e das colunas da matriz,
no final mostrar os dois vetores.
"""

m5x5 = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
]
sl, sc = [0] * 5, [0] * 5

for i in range(5):
    for j in range(5):
        sl[i] = sl[i] + m5x5[i][j]
        sc[j] = sc[j] + m5x5[i][j]

print("soma das colunas", sc)
print("soma das linhas", sl)
