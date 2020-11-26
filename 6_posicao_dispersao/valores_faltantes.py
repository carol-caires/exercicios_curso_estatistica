import statistics
import pandas as pd
import numpy as np

dataset = pd.read_csv('../data/credit_data.csv')

# Substituindo valores numéricos faltantes com a média

print("Valores faltantes:\n\n", dataset.isnull().sum())

dataset['age'] = dataset['age'].replace(to_replace = np.nan, value = dataset['age'].mean())

print("\n\nValores faltantes depois da substituição:\n\n", dataset.isnull().sum())

dataset2 = pd.read_csv('../data/autos.csv', encoding='ISO-8859-1')

# Substituindo valores categóricos faltantes com a moda

print("\n\nValores faltantes:\n\n", dataset2['fuelType'].isnull().sum())

dataset2['fuelType'] = dataset2['fuelType'].replace(to_replace = np.nan, value = statistics.mode(dataset2['fuelType']))

print("\n\nValores faltantes depois da substituição:\n\n", dataset2['fuelType'].isnull().sum())