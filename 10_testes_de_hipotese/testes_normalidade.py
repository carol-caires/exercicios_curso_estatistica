"""
    Alguns tipos de teste de hipótese podem nos dizer se os dados seguem uma distribuição normal ou não.
    Abaixo, faço a predição de atributo usando 3 algoritmos de classificação diferentes (Naive-Bayes, Regressão Logística e Random Forest)
    e usamos os testes de hipótese de Shapiro-Wilk, D'Agostinho e Anderson-Darling para verificar se os scores obtidos
    das predições seguem uma distribuição normal.
"""

import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, KFold
dataset = pd.read_csv('../data/credit_data.csv')
dataset.dropna(inplace=True)
dataset.head()

X = dataset.iloc[:, 1:4].values
y = dataset.iloc[:, 4].values

# diminuir a escala dos dados
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X)

resultados_naive_cv = []
resultados_logistica_cv = []
resultados_forest_cv = []
for i in range(30):
    kfold = KFold(n_splits=10, shuffle=True, random_state=i)

    naive_bayes = GaussianNB()
    scores = cross_val_score(naive_bayes, X, y, cv=kfold)
    resultados_naive_cv.append(scores.mean())

    logistica = LogisticRegression()
    scores = cross_val_score(logistica, X, y, cv=kfold)
    resultados_logistica_cv.append(scores.mean())

    random_forest = RandomForestClassifier()
    scores = cross_val_score(random_forest, X, y, cv=kfold)
    resultados_forest_cv.append(scores.mean())

resultados_naive_cv = np.array(resultados_naive_cv)
resultados_logistica_cv = np.array(resultados_logistica_cv)
resultados_forest_cv = np.array(resultados_forest_cv)

''' 
    alpha = nível de confiança. 
    Se o resultado do teste de hipótese (p-value) for menor, rejeitamos a hipótese nula.
    No caso de testes de normalidade, a hipótese nula é de que os dados encontram-se em uma distribuição normal
'''
alpha = 0.05


# from scipy.stats import shapiro
# print("Shapiro:", shapiro(resultados_naive_cv), shapiro(resultados_logistica_cv), shapiro(resultados_forest_cv))

# from scipy.stats import normaltest
# print("D'Agostinho:", normaltest(resultados_naive_cv), normaltest(resultados_logistica_cv), normaltest(resultados_forest_cv))

# from scipy.stats import anderson
# print("Anderson-Darling:", anderson(resultados_naive_cv).statistic, anderson(resultados_logistica_cv).statistic, anderson(resultados_forest_cv).statistic)

"""
    A interpretação dos resultados obtidos acima é de que os 3 arrays tem os dados distribuidos de forma normal,
    pois o resultado dos testes foi superior ao valor do alpha
"""