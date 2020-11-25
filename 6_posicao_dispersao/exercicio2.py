'''

    No primeiro exemplo abaixo, temos a avaliação de algoritmos de machine learning utilizando a técnica de divisão da
    base de dados entre base de treinamento e teste. Porém, existe uma forma mais usada no meio científico, que é a validação cruzada.
    A validação cruzada permite que a base seja dividida em n partes e cada uma dessas partes é usada tanto como
    base de treinamento, quanto como base de testes. Isso aumenta a confiabilidade da predição.
    No segundo exemplo eu uso a técnica de validação cruzada para avaliar os resultados das mesmas predições do primeiro exemplo.
'''

import pandas as pd
import numpy as np
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score, KFold

dataset = pd.read_csv('../data/credit_data.csv')
dataset.dropna(inplace=True)  # remove linhas com valores nulos

X = dataset.iloc[:, 1:4].values
y = dataset.iloc[:, 4].values


def train_test_split_accuracy_evaluation(X, y):
    resultados_naive_bayes = []
    resultados_logistica = []
    resultados_forest = []
    for i in range(30):
      X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X, y, test_size = 0.2,
                                                                        stratify = y, random_state = i)
      naive_bayes = GaussianNB()
      naive_bayes.fit(X_treinamento, y_treinamento)
      resultados_naive_bayes.append(accuracy_score(y_teste, naive_bayes.predict(X_teste)))

      logistica = LogisticRegression()
      logistica.fit(X_treinamento, y_treinamento)
      resultados_logistica.append(accuracy_score(y_teste, logistica.predict(X_teste)))

      random_forest = RandomForestClassifier()
      random_forest.fit(X_treinamento, y_treinamento)
      resultados_forest.append(accuracy_score(y_teste, random_forest.predict(X_teste)))

    return np.array(resultados_naive_bayes), np.array(resultados_logistica), np.array(resultados_forest)

def cross_validation_accuracy_evaluation(X, y):
    resultados_naive_bayes_cv = []
    resultados_logistica_cv = []
    resultados_forest_cv = []
    for i in range(30):
        kfold = KFold(n_splits=10, shuffle=True, random_state=i)

        naive_bayes = GaussianNB()
        scores = cross_val_score(naive_bayes, X, y, cv=kfold)
        resultados_naive_bayes_cv.append(scores.mean())

        logistica = LogisticRegression()
        scores = cross_val_score(logistica, X, y, cv=kfold)
        resultados_logistica_cv.append(scores.mean())

        random_forest = RandomForestClassifier()
        scores = cross_val_score(random_forest, X, y, cv=kfold)
        resultados_forest_cv.append(scores.mean())

    return np.array(resultados_naive_bayes_cv), np.array(resultados_logistica_cv), np.array(resultados_forest_cv)


print("Exemplo 1: Divisão Manual da Base de Dados\n\n")

resultados_naive_bayes, resultados_logistica, resultados_forest = train_test_split_accuracy_evaluation(X, y)
np.set_printoptions(suppress=True)
print("Média: NB: %f, R. Logística: %f, R. Forest: %f" %(resultados_naive_bayes.mean(), resultados_logistica.mean(), resultados_forest.mean()))
print("Moda: NB: %s, R. Logística: %s, R. Forest: %s" %(stats.mode(resultados_naive_bayes), stats.mode(resultados_logistica), stats.mode(resultados_forest)))
print("Mediana: NB: %f, R. Logística: %f, R. Forest: %f" %(np.median(resultados_naive_bayes), np.median(resultados_logistica), np.median(resultados_forest)))
print("Variância: NB: %f, R. Logística: %f, R. Forest: %f" %(np.var(resultados_naive_bayes), np.var(resultados_logistica), np.var(resultados_forest)))
print("Desvio Padrão: NB: %f, R. Logística: %f, R. Forest: %f" %(np.std(resultados_naive_bayes), np.std(resultados_logistica), np.std(resultados_forest)))
print("Coef. Variação: NB: %f, R. Logística: %f, R. Forest: %f" %(stats.variation(resultados_naive_bayes) * 100, stats.variation(resultados_logistica) * 100, stats.variation(resultados_forest) * 100))

# --------------------------------------------------

print("\n\nExemplo 2: Cross Validation\n\n")

resultados_naive_bayes_cv, resultados_logistica_cv, resultados_forest_cv = cross_validation_accuracy_evaluation(X, y)
print("Média: NB: %f, R. Logística: %f, R. Forest: %f" %(resultados_naive_bayes_cv.mean(), resultados_logistica_cv.mean(), resultados_forest_cv.mean()))
print("Moda: NB: %s, R. Logística: %s, R. Forest: %s" %(stats.mode(resultados_naive_bayes_cv), stats.mode(resultados_logistica_cv), stats.mode(resultados_forest_cv)))
print("Mediana: NB: %f, R. Logística: %f, R. Forest: %f" %(np.median(resultados_naive_bayes_cv), np.median(resultados_logistica_cv), np.median(resultados_forest_cv)))
print("Variância: NB: %f, R. Logística: %f, R. Forest: %f" %(np.var(resultados_naive_bayes_cv), np.var(resultados_logistica_cv), np.var(resultados_forest_cv)))
print("Desvio Padrão: NB: %f, R. Logística: %f, R. Forest: %f" %(np.std(resultados_naive_bayes_cv), np.std(resultados_logistica_cv), np.std(resultados_forest_cv)))
print("Coef. Variação: NB: %f, R. Logística: %f, R. Forest: %f" %(stats.variation(resultados_naive_bayes_cv) * 100, stats.variation(resultados_logistica_cv) * 100, stats.variation(resultados_forest_cv) * 100))