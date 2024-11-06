# Faça uma função que inverte uma matriz 10 x 10 (linhas viram colunas e colunas viram linhas).

def inverter_matriz(matriz):
    matriz_invertida = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
    return matriz_invertida
