import pandas as pd

dataset = pd.read_csv('credit_data.csv')


def amostragem_aleatoria_simples(dataset, amostras):
    return dataset.sample(n=amostras, random_state=1)


df_amostragem_aleatoria_simples = amostragem_aleatoria_simples(dataset, 1000)
print(df_amostragem_aleatoria_simples.shape)
print(df_amostragem_aleatoria_simples.head())
