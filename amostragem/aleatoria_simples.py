import pandas as pd

globalDataset = pd.read_csv('credit_data.csv')


class AleatoriaSimples:
    dataset = globalDataset
    df_amostragem_aleatoria_simples = None

    def amostragem_aleatoria_simples(self, dataset, amostras):
        sample = dataset.sample(n=amostras, random_state=1)
        self.df_amostragem_aleatoria_simples = sample
        return sample
