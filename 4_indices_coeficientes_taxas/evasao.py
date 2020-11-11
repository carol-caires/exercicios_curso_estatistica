import pandas as pd

tabela = {
    'ano 1': {'marco': 70, 'novembro': 65},
    'ano 2': {'marco': 50, 'novembro': 48},
    'ano 3': {'marco': 47, 'novembro': 40},
    'ano 4': {'marco': 23, 'novembro': 22},
}

total_matriculas = 0
total_evasoes = 0
for k in tabela:
    total_matriculas += tabela[k]['marco']
    total_evasoes += tabela[k]['marco'] - tabela[k]['novembro']
    coef = (tabela[k]['marco'] - tabela[k]['novembro']) / tabela[k]['marco']
    taxa = coef * 100
    tabela[k]['%_evasao'] = taxa

tabela['total'] = {
    'marco': total_matriculas,
    'novembro': total_matriculas - total_evasoes,
    '%_evasao': (total_evasoes / total_matriculas) * 100
}
df = pd.DataFrame(tabela)
print(df)