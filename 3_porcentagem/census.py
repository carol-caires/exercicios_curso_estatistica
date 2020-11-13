import pandas as pd

dataset = pd.read_csv('../data/census.csv')

education = dataset['education'].unique()

d = {'education': [], '>50': [], '<=50': []}
for ed in education:
    d['education'].append(ed)
    filtered = dataset[dataset['education'] == ed]
    more50 = filtered[filtered['income'] == ' >50K']['income'].count()
    less50 = filtered[filtered['income'] == ' <=50K']['income'].count()
    d['>50'].append(more50)
    d['<=50'].append(less50)

df = pd.DataFrame(d)

df['%_>50'] = (df['>50'] / df['>50'].sum()) * 100
df['%_<=50'] = (df['<=50'] / df['<=50'].sum()) * 100

print(df)
