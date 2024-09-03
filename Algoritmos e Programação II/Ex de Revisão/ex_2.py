"""
2. A prefeitura de uma cidade fez uma pesquisa com 100 pessoas, coletando
dados sobre o salário e o número de filhos. A prefeitura deseja saber:
a. A média do salário dessas pessoas
a. A média do número de filhos
b. O maior salário
c. A percentagem de pessoas com salários até R$ 1500,00
"""

# Dicionário com a amostra da pesquisa. no formato:
# sample[x] = pessoa
# sample[x][0] = salário, sample[x][1] = filhos
sample = {1: [3000, 2], 2: [6000, 2]}


# Função para obtenção da média dos salarios.
def avgearnings(x):
    earnings = 0  # Variavel local para somatório dos salarios.
    for i in x:  # Loop for para somatório dos salarios.
        earnings += x[i][0]
    avg = earnings / len(x)  # Variavel local da média dos salários
    return avg


# Função para obtenção da média de filhos.
def avgchildrens(x):
    childrens = 0  # Variavel local para somatório do numero de filhos.
    for i in x:  # Loop for para somatório dos filhos
        childrens += x[i][1]
    avg = childrens / len(x)  # Variavel local da média dos filhos
    return avg


# Função para obter o maior salário da amostra.
def biggestwage(x):
    biggestwage = 0  # Variavel local para marcação do maior salário.
    for i in x:  # Loop for para separar o maior salário.
        if x[i][0] > biggestwage:
            biggestwage = x[i][0]
    return biggestwage


# Função para descobrir porcentagem de pessoas com salário até um valor especifico.
def percentwage(x, wage):
    n = 0  # Variavel local para o número de pessoas com o salário dentro do padrão.
    for i in x:  # Loop for para obtenção do número de pessoas com o salario esperado.
        if x[i][0] <= wage:
            n += 1
    return n / len(x) * 100  # Retorna a porcentagem de pessoas.


# Impressão os valores solicitados no enunciado do exercicio
print(
    f"""
    média de salarios: {avgearnings(sample)},
    média de filhos: {avgchildrens(sample)}
    maior salario: {biggestwage(sample)}
    percentagem de salarios até 1500: {percentwage(sample, 1500)}
    """
)
