"""
Faça um programa que leia o nome do usuário e o imprima na vertical, em
forma de escada, usando apenas letras maiúsculas.
Exemplo: Nome = RAFAEL
Resultado gerado pelo programa:
R
RA
RAF
RAFA
RAFAE
RAFAEL
"""

# Input do nome de usuário
word = str(input("")).upper()

# Loop for para impressão do nome por linha sendo que
# a linha 1 tera 1 letra, linha 2 tera 2 letras assim por diante até a palavra completa.
for i in range(1, len(word) + 1):
    print(word[:i])
