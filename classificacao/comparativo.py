from reputacao_ebay import PredicaoReputacao
import pandas as pd

dataset = pd.read_csv('csv_result-ebay_confianca_completo.csv')


pr = PredicaoReputacao()
scores = pr.predict(dataset)

print(scores)