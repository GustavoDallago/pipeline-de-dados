# Importante a classe Dados

from processamento_dados import Dados

# Definindo os caminhos dos arquivos

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'
path_final = 'data_processed/dados_combinados.csv'

# Key mapping para renomear as colunas do arquivo CSV

key_mapping = {'Nome do Item': 'Nome do Produto',
               'Classificação do Produto': 'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque': 'Quantidade em Estoque',
               'Nome da Loja': 'Filial',
               'Data da Venda': 'Data da Venda'}

# Executando a Pipeline

def main ():
    dados_empresaA = Dados(path_json, 'json')
    dados_empresaB = Dados(path_csv, 'csv')
    dados_empresaB.rename_columns(key_mapping)
    dados_combinados = Dados.join(dados_empresaA, dados_empresaB)
    dados_empresaA.salvar_dados(path_final, dados_combinados)
    
main()