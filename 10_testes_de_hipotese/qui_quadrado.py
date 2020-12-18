"""
    Podemos usar o teste de hipoteses qui-quadrado para fazer seleção somente dos atributos estatisticamente relevantes
    de um dataset, aumentando assim a confiabilidade da predição.

    Ver mais em: https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html?highlight=chi2#sklearn.feature_selection.chi2
"""


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectFdr
from sklearn.feature_selection import chi2
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

dataset = pd.read_csv('../data/ad.data', header=None)

X = dataset.iloc[:, 0:1558].values
y = dataset.iloc[:, 1558].values

# predição SEM seleção de atributos
naive1 = GaussianNB()
naive1.fit(X, y)
previsoes1 = naive1.predict(X)
print(accuracy_score(y, previsoes1))

# predição COM seleção qui-quadrado

selecao = SelectFdr(chi2, alpha=0.01)
X_novo = selecao.fit_transform(X, y)

naive2 = GaussianNB()
naive2.fit(X_novo, y)
previsoes2 = naive2.predict(X_novo)
print(accuracy_score(y, previsoes2))