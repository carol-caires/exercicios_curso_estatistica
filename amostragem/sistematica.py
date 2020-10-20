import pandas as pd
import random
import numpy as np

dataset = pd.read_csv('credit_data.csv')


def amostragem_sistematica(dataset, amostras):
    intervalo = len(dataset) // amostras
    random.seed(1)
    inicio = random.randint(0, intervalo)
    indices = np.arange(inicio, len(dataset), step=intervalo)
    amostra_sistematica = dataset.iloc[indices]
    return amostra_sistematica


df_amostragem_sistematica = amostragem_sistematica(dataset, 1000)
print(df_amostragem_sistematica.shape)
print(df_amostragem_sistematica.head())
