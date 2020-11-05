import random
from aleatoria_simples import globalDataset


class Reservatorio:
    dataset = globalDataset
    df_amostragem_reservatorio = None

    def amostragem_reservatorio(self, dataset, amostras):
        stream = []
        for i in range(len(dataset)):
            stream.append(i)

        i = 0
        tamanho = len(dataset)

        reservatorio = [0] * amostras
        for i in range(amostras):
            reservatorio[i] = stream[i]

        while i < tamanho:
            j = random.randrange(i + 1)
            if j < amostras:
                reservatorio[j] = stream[i]
            i += 1

        sample = dataset.iloc[reservatorio]
        self.df_amostragem_reservatorio = sample

        return sample
