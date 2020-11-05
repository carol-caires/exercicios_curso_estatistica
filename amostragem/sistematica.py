import random
import numpy as np
from aleatoria_simples import globalDataset


class Sistematica:
    dataset = globalDataset
    df_amostragem_sistematica = None

    def amostragem_sistematica(self, dataset, amostras):
        intervalo = len(dataset) // amostras
        random.seed(1)
        inicio = random.randint(0, intervalo)
        indices = np.arange(inicio, len(dataset), step=intervalo)
        amostra_sistematica = dataset.iloc[indices]
        self.df_amostragem_sistematica = amostra_sistematica
        return amostra_sistematica
