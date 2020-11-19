import math
import numpy as np
import pandas as pd
from scipy import stats

dados = np.array([150, 151, 152, 152, 153, 154, 155, 155, 155, 155, 156, 156, 156,
                  157, 158, 158, 160, 160, 160, 160, 160, 161, 161, 161, 161, 162,
                  163, 163, 164, 164, 164, 165, 166, 167, 168, 168, 169, 170, 172,
                  173])

# Quartis - Cálculo manual
posicao_mediana = math.floor(len(dados) / 2)
esquerda = dados[0:posicao_mediana]
direita = dados[posicao_mediana + 1:]

print("25%%: %.2f, 50%%: %.2f, 75%%: %.2f" %(np.median(esquerda), np.median(dados), np.median(direita)))

# Numpy
print("25%%: %.2f, 50%%: %.2f, 75%%: %.2f" %(np.quantile(dados, 0.25), np.quantile(dados, 0.5), np.quantile(dados, 0.75)))

# Scipy
print("25%%: %.2f, 50%%: %.2f, 75%%: %.2f" %(stats.scoreatpercentile(dados, 25), stats.scoreatpercentile(dados, 50), stats.scoreatpercentile(dados, 75)))

# Pandas
dataset = pd.DataFrame(dados)
q = dataset.quantile([0.25, 0.5, 0.75])
print("25%%: %.2f, 50%%: %.2f, 75%%: %.2f" %(q[0][0.25], q[0][0.5], q[0][0.75]))