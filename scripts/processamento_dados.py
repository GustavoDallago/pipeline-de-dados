import json
import csv
import pandas as pd

class Dados:
    
    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados
        self.dados = self.leitura_dados()
        self.nome_colunas = self.get_columns()
        
    def arquivo_json(self):
        dados_json = []
        with open(self.path, 'r') as file:
            dados_json = json.load(file)
        return dados_json
        
    def arquivo_csv(self):
        dados_csv = []
        with open(self.path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
        return dados_csv

    def leitura_dados(self):
        dados = [] 
        if self.tipo_dados == 'json':
            dados = self.arquivo_json()
        elif self.tipo_dados == 'csv':
            dados = self.arquivo_csv()
        return dados
    
    def get_columns(self):
        return list(self.dados[-1].keys())
    
    def rename_columns(self, key_mapping):
        new_dados = []
        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_dados.append(dict_temp)
        self.dados = new_dados
        self.nome_colunas = self.get_columns()
        
    @staticmethod
    def join(dadosA, dadosB):
        df_a = pd.DataFrame(dadosA.dados)
        df_b = pd.DataFrame(dadosB.dados)
        
        df_combinado = pd.concat([df_a, df_b], ignore_index=True)
        df_final = df_combinado.fillna('Indisponível')
        
        nome_colunas = list(df_final.columns)
        dados_lista = df_final.values.tolist()
        
        return [nome_colunas] + dados_lista
    
    def salvar_dados(self, path, dados_combinados):
        with open(path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinados)
        print(f"Sucesso! Arquivo salvo em: {path}")