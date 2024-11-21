# Nome: Luciano Brum Silva
# Matrícula: 2024006344
# Turma: BSI24
# Trabalho Final - Análise de Dados Eleitorais

import csv
import statistics

def carregar_dados(caminho):
    """Carrega os dados do arquivo CSV."""
    try:
        with open(caminho, mode='r', encoding='latin-1') as arquivo:
            leitor = csv.reader(arquivo, delimiter=';')
            dados = [linha for linha in leitor]
            return dados
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
        return None

def gerar_relatorio(dados):
    """Gera um relatório inicial com o número de linhas e nomes das colunas."""
    if not dados:
        print("Nenhum dado disponível.")
        return
    print(f"Número de linhas: {len(dados)}")
    print(f"Colunas: {', '.join(dados[0])}")

def filtrar_dados(dados, filtro, valor):
    """Filtra os dados conforme o critério informado."""
    if not dados:
        print("Nenhum dado disponível.")
        return
    colunas = dados[0]
    if filtro not in colunas:
        print("Coluna para filtro não encontrada.")
        return
    indice = colunas.index(filtro)
    filtrados = [linha for linha in dados if linha[indice] == valor]
    return filtrados

def criar_arquivo_filtrado(nome, dados_filtrados):
    """Cria um arquivo com os dados filtrados."""
    if not dados_filtrados:
        print("Nenhum dado para salvar.")
        return
    with open(nome, mode='w', encoding='latin-1') as arquivo:
        escritor = csv.writer(arquivo, delimiter=';')
        escritor.writerows(dados_filtrados)
    print(f"Arquivo '{nome}' criado com sucesso.")

def gerar_resumo(dados, coluna):
    """Gera um resumo agrupado e totalizado para a coluna especificada."""
    if not dados:
        print("Nenhum dado disponível.")
        return
    colunas = dados[0]
    if coluna not in colunas:
        print("Coluna para resumo não encontrada.")
        return
    indice = colunas.index(coluna)
    resumo = {}
    for linha in dados[1:]:
        chave = linha[indice]
        resumo[chave] = resumo.get(chave, 0) + 1
    for chave, total in resumo.items():
        print(f"{chave}: {total}")

def calcular_estatisticas(dados, coluna):
    """Calcula estatísticas (média, moda, desvio padrão) para a coluna especificada."""
    if not dados:
        print("Nenhum dado disponível.")
        return
    colunas = dados[0]
    if coluna not in colunas:
        print("Coluna para estatísticas não encontrada.")
        return
    indice = colunas.index(coluna)
    valores = [int(linha[indice]) for linha in dados[1:] if linha[indice].isdigit()]
    if valores:
        print(f"Média: {statistics.mean(valores)}")
        print(f"Moda: {statistics.mode(valores)}")
        print(f"Desvio Padrão: {statistics.stdev(valores)}")
    else:
        print("Não há valores numéricos na coluna selecionada.")

def buscar_dados(dados, termo):
    """Busca dados no arquivo contendo o termo especificado."""
    if not dados:
        print("Nenhum dado disponível.")
        return
    resultados = [linha for linha in dados if termo in ','.join(linha)]
    print(f"Encontrados {len(resultados)} resultados:")
    for linha in resultados:
        print(', '.join(linha))

def menu_interativo(caminho_csv):
    """Menu interativo para o programa."""
    dados = carregar_dados(caminho_csv)
    if not dados:
        return
    while True:
        print("\nMenu de Opções:")
        print("1. Gerar relatório inicial")
        print("2. Criar arquivo filtrado")
        print("3. Gerar resumo dos dados")
        print("4. Calcular estatísticas")
        print("5. Buscar dados")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            gerar_relatorio(dados)
        elif opcao == '2':
            filtro = input("Informe a coluna para o filtro: ")
            valor = input("Informe o valor para filtrar: ")
            filtrados = filtrar_dados(dados, filtro, valor)
            if filtrados:
                nome_arquivo = input("Informe o nome do arquivo para salvar: ")
                criar_arquivo_filtrado(nome_arquivo, filtrados)
        elif opcao == '3':
            coluna = input("Informe a coluna para gerar o resumo: ")
            gerar_resumo(dados, coluna)
        elif opcao == '4':
            coluna = input("Informe a coluna para calcular estatísticas: ")
            calcular_estatisticas(dados, coluna)
        elif opcao == '5':
            termo = input("Informe o termo para busca: ")
            buscar_dados(dados, termo)
        elif opcao == '6':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Execute o programa
if __name__ == "__main__":
    caminho_arquivo = "bweb_1t_AC_091020241636.csv"  # Substitua pelo caminho do arquivo
    menu_interativo(caminho_arquivo)
