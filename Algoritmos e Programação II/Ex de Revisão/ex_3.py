"""
Faça um programa que leia o nome do usuário e mostre o nome de trás
para frente, utilizando somente letras maiúsculas.
"""

# Solicitação do nome do usuário e o converçãp para letras maiúsculas
word = input("Insira o nme de usuário: ").upper()

# Impressão invertida do nome de usuário
print(word[::-1])
