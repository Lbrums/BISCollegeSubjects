# Escreva um programa que pergunte o salário do funcionário,
# calcule e mostre o valor do aumento.
# Para salários maiores que R$ 1100,00 calcule um aumento de 10%.
# Para salários menores ou iguais 15%.

salario = float(input("Insira o valor do salário: "))

if salario > 1100:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

novo_salario = salario + aumento

print(
    f"""
      O aumento será de R${aumento:.2f},
      Valor do novo salário é de R${novo_salario:.2f}.
      """
)
