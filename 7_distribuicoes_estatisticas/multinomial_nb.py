'''
    O Multinomial Naive-Bayes é uma versão do Naive-Bayes que tem um melhor desempenho em dados com distribuição multinomial,
    Ou seja, cujos atributos sejam atributos categóricos com vários valores possíveis.
    No exemplo abaixo, estamos prevendo o atributo 'income' de acordo com todos os atributos com distribuição multinomial da base.
'''

from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import pandas as pd

dataset = pd.read_csv('../data/census.csv')

label_encoder0 = LabelEncoder()
label_encoder1 = LabelEncoder()
label_encoder2 = LabelEncoder()
label_encoder3 = LabelEncoder()
label_encoder4 = LabelEncoder()
label_encoder5 = LabelEncoder()
label_encoder6 = LabelEncoder()

dataset['workclass'] = label_encoder0.fit_transform(dataset['workclass'])
dataset['education'] = label_encoder1.fit_transform(dataset['education'])
dataset['marital-status'] = label_encoder2.fit_transform(dataset['marital-status'])
dataset['occupation'] = label_encoder3.fit_transform(dataset['occupation'])
dataset['relationship'] = label_encoder4.fit_transform(dataset['relationship'])
dataset['race'] = label_encoder5.fit_transform(dataset['race'])
dataset['native-country'] = label_encoder6.fit_transform(dataset['native-country'])

X = dataset.iloc[:, [1,3,5,6,7,8,13]].values

y = dataset['income'].values

multinomial_naive_bayes = MultinomialNB()
multinomial_naive_bayes.fit(X, y)

previsoes = multinomial_naive_bayes.predict(X)

print(accuracy_score(y, previsoes))