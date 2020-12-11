"""
    É possível, ao utilizar qualquer algoritmo de Machine Learning, passar um registro específico para aquele modelo
    e ele te responder qual é a probabilidade de ser classificado como cada um dos valores possíveis.

    Isso é especialmente útil, caso você precise ter uma confiabilidade alta nas predições, pois é possível rejeitar
    registros com uma porcentagem baixa de confiabilidade.
"""

import pandas as pd
import numpy as np

dataset = pd.read_csv('../data/credit_data.csv')
dataset.dropna(inplace=True)

X = dataset.iloc[:, 1:4].values
y = dataset.iloc[:, 4].values

from sklearn.naive_bayes import GaussianNB

naive_bayes = GaussianNB()
naive_bayes.fit(X, y)

novo = X[0].reshape(1, -1)  # necessário mudar para o formato de matrix -> 1 linha e 3 colunas

naive_bayes.predict(novo)
previsao = naive_bayes.predict_proba(novo)
print("Probabilidade de ser classificado como qualquer uma das classes possíveis:", previsao)

print("Classe mais próvável:", np.argmax(previsao))
