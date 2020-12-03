'''
    Você pode usar o algoritmo KNN para fazer predições, porém nem sempre o accuracy score será muito alto, pois as bases
    de treinamento e teste são muito diferentes entre si. Para resolver esse problema e melhorar a taxa de acerto,
    podemos padronizar os atributos previsores para que esles estejam na mesma escala e, consequentemente, melhorar a
    qualidade da predição.
'''

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv('../data/credit_data.csv')
dataset.dropna(inplace=True)

X = dataset.iloc[:, 1:4].values
y = dataset['c#default'].values

X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X, y, test_size = 0.2,
                                                                  stratify = y)

knn = KNeighborsClassifier()
knn.fit(X_treinamento, y_treinamento)

previsoes = knn.predict(X_teste)

print("Accuracy score SEM padronização:", accuracy_score(y_teste, previsoes))

z_score_treinamento = StandardScaler()
z_score_teste = StandardScaler()

X_treinamento_p = z_score_treinamento.fit_transform(X_treinamento)
X_teste_p = z_score_teste.fit_transform(X_teste)

knn = KNeighborsClassifier()
knn.fit(X_treinamento_p, y_treinamento)
previsoes = knn.predict(X_teste_p)

print("Accuracy score COM padronização:", accuracy_score(y_teste, previsoes))