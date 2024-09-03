# Faça um programa que leia o nome de um aluno e duas notas,
# calcule e mostre a média ponderada dessas notas,
# considerando peso 2 para a primeira nota e peso 3 para a segunda nota.

nome = input("Insira seu nome: ")
nota1 = float(input("Insira a primeira nota: ")) * 2
nota2 = float(input("Insira a segunda nota:")) * 3
mediap = (nota1 + nota2) / 5
print(f"{mediap:.0f}")
