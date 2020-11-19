import pandas as pd

'''
    ** Obtendo as estatísticas (média, moda e mediana) de um dataframe de dados agrupados **
    fi = somatório de elementos dentro de uma classe específica
    xi = média dentro de uma classe específica
    Fi = somatório acumulado de elementos nas classes anteriores e atual
'''

dados = {'inferior': [150, 154, 158, 162, 166, 170],
         'superior': [154, 158, 162, 166, 170, 174],
         'fi': [5, 9, 11, 7, 5, 3]}
dataset = pd.DataFrame(dados)

dataset['xi'] = (dataset['superior'] + dataset['inferior']) / 2
dataset['fi.xi'] = dataset['fi'] * dataset['xi']
dataset['Fi'] = 0

frequencia_acumulada = []
somatorio = 0
for linha in dataset.iterrows():
    somatorio += linha[1][2]
    frequencia_acumulada.append(somatorio)

dataset['Fi'] = frequencia_acumulada


def get_estatisticas(dataframe):
    media = dataframe['fi.xi'].sum() / dataframe['fi'].sum()
    moda = dataframe[dataframe['fi'] == dataframe['fi'].max()]['xi'].values[0]

    fi_2 = dataframe['fi'].sum() / 2
    limite_inferior, frequencia_classe, id_frequencia_anterior = 0, 0, 0
    for i, linha in enumerate(dataframe.iterrows()):
        limite_inferior = linha[1][0]
        frequencia_classe = linha[1][2]
        id_frequencia_anterior = linha[0]
        if linha[1][5] >= fi_2:
            id_frequencia_anterior -= 1
            break
    Fi_anterior = dataframe.iloc[[id_frequencia_anterior]]['Fi'].values[0]
    mediana = limite_inferior + ((fi_2 - Fi_anterior) * 4) / frequencia_classe

    return media, moda, mediana


print(get_estatisticas(dataset))


# Quartil - mediana a 25% e 75%
def get_quartil(dataframe, q1=True):
    if q1 == True:
        fi_4 = dataframe['fi'].sum() / 4
    else:
        fi_4 = (3 * dataframe['fi'].sum()) / 4

    limite_inferior, frequencia_classe, id_frequencia_anterior = 0, 0, 0
    for linha in dataframe.iterrows():
        limite_inferior = linha[1][0]
        frequencia_classe = linha[1][2]
        id_frequencia_anterior = linha[0]
        if linha[1][5] >= fi_4:
            id_frequencia_anterior -= 1
            break
    Fi_anterior = dataframe.iloc[[id_frequencia_anterior]]['Fi'].values[0]
    q = limite_inferior + ((fi_4 - Fi_anterior) * 4) / frequencia_classe

    return q


print(get_quartil(dataset), get_quartil(dataset, q1=False))
