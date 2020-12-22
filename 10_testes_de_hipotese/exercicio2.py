from testes_normalidade import resultados_naive_cv, resultados_logistica_cv, resultados_forest_cv
from scipy.stats import f_oneway
import pandas as pd
import numpy as np
from statsmodels.stats.multicomp import MultiComparison

# ANOVA
_, p = f_oneway(resultados_naive_cv, resultados_logistica_cv, resultados_forest_cv)
print("ANOVA: ", p)

alpha = 0.05
if p <= alpha:
  print('Hipótese nula rejeitada. Dados são diferentes')
else:
  print('Hipótese alternativa rejeitada')

# Tukey

resultados_algoritmos = {'accuracy': np.concatenate([resultados_naive_cv, resultados_logistica_cv, resultados_forest_cv]),
                         'algoritmo': ['naive', 'naive','naive','naive','naive','naive','naive','naive','naive','naive',
                                       'naive', 'naive','naive','naive','naive','naive','naive','naive','naive','naive',
                                       'naive', 'naive','naive','naive','naive','naive','naive','naive','naive','naive',
                                       'logistic','logistic','logistic','logistic','logistic','logistic','logistic','logistic','logistic','logistic',
                                       'logistic','logistic','logistic','logistic','logistic','logistic','logistic','logistic','logistic','logistic',
                                       'logistic','logistic','logistic','logistic','logistic','logistic','logistic','logistic','logistic','logistic',
                                       'forest','forest','forest','forest','forest','forest','forest','forest','forest','forest',
                                       'forest','forest','forest','forest','forest','forest','forest','forest','forest','forest',
                                       'forest','forest','forest','forest','forest','forest','forest','forest','forest','forest']}

resultados_df = pd.DataFrame(resultados_algoritmos)
compara_grupos = MultiComparison(resultados_df['accuracy'], resultados_df['algoritmo'])
teste = compara_grupos.tukeyhsd()
print(teste)
