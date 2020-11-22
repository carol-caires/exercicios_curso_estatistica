import math
import statistics
import numpy as np
import pandas as pd
from scipy.stats.mstats import hmean
from scipy.stats.mstats import gmean

dataset = pd.read_csv('../data/census.csv')
dados = np.array(dataset['age'])


def qmean(dados):
    return math.sqrt(sum(n * n for n in dados) / len(dados))


print("Média aritmética:", dados.mean())
print("Média Harmômica:", hmean(dados))
print("Média Geométrica:", gmean(dados))
print("Média Quadrática:", qmean(dados))
print("Mediana:", statistics.median(dados))
print("Moda:", statistics.mode(dados))
