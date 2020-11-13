import numpy as np
import pandas as pd

dataset = pd.read_csv('../data/census.csv')
dados = np.array(dataset['age'])

frequencia, classes = np.histogram(dados)


