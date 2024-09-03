# Crie um algoritmo que leia um número inteiro,
# verifique e mostre se o número lido é positivo ou negativo.

x = int(input("Insira um número Inteiro: "))

if x != 0:
    if x > 0:
        print(f"{x} é positivo.")
    else:
        print(f"{x} é negativo.")
else:
    print(f"{x} é um numero neutro")
