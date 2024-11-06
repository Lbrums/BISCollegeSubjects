# Escreva um algoritmo que imprima todos os números inteiros de 10 a 1 (em ordem decrescente), utilizando recursividade.
def imprimir_decrescente(n):
    if n < 1:  # Condição de parada: quando n for menor que 1, a recursão para
        return
    print(n)  # Imprime o valor atual de n
    imprimir_decrescente(n - 1)  # Chama a função recursivamente com n - 1

# Chama a função para imprimir os números de 10 a 1
imprimir_decrescente(10)