import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dataset = pd.read_csv('../data/census.csv')

dados = pd.DataFrame({'dados': dataset['age']})

dados.plot.hist(); # histograma simples

'''
    rodando essa função mais de uma vez no console, pode-se sobrepor mais de um gráfico.
    Por exemplo: Rodar sem o parâmetro `bins` traz um gráfico com uma quantidade grande de 
    colunas. Com o bins = 5 logo em seguida, por exemplo, você pode sobrepor colunas mais
    grossas e visualizar melhor quais frequências ocorrem mais.
'''
sns.distplot(dados, hist = True, kde = True, bins = 5); # histograma com linha de curva
