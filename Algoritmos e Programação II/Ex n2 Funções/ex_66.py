# Escreva um algoritmo que leia um valor para X e uma sub-rotina que imprima todos os números ímpares do intervalo fechado de 1 a X.
def imprimir_impares(X):
    # Percorre o intervalo de 1 até X
    for i in range(1, X + 1):  # O intervalo é fechado, então vai de 1 até X (inclusive)
        if i % 2 != 0:  # Verifica se o número é ímpar
            print(i)

# Leitura do valor de X
X = int(input("Digite um valor para X: "))

# Chama a sub-rotina para imprimir os números ímpares no intervalo de 1 até X
imprimir_impares(X)