"""
    Enquanto os algoritmos de classificação predizem atributos categóricos, os algoritmos de regressão predizem atributos numéricos

    No caso abaixo, estamos predizendo o preço de um imóvel de acordo com todos os atributos dele.
    O algoritmo busca uma relação de linearidade entre os atributos usados para fazer a predição e o atributo que será predito.

    O ideal é que os atributos usados para as predições possuam correlação de moderada a forte
    com o atributo que será predito (ver como esses cálculos são feitos no exercício 1).

    Conseguimos scores melhores se os dados estiverem em uma distribuição normal. Podemos colocar os dados em
    escala logarítmica para normalizar os dados (y = np.log(y)) e testar se o score melhorou.
"""

import pandas as pd
import math

dataset = pd.read_csv('../data/house_prices.csv')

dataset.drop(labels = ['id', 'date', 'sqft_living15', 'sqft_lot15'], axis = 1, inplace=True)

X = dataset.iloc[:, 1:].values
y = dataset.iloc[:, 0].values

from sklearn.model_selection import train_test_split
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X, y, test_size = 0.2, random_state = 1)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_treinamento, y_treinamento)

print("score base treinamento", regressor.score(X_treinamento, y_treinamento))
print("score base teste", regressor.score(X_teste, y_teste))

previsoes = regressor.predict(X_teste)

from sklearn.metrics import mean_absolute_error, mean_squared_error
print("erro absoluto", mean_absolute_error(y_teste, previsoes))
print("erro quadrado (raiz)", math.sqrt(mean_squared_error(y_teste, previsoes)))

'''
    Seleção de atributos:
    
    Às vezes as predições podem ser melhoradas se selecionarmos os atributos mais relevantes para o algoritmo.
    
    Abaixo temos um exemplo de seleção de atributos usando a técnica de f_regression. 
    Se não houver melhora significativa, podemos testar outras técnicas para ver se melhora.
'''

from sklearn.feature_selection import SelectFdr, f_regression
selecao = SelectFdr(f_regression, alpha = 0.0)
X_novo = selecao.fit_transform(X, y)
colunas = selecao.get_support()
print(dataset.columns[1:17][colunas == True]) # apenas as colunas selecionadas.
# rodar novamente a predição...
