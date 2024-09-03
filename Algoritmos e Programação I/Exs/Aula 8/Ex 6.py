# Escreva um algoritmo que leia três valores que formam uma data: dia, mês
# e ano. O usuário deverá, então, informar o número de dias que deseja somar
# a esta data. Seu algoritmo deverá apresentar a data calculada.

# Considere que:
# - O usuário sempre informará uma data válida, não sendo necessário fazer
# este teste;
# - Considere que os anos são todos não-bissextos

# Entrada dos dados
dia = int(input("Insira o dia:"))
mes = int(input("Insira o mês:"))
ano = int(input("Insira o ano:"))
data = f"{dia}/{mes}/{ano}"
diasdps = int(input("Insira a quantidade de dias a somar:"))

# Impreção de data e dias a adicionar
print(data, "\nDepois de", diasdps, "dias")

# Soma dos dias por meio de loop while
while diasdps > 0:
    dia, diasdps = dia + 1, diasdps - 1
    # Condicionais para separação dos Mêses por quantidade de dias
    match mes:
        # Quando dia atingir o máximo mês é incrementado em 1
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            if dia > 31:
                dia, mes = 1, mes + 1
        case 4 | 6 | 9 | 11:
            if dia > 30:
                dia, mes = 1, mes + 1
        case 2:
            if dia > 28:
                dia, mes = 1, mes + 1
        case _:
            pass
    # Soma do ano após mês atingir o máximo
    if mes == 13:
        mes, ano = 1, ano + 1
# Formação da nova data
data = f"{dia}/{mes}/{ano}"

# Impreção do resultado
print("Será: ", data)
