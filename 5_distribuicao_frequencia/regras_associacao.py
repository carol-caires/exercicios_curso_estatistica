import pandas as pd
from apyori import apriori

dataset = pd.read_csv('../data/census.csv')

# para executar o algoritmo apriori, devemos ter apenas colunas com valores categóricos (não numéricos)
dataset_apriori = dataset[['age', 'workclass', 'education', 'marital-status', 'relationship', 'occupation',
                            'sex', 'native-country', 'income']]


# normalmente usa-se um dataset menor para fazer esse tipo de análise
dataset_apriori = dataset_apriori.sample(n = 1000)

# precisamos de um array bi-dimensional para passar como parâmetro
transacoes = []
for i in range(dataset_apriori.shape[0]):
  transacoes.append([str(dataset_apriori.values[i, j]) for j in range(dataset_apriori.shape[1])])


regras = apriori(transacoes, min_support = 0.3, min_confidence = 0.6)
resultados = list(regras)


'''
     Em cada resultado, cada `OrderedStatistic` terá uma associação encontrada pelo algoritmo.
     O campo `confidence` diz em quantos porcento ocorre X e Y
'''

for r in resultados:
    print(r, "\n\n")