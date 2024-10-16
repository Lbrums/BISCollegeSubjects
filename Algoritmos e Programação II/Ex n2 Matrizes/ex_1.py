"""
Faça um algoritmo que receba um valor N correspondente ao tamanho de duas matrizes quadradas de ordem N (MNxN). 
Leia os valores inteiros para preencher todas as posições de cada uma das matrizes,
e calcule a SOMA das matrizes.
"""

size_n = int(input("Insira o tamanho da matriz (x)²: "))

mtrz_1 = []
for i in range(size_n):
    linha = []
    for j in range(size_n):
        valor = int(input(f"Insira o valor da matriz 1 coluna {i} posição {j}: "))
        linha.append(valor)
    mtrz_1.append(linha)

mtrz_2 = []
for i in range(size_n):
    linha = []
    for j in range(size_n):
        valor = int(input(f"Insira o valor da matriz 2 coluna {i} posição {j}: "))
        linha.append(valor)
    mtrz_2.append(linha)

mtrz_sum = []
for i in range(size_n):
    linha = []
    for j in range(size_n):
        linha.append(mtrz_1[i][j] + mtrz_2[i][j])
    mtrz_sum.append(linha)

print(mtrz_1)
print("\n+\n")
print(mtrz_2)
print("\n=\n")
print(mtrz_sum)
