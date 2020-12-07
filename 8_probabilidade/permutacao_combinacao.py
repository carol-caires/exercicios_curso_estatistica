"""
    Vamos supor que precisamos gerar uma senha de 5 caracteres que pode ter letras e números de zero à nove.
    Obs.: nesse primeiro exemplo os caracteres não podem se repetir
"""

import math

qtd_caracteres = 5
total_caracteres_possiveis = 36  # 26 letras do alfabeto + 10 algarismos

perm = math.factorial(total_caracteres_possiveis) / math.factorial(total_caracteres_possiveis - qtd_caracteres)
print("Quantidade de senhas possíveis:", perm)

''' Nesse segundo exemplo os caracteres podem se repetir '''

perm_repeat = math.pow(total_caracteres_possiveis, qtd_caracteres)
print("Quantidade de senhas possíveis:", perm_repeat)

"""
    A combinação funciona como a permutação, porém a ordem não importa. Por exemplo, numa permutação {A e B} e {B e A} são
    permutações diferentes. Na combinação, ambos contam como apenas 1 evento. 
"""

comb = math.factorial(total_caracteres_possiveis) / (math.factorial(qtd_caracteres) * math.factorial(total_caracteres_possiveis - qtd_caracteres))
print("Quantidade de senhas possíveis:", comb)

comb_repeat = math.factorial(total_caracteres_possiveis + qtd_caracteres - 1) / (math.factorial(qtd_caracteres) * math.factorial(total_caracteres_possiveis - 2))
print("Quantidade de senhas possíveis:", comb_repeat)



