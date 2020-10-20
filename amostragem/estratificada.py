import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit

dataset = pd.read_csv('credit_data.csv')


def amostragem_estratificada(dataset, percentual):
    global df_y
    split = StratifiedShuffleSplit(test_size=percentual, random_state=1)
    for _, y in split.split(dataset, dataset['c#default']):
        df_y = dataset.iloc[y]
    return df_y


df_amostragem_estratificada = amostragem_estratificada(dataset, 0.5)
print(df_amostragem_estratificada.shape)
print(df_amostragem_estratificada.head())
print(df_amostragem_estratificada['c#default'].value_counts())
