import pandas as pd
import seaborn as sns

dataset = pd.read_csv('../data/census.csv')

# atributos numéricos
sns.distplot(dataset['age'])  # gama
sns.distplot(dataset['final-weight'])  # gama
sns.distplot(dataset['hour-per-week'])  # binomial ou poisson
sns.distplot(dataset['capital-gain'])  # exponencial
sns.distplot(dataset['capital-loos'])  # exponencial
sns.distplot(dataset['hour-per-week'])  # poisson ou binomial
sns.distplot(dataset['education-num'])  # poisson

# atributos categóricos
sns.countplot(dataset['marital-status'])  # binomial
sns.countplot(dataset['sex'])  # bernoulli
sns.countplot(dataset['income'])  # bernoulli

dataset = pd.read_csv('../data/credit_data.csv')

sns.distplot(dataset['income'])  # uniforme
sns.distplot(dataset['age'])  # uniforme
sns.distplot(dataset['loan'])  # gama
sns.distplot(dataset['c#default'], kde=False)  # bernoulli
