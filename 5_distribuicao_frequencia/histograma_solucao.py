import pandas as pd

dataset = pd.read_csv('../data/census.csv')

# dataset['age'] = pd.cut(dataset['age'], bins=[0, 17, 25, 40, 60, 90], labels=['Faixa 1', 'Faixa 2', 'Faixa 3', 'Faixa 4', 'Faixa 5'])

# definição de bins manualmente
dataset['age'].plot.hist(bins=[0, 17, 25, 40, 60, 90]);