import numpy as np
import json
import statsmodels.api as sm
import pandas as pd
import scipy.stats

class Alg:
    def __init__(self):
        
        self.acao = self.preencher("/home/gustavo/Área de Trabalho/ANALISE/acoes6/equatorial.json")
        self.acaoData = self.preencherData2("/home/gustavo/Área de Trabalho/ANALISE/acoes6/equatorial.json")
        #self.dolar = self.preencher2("/home/gustavo/Área de Trabalho/ANALISE/indicadores6/dolar.json")
        
        '''
        aux = []
        
        for i in range(9169, len(self.acao)):
            aux.append(self.acao[i][:])
        
        self.acao = aux[:]
        
        self.acao = [float(valor) for valor in self.acao]
        
        print(len(self.acao))
        print(len(self.dolar))
        
        
        print(len(self.acao))
        print(len(self.dolar))
        
        for i in range(0, len(self.acao)):
            
            if(self.acao[i] != self.dolar[i]):
                print(f'Selic: {self.acao[i]}')
                print(f'Petrobras: {self.dolar[i]}')
                print()
            
        '''
        #self.ibovespa = self.preencher2("/home/gustavo/Área de Trabalho/ANALISE/indicadores6/ibovespa.json")
        #self.combustiveis = self.preencher('referencia_dos_combustiveis.json')
        
        
    
    def preencherSelic(self, caminho):
        
        lista = []
        
        with open(caminho, 'r') as arquivo_json:
            dados = json.load(arquivo_json)        

        for dado in dados:
            lista.append(dado["valor"])
        
        return lista
    
    def preencher(self, caminho):
        
        lista = []
        
        with open(caminho, 'r') as arquivo_json:
            dados = json.load(arquivo_json)        

        for dado in dados:
            lista.append(dado["Adj Close"])
        
        return lista
     
    def preencherData(self, caminho):
        
        lista = []
        
        with open(caminho, 'r') as arquivo_json:
            dados = json.load(arquivo_json)        

        for dado in dados:
            lista.append(dado["data"])
        
        return lista

    def preencher2(self, caminho):
        
        lista = []
        
        with open(caminho, 'r') as arquivo_json:
            dados = json.load(arquivo_json)        

        for i in range(0, len(self.acao)):
            lista.append(dados[i]["Adj Close"])
        
        return lista
    
    def preencherData2(self, caminho):
        
        lista = []
        
        with open(caminho, 'r') as arquivo_json:
            dados = json.load(arquivo_json)        

        for i in range(0, len(self.acao)):
            lista.append(dados[i]["Date"])
        
        return lista

    def calcular_correlacao_pearson(self, x, y):
        # Calcular as médias
        media_x = np.mean(x)
        media_y = np.mean(y)
        
        # Calcular o numerador e o denominador da fórmula do coeficiente de correlação de Pearson
        numerador = np.sum((x - media_x) * (y - media_y))
        denominador = np.sqrt(np.sum((x - media_x)**2) * np.sum((y - media_y)**2))
        
        # Calcular o coeficiente de correlação
        if denominador != 0:
            r = numerador / denominador
            return r
        else:
            # Se o denominador for zero, a correlação é indefinida
            return "Correlação indefinida (divisão por zero)."
    
    def teste_pearson(self):
        
        #print(f'Dolar ultimo: {self.dolar[len(self.dolar)-1]}. {len(self.dolar)}')
        #print(f'acao ultimo: {self.acao[len(self.acao)-1]}. {len(self.acao)}')
        
        print(f'Dolar: {self.calcular_correlacao_pearson(self.dolar, self.acao)}')
        print(f'Ibovespa: {self.calcular_correlacao_pearson(self.ibovespa, self.acao)}')
    
    def correlacao(self):
        correlation_coefficient, p_value = scipy.stats.spearmanr(self.acao, self.ibovespa)
        print(f'Ação-Ibovespa Spearman: {correlation_coefficient}, {p_value}')
        correlation_coefficient2, p_value2 = scipy.stats.spearmanr(self.acao, self.dolar)
        print(f'Ação-Dolar Spearmanr: {correlation_coefficient2}, {p_value2}')
        kendall_corr, kendall_p_value = scipy.stats.spearmanr(self.acao, self.ibovespa)
        print(f'Ação-Ibovespa Kendal: {kendall_corr}, {kendall_p_value}')
        kendall_corr2, kendall_p_value2 = scipy.stats.kendalltau(self.acao, self.dolar)
        print(f'Ação-Dolar Kendall: {kendall_corr2}, Valor_p: {kendall_p_value2}')
    
    def maior_menor(self):
        
        maior = 0
        maiorData = ""
        menor = -1
        menorData = ""
        aux = True
        
        for i in range(0, len(self.acao)):
            if(aux):
                menor = self.acao[i]
                menorData = self.acaoData[i]
                aux = False
            if(self.acao[i] > maior):
                maior = self.acao[i]
                maiorData = self.acaoData[i]
            if(self.acao[i] < menor):
                menor = self.acao[i]
                menorData = self.acaoData[i]
            

        print(f'Maior: {maior}, Data: {maiorData}')
        print(f'Menor: {menor}, Data: {menorData}')
    
    def regressao_simples(self):
        data = {'Y': self.ibovespa, 'X': self.acao}
        df = pd.DataFrame(data)

        # Adicionar uma constante ao conjunto de dados e termos polinomiais
        X = sm.add_constant(df['X'])
        X['X^2'] = df['X'] ** 2

        # Ajustar o modelo de regressão linear simples
        modelo = sm.OLS(df['Y'], X).fit()

        # Imprimir o resumo do modelo
        print(modelo.summary())   

alg = Alg()
#alg.teste_pearson()
#alg.regressao_simples()
#alg.correlacao()
alg.maior_menor()