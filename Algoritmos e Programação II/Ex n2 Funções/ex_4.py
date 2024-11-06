#Escreva um programa que preencha um vetor de inteiros de 10 posições e solicite ao usuário um valor inteiro para ser procurado no vetor. 
#Crie uma função que receba como parâmetro o vetor e o número a ser procurado. 
#Ao final, retorne quantas vezes o número foi encontrado no vetor.

def contar_ocorrencias(vetor, numero):
    # Conta quantas vezes o número aparece no vetor
    contador = 0
    for num in vetor:
        if num == numero:
            contador += 1
    return contador

# Preenchendo o vetor com 10 inteiros fornecidos pelo usuário
vetor = []
for i in range(10):
    valor = int(input(f"Digite o {i+1}º número para o vetor: "))
    vetor.append(valor)

# Solicita o número a ser procurado
numero_procurado = int(input("Digite o número a ser procurado no vetor: "))

# Chama a função para contar as ocorrências
resultado = contar_ocorrencias(vetor, numero_procurado)

# Exibe o resultado
print(f"O número {numero_procurado} foi encontrado {resultado} vez(es) no vetor.")
