"""
Faça um programa que solicite valores inteiros fornecidos pelo usuário até
ele informar o valor 0 (zero). Em seguida, identifique e exiba quantos
números ímpares e os pares foram fornecidos, sem considerar o valor 0.
"""

# Inicialização das listas que serão utilizadas
inpts = []  # Valores fornecidos pelo usuário
pares = []  # Valores que são pares
impares = []  # Valores que são impares

# Loop para inserção de valores pelo usuário
while True:
    valor = int(
        input(
            "Insira um valor diferente de 0 para inserir na lista. 0 encerra o programa.\n..."
        )
    )
    if valor == 0:  # Se o valor inserido for 0, o loop encerra.
        break
    inpts.append(
        valor
    )  # Inserção da variavel valor à lista inpts, por meio da função .append()

# Impressão dos valores inseridos pelo usuário
print(f"Lista: ,{inpts}")

# Separação dos valores em impares e pares.
for i in inpts:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

# Impressão dos valores separados em pares e impares.
print(f"Pares: {pares}\nImpares:{impares}.")
