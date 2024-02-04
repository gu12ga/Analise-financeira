import pandas as pd
import json

'''
# Carrega o arquivo CSV
df = pd.read_csv('combustiveis-brasil.csv')

# Converte o DataFrame para um dicionário
data = df.to_dict(orient='records')

# Salva o dicionário em um arquivo JSON
with open('referencia_dos_combustiveis.json', 'w') as f:
    json.dump(data, f, indent=4)
'''
# Leia o arquivo CSV
nome_arquivo_csv = '/home/gustavo/Área de Trabalho/ANALISE/Indicadores_energia/indicadores-continuidade-coletivos-2020-2029.csv'
dados_csv = pd.read_csv(nome_arquivo_csv, delimiter=';', encoding='utf-8')
# Converta para JSON
dados_json = dados_csv.to_json(orient='records', lines=True)

# Salve o JSON em um arquivo
nome_arquivo_json = '/home/gustavo/Área de Trabalho/ANALISE/Indicadores_energia/indicadores-continuidade-coletivos-2020-2029.json'
with open(nome_arquivo_json, 'w') as arquivo_json:
    arquivo_json.write(dados_json)

print(f'Dados convertidos para JSON e salvos em {nome_arquivo_json}')