'''
    O Bernoulli Naive-Bayes é uma versão do Naive-Bayes que tem um melhor desempenho em dados com distribuição Bernoulli,
    ou seja, cujos atributos preditivos tenham apenas 2 valores diferentes.
    No exemplo abaixo, estamos prevendo o atributo 'income' de acordo com o atributo 'sex'.
'''


from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import pandas as pd

dataset = pd.read_csv('../data/census.csv')

X = dataset['sex'].values

label_encoder = LabelEncoder()
X = label_encoder.fit_transform(X) # transforma atributos categóricos em numéricos (0 e 1)s
X = X.reshape(-1, 1) # transforma em formato de matriz

y = dataset['income'].values

bernoulli_naive_bayes = BernoulliNB()
bernoulli_naive_bayes.fit(X, y)

previsoes = bernoulli_naive_bayes.predict(X)

print(accuracy_score(y, previsoes))