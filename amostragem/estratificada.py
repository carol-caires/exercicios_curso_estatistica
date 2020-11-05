from sklearn.model_selection import StratifiedShuffleSplit
from aleatoria_simples import globalDataset


class Estratificada:
    dataset = globalDataset
    df_amostragem_estratificada = None

    def amostragem_estratificada(self, dataset, percentual):
        global df_y
        split = StratifiedShuffleSplit(test_size=percentual, random_state=1)
        for _, y in split.split(dataset, dataset['c#default']):
            df_y = dataset.iloc[y]
        self.df_amostragem_estratificada = df_y
        return df_y

