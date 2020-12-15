"""
    Descobrir o intervalo de confiança da média salarial de funcionários com 95% de confiança
"""

import numpy as np
from scipy.stats import norm
from scipy import stats
import math

dados_salario = np.array([82.1191, 72.8014, 79.1266, 71.3552, 59.192, 79.1952, 56.518,
                          70.3752, 73.5364, 61.0407, 64.3902, 66.4076, 63.5215, 71.9936,
                          60.1489, 78.5932, 76.0459, 67.7726, 64.6149, 80.1948, 76.7998,
                          76.1831, 80.7065, 62.4953, 57.204, 62.5408, 80.0982, 63.287,
                          66.5826, 79.3674])

confianca = 0.95
media = dados_salario.mean()
desvio_padrao = np.std(dados_salario)
intervalos = norm.interval(confianca, media, stats.sem(dados_salario))

print("Temos %.2f%% de confiança que a média salarial das pessoas está no intervalo entre %.2f e %.2f"
      % (confianca * 100, intervalos[0], intervalos[1]))
