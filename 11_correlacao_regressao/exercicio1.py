import pandas as pd

dataset = pd.read_csv('../data/house_prices.csv')
dataset.drop(labels = ['id', 'date', 'sqft_living', 'sqft_lot'], axis = 1, inplace=True)

corr = dataset.corr()

del corr['price']['price']

corr_bem_fraca = [0, 0.19]
corr_fraca = [0.2, 0.39]
corr_moderada = [0.4, 0.69]
corr_forte = [0.7, 0.89]
corr_muito_forte = [0.9, 1]

for i in range(0, len(corr['price'])):
    index = corr['price'].index[i]
    value = corr['price'].values[i]

    if corr_bem_fraca[0] <= abs(value) <= corr_bem_fraca[1]:
        print("[bem fraca]", index, value)
    elif corr_fraca[0] <= abs(value) <= corr_fraca[1]:
        print("[fraca]", index, value)
    elif corr_moderada[0] <= abs(value) <= corr_moderada[1]:
        print("[moderada]", index, value)
    elif corr_forte[0] <= abs(value) <= corr_forte[1]:
        print("[forte]", index, value)
    elif corr_muito_forte[0] <= abs(value) <= corr_muito_forte[1]:
        print("[muito forte]", index, value)

q = corr['price'].quantile([0.75])
print("\n\nAtributos com correlação mais forte em relação ao preço:\n")
print(corr['price'][corr['price'].values > q.values[0]])

# podemos gerar gráficos para verificar se há uma relação linear entre os atributos
# import seaborn as sns
# sns.scatterplot(dataset['sqft_living15'], dataset['price']);
# sns.scatterplot(dataset['grade'], dataset['price']);

# heatmap
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots(figsize=(15,15))
# ax = sns.heatmap(dataset.corr(), annot=True)