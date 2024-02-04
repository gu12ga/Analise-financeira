from pandas_datareader import data as pdr
import yfinance as yfin

#MAGAZINE LUIZA: MGLU3.SA
#IBOVESPA: ^BVSP
#Dolar: USDBRL=X
#Arezzo: ARZZ3.SA
#Gol linhas areas: GOL
#Petroleo Cru: CL=F

#Ações de predução de energia
# fonte: https://inteligenciafinanceira.com.br/mercado-financeiro/acoes/as-melhores-acoes-de-energia-para-investir-ainda-em-2023-segundo-especialistas/
#Alupar: ALUP11.SA
#Equatorial: EQTL3.SA
#Petrobras: PETR4.SA
#CTTEP: TRPL4.SA
#Transmissora Aliança: TAEE11.SA
#AES Brasil: AESB3.SA
#Auren Energia: AURE3.SA
#Empresa Metropolitana de Águas e Energia: EMAE4.SA

#Ações de mineração
#Vale: VALE3.SA
#CSN Mineração: CMIN3.SA
#Aura Minerals Inc.: AURA33.SA
#MMX Mineração e Metálicos: MMXM11.SA

'''
yfin.pdr_override()

spy = pdr.get_data_yahoo('EQTL3.SA', start='2018-01-01', end='2018-12-31')
#spy = yfin.download("^BVSP", period="1mo")

#Coletar dados mensais

#
msft = yfin.Ticker("MSFT")
spy = msft.history(period="1mo")
spy = spy.resample('M').mean()
#

# Converter o DataFrame para um formato de lista de dicionários
data_list = spy.reset_index().to_dict(orient='records')


# Defina o nome do arquivo JSON
nome_arquivo_json = '/home/gustavo/Área de Trabalho/ANALISE/acoes6/equatorial.json'

# Salve os dados no formato desejado em um arquivo JSON
with open(nome_arquivo_json, 'w') as json_file:
    json_file.write('[')
    for i, record in enumerate(data_list):
        json_file.write('{' + ', '.join(f'"{key}": {value}' if key != 'Date' else f'"{key}": \"{value}\"'
                                      for key, value in record.items()) + '}')
        if i < len(data_list) - 1:
            json_file.write(', ')
    json_file.write(']')

print(f'Dados do spy foram salvos em "{nome_arquivo_json}" no formato desejado.')
'''
import urllib
url = 'https://dadosabertos.aneel.gov.br/pt_BR/api/3/action/datastore_search?resource_id=4493985c-baea-429c-9df5-3030422c71d7&limit=5&q=title:jones'  
fileobj = urllib.request.urlopen(url)
print(fileobj.read())