"""
    Exemplo de lançamento de dados:
    Pergunta 1: qual é a probabilidade de conseguirmos um número par?
    Pergunta 2: qual é a probabilidade de conseguirmos um número menos que seis?
"""

lados = {1, 2, 3, 4, 5, 6}
pares = {2, 4, 6}

prob_pares = len(pares) / len(lados)
print(prob_pares)

prob_menor_seis = 5 / len(lados)
print(prob_menor_seis)

# --------------

"""
    Exemplo das cartas do baralho:
    Temos 52 cartas de baralho, sendo que 13 delas são cartas do naipe de espadas. Qual é a probabilidade de tirarmos
    cinco cartas de espadas seguidas, sem repor a carta que acabamos de tirar do monte?
"""

len_baralho = 52
qtd_espadas = 13

for i in range(0, 5):
    div = (qtd_espadas - i) / (len_baralho - i)
    if i == 0:
        prob = div
    else:
        prob = prob * div

print("%.4f" % prob)

# --------------

"""
    Exemplo dos livros: 
    Numa feira com 90 pessoas, 40 compraram um livro de python, 30 compraram um livro de java e 20 compraram os dois.
    Se escolhermos uma pessoa que comprou o livro de java, qual é a probabilidade ela também ter comprado o livro de python?  
"""

java = 30
ambos = 20
prob_python = ambos / java
print(prob_python)



