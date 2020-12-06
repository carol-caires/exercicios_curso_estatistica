'''
    Como normalmente o algoritmo de regressão linear faça melhores predições baseado em dados com distribuição normal,
    pode valer a pena normalizar os parâmetros efetuando o logaritmo do valor deles.
    No exemplo com tratamento de dados, alteramos o X e o y afim de colocar ambos em uma distribuição normal e melhorar
    o score da predição. Nesse caso, os resultados foram baixos, pois estamos baseando a predição em apenas 1 parâmetro.
    Mas a ideia é testar o mesmo conceito com mais parâmetros e escolher a melhor técnica.
'''


import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

dataset = pd.read_csv('../data/house_prices.csv')

# Regressão linear SEM tratamento de dados
X = dataset['sqft_living'].values
X = X.reshape(-1, 1)  # transformar em matriz

y = dataset['price'].values
regressor = LinearRegression()
regressor.fit(X, y)

previsoes = regressor.predict(X)

print("Score da previsão SEM tratamento dos dados: %s " % r2_score(y, previsoes))

# Regressão linear COM tratamento de dados

# transforma a distribução dos atributos em distribuição normal
X_novo = np.log(X)
y_novo = np.log(y)

regressor = LinearRegression()
regressor.fit(X_novo, y_novo)
previsoes = regressor.predict(X_novo)

print("Score da previsão COM tratamento dos dados: %s " % r2_score(y_novo, previsoes))
