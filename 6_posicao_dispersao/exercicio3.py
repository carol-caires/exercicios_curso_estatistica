'''
    Às vezes um dataset pode ter atributos que não são relevantes para utilizar numa predição, pois os valores dele são
    muito homogêneos e não fazem diferença numa classificação. Para remover esses atributos, podemos avaliar a variância
    de cada atributo do dataset e remover os que tiverem uma variância muito baixa.

    Na solução do professor, ele utiliza o MinMaxScaler para normalizar os valores entre 0 e 1
    e facilitar a visualização dos valores. Porém no final, o accuracy score é o mesmo
'''

import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score, KFold
from sklearn.feature_selection import VarianceThreshold

dataset = pd.read_csv('../data/credit_data.csv')
dataset.dropna(inplace=True)  # remove linhas com valores nulos

print(dataset.describe())

X = dataset.iloc[:, 1:4].values
y = dataset.iloc[:, 4].values

selecao = VarianceThreshold(threshold=190)
X_novo = selecao.fit_transform(X)

print(X.shape)
print(X_novo.shape)

kfold = KFold(n_splits=10, shuffle=True)
naive_bayes = GaussianNB()
scores = cross_val_score(naive_bayes, X, y, cv=kfold)

print("score médio SEM remoção de atributos:", scores.mean())

kfold = KFold(n_splits=10, shuffle=True)
naive_bayes = GaussianNB()
scores_novo = cross_val_score(naive_bayes, X_novo, y, cv=kfold)

print("score médio COM remoção de atributos:", scores_novo.mean())