# Construa uma função que receba como parâmetro uma matriz quadrada 4 X 4 e retorne a soma dos valores da diagonal principal.
def soma_diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][i]  # Soma os elementos A[i, i] da diagonal principal
    return soma