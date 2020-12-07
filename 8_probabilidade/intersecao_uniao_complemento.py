a = (0, 1, 2, 3, 4, 5, 6, 7)
b = (0, 2, 4, 6, 8)

''' Interseção: o que está em ambos os conjuntos (operador `and`) '''

print(set(a) and set(b))

''' União: o que está em um conjunto ou o outro (operador `or`) '''

print(set(a) | set(b))

''' Diferença: o que tem em um que não tem no outro '''

print(set(a).difference(set(b)))  # o que tem em `a` que não tem em `b`
print(set(b).difference(set(a)))  # o que tem em `b` que não tem em `a`
