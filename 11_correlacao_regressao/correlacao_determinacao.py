"""
    Podemos descobrir se duas variáveis são correlacionadas (positivamente ou negativamente) ou não fazendo os cálculos
    de covariância. Assim descobrimos os seguintes valores:

    Covariância: se maior que zero, as variáveis se movem juntas, se menor que zero, se movem em direções opostas e se
    igual a zero, as variáveis são independentes.

    Coeficiente de correlação: quanto mais próximo de 1 ou -1, mais forte é a correlação.

    Coeficiente de determinação: o quanto os valores da variável dependente conseguem ser explicados pelas variáveis explanatórias
"""

import numpy as np
import pandas as pd
import math

''' Cálculo manual '''

tamanho = np.array([30, 39, 49, 60])
preco = np.array([57000, 69000, 77000, 90000])

# se criarmos um gráfico de pontos do tamanho versus o preço, iremos notar que há uma relação linear entre as variáveis
# sns.scatterplot(tamanho, preco);

dataset = pd.DataFrame({'tamanho': tamanho, 'preco': preco})

media_tamanho = dataset['tamanho'].mean()
media_preco = dataset['preco'].mean()

dp_tamanho = dataset['tamanho'].std()
dp_preco = dataset['preco'].std()

dataset['dif'] = (dataset['tamanho'] - media_tamanho) * (dataset['preco'] - media_preco)

soma_dif = dataset['dif'].sum()

covariancia = soma_dif / (len(dataset) - 1)
print("Covariância:", covariancia)

coeficiente_correlacao = covariancia / (dp_tamanho * dp_preco)
print("Coeficiente de correlação:", coeficiente_correlacao)

coeficiente_determinacao = math.pow(coeficiente_correlacao, 2)
print("Coeficiente de determinação:", coeficiente_correlacao)

''' Pandas e Numpy '''

np.cov(tamanho, preco)
np.corrcoef(tamanho, preco)

dataset.cov()
dataset.corr()