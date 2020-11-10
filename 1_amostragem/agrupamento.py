import random
from aleatoria_simples import globalDataset


class Agrupamento:
    dataset = globalDataset
    df_amostragem_grupos = None

    def amostragem_agrupamento(self, dataset, numero_grupos):
        intervalo = len(dataset) / numero_grupos

        grupos = []
        id_grupo = 0
        contagem = 0
        for _ in dataset.iterrows():
            grupos.append(id_grupo)
            contagem += 1
            if contagem > intervalo:
                contagem = 0
                id_grupo += 1

        dataset['grupo'] = grupos
        random.seed(1)
        grupo_selecionado = random.randint(0, numero_grupos)
        sample = dataset[dataset['grupo'] == grupo_selecionado]
        self.df_amostragem_grupos = sample
        return sample
