"""
    T-Student é o tipo de distribuição parecida com a distribuição normal, porém usada para amostras de dados pequenas (até 30 elementos)
"""

from scipy.stats import t
from scipy import stats
import numpy as np

''' Cálculo de intervalos de confiança '''

dados = np.array([149. , 160., 147., 189., 175., 168., 156., 160., 152.])

n = len(dados)
media = dados.mean()
desvio_padrao = np.std(dados)

intervalos = t.interval(0.95, n - 1, media, stats.sem(dados, ddof = 0))
margem_erro = media - intervalos[0]

print("A margem de erro das alturas é de %.2f centímetros" % margem_erro)



