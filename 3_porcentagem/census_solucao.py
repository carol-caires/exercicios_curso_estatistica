"""
    Solução do exercício feita pelo professor.
    Mantive a minha solução no arquivo census.py, pois dá uma visão diferente
    e a tabela final é de visualização mais fácil da ideia
"""

import pandas as pd

dataset = pd.read_csv('../data/census.csv')

dataset2 = dataset[['income', 'education']]
dataset3 = dataset2.groupby(['education', 'income'])['education'].count()

menos50k = dataset3[' Bachelors', ' <=50K']
mais50k = dataset3[' Bachelors', ' >50K']
total = menos50k + mais50k

mais50kPercent = (mais50k / total) * 100
menos50kPercent = (menos50k / total) * 100

print('%.2f por cento das pessoas ganham menos ou igual 50k.\n%.2f por cento ganham mais que 50k.\nTotal de pessoas: %d'
      % (menos50kPercent, mais50kPercent, total))