from scipy import ndimage
from scipy.stats import stats
import numpy as np
import statistics
import math

dados = np.array([150, 151, 152, 152, 153, 154, 155, 155, 155, 155, 156, 156, 156,
                  157, 158, 158, 160, 160, 160, 160, 160, 161, 161, 161, 161, 162,
                  163, 163, 164, 164, 164, 165, 166, 167, 168, 168, 169, 170, 172,
                  173])


def get_variancia_desvio_padrao_coeficiente(dataset):
    media = dataset.sum() / len(dataset)
    desvio = abs(dataset - media)
    desvio = desvio ** 2
    soma_desvio = desvio.sum()
    variancia = soma_desvio / len(dataset)
    dp = math.sqrt(variancia)
    return variancia, dp, (dp / media) * 100


variancia, desvio_padrao, coeficiente = get_variancia_desvio_padrao_coeficiente(dados)
print("Variância: %.2f, Desvio Padrão: %.2f, Coeficiente de Variação: %.2f" % (variancia, desvio_padrao, coeficiente))

# Numpy
print("Variância: %.2f, Desvio Padrão: %.2f" % (dados.var(), dados.std()))

# Statistics
print("Variância: %.2f, Desvio Padrão: %.2f" % (statistics.variance(dados), statistics.stdev(dados)))

# Scipy
print("Variância: %.2f, Desvio Padrão: %.2f" % (ndimage.variance(dados), ndimage.standard_deviation(dados)))

# Stats
print("Desvio Padrão: %.2f, Coeficiente de Variação: %.2f" % (stats.tstd(dados, ddof=0), stats.variation(dados) * 100))
