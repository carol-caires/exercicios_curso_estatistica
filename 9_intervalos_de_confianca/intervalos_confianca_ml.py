"""
    Intervalos de confiança também podem ser usados para avaliar a margem de erro nos scores de acerto de algoritmos
    de classificação. No exemplo abaixo, comparamos os resultados dos algoritmos Naive-Bayes, Logistic Regression e Random Forest
    para avaliar, de acordo com a margem de erro dos scores, qual algoritmo traz resultados mais confiáveis.
"""

import pandas as pd
import numpy as np
from scipy.stats import t
from scipy.stats import norm
from scipy import stats
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, KFold

dataset = pd.read_csv('../data/credit_data.csv')
dataset.dropna(inplace=True)

X = dataset.iloc[:, 1:4].values
y = dataset.iloc[:, 4].values

"""
    Os arrays `_cv` armazenam as médias da pontuação atingida através do método KFold
    Já os arrays `_cv_300` armazenam todas as pontuações, o que fará com que a distribuição dessas pontuações 
    se aproxime de uma distribuição normal, de acordo com a teoria central do limite
"""
resultados_naive_bayes_cv = []
resultados_naive_bayes_cv_300 = []
resultados_logistica_cv = []
resultados_logistica_cv_300 = []
resultados_forest_cv = []
resultados_forest_cv_300 = []
for i in range(30):
    kfold = KFold(n_splits=10, shuffle=True, random_state=i)

    naive_bayes = GaussianNB()
    scores = cross_val_score(naive_bayes, X, y, cv=kfold)
    resultados_naive_bayes_cv_300.append(scores)
    resultados_naive_bayes_cv.append(scores.mean())

    logistica = LogisticRegression()
    scores = cross_val_score(logistica, X, y, cv=kfold)
    resultados_logistica_cv_300.append(scores)
    resultados_logistica_cv.append(scores.mean())

    random_forest = RandomForestClassifier()
    scores = cross_val_score(random_forest, X, y, cv=kfold)
    resultados_forest_cv_300.append(scores)
    resultados_forest_cv.append(scores.mean())

# converter pro formato do numpy
resultados_naive_bayes_cv = np.array(resultados_naive_bayes_cv)
resultados_naive_bayes_cv_300 = np.array(np.asarray(resultados_naive_bayes_cv_300).reshape(-1))
resultados_logistica_cv = np.array(resultados_logistica_cv)
resultados_logistica_cv_300 = np.array(np.asarray(resultados_logistica_cv_300).reshape(-1))
resultados_forest_cv = np.array(resultados_forest_cv)
resultados_forest_cv_300 = np.array(np.asarray(resultados_forest_cv_300).reshape(-1))


# margem de erro Naive-Bayes

intervalos_naive_bayes_t = t.interval(0.95, len(resultados_naive_bayes_cv) - 1,
                                    resultados_naive_bayes_cv.mean(),
                                    stats.sem(resultados_naive_bayes_cv, ddof = 0))
margem_erro_nb_t = abs(resultados_naive_bayes_cv.mean() - intervalos_naive_bayes_t[1])

intervalos_naive_bayes_n = norm.interval(0.95, resultados_naive_bayes_cv_300.mean(),
                                         stats.sem(resultados_naive_bayes_cv_300))

margem_erro_nb_n = abs(resultados_naive_bayes_cv_300.mean() - intervalos_naive_bayes_n[1])

print("A margem de erro do score Naive-Bayes é de %f para 30 experimentos e %f para 300 experimentos." % (margem_erro_nb_t, margem_erro_nb_n))

# margem de erro Logistic Regression

intervalos_logistica_t = t.interval(0.95, len(resultados_logistica_cv) - 1,
                                    resultados_logistica_cv.mean(),
                                    stats.sem(resultados_logistica_cv, ddof = 0))

margem_erro_lr_t = abs(resultados_logistica_cv.mean() - intervalos_logistica_t[1])

intervalos_logistica_n = norm.interval(0.95, resultados_logistica_cv_300.mean(),
                                       stats.sem(resultados_logistica_cv_300))

margem_erro_lr_n = abs(resultados_logistica_cv_300.mean() - intervalos_logistica_n[1])

print("A margem de erro do score Logistic Regression é de %f para 30 experimentos e %f para 300 experimentos." % (margem_erro_lr_t, margem_erro_lr_n))

# margem de erro Random Forest

intervalos_forest_t = t.interval(0.95, len(resultados_forest_cv) - 1,
                                 resultados_forest_cv.mean(),
                                 stats.sem(resultados_forest_cv, ddof = 0))

margem_erro_rf_t = abs(resultados_forest_cv.mean() - intervalos_forest_t[1])

intervalos_forest_n = norm.interval(0.95, resultados_forest_cv_300.mean(),
                                    stats.sem(resultados_forest_cv_300))

margem_erro_rf_n = abs(resultados_forest_cv_300.mean() - intervalos_forest_n[1])

print("A margem de erro do score Random Forest é de %f para 30 experimentos e %f para 300 experimentos." % (margem_erro_rf_t, margem_erro_rf_n))

"""
    Interpretação: Temos 95% de confiança de que a média de acertos do Random Forest está
    no intervalo entre 98,63% e 98,74% - 98,59% e 98,77%
"""