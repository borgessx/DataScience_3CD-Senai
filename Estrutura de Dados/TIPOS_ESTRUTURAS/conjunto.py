# CONJUNTO

conjunto_a = {1,2,3,4}
conjunto_b = {3,4,5,6}

# uniao (juntar os dois conjuntos)
uniao = conjunto_a | conjunto_b

print(uniao)

# interseccao (juntas elementos em comum)
inter = conjunto_a & conjunto_b
print(inter)

# diferenca (elementos que estao no conjunto_a, mas nao no conjunto_b)
difer = conjunto_a - conjunto_b
print(difer)

# diferenca simetrica (elementos que estao em ambos, nao exibidos)
difer_sim = conjunto_a ^ conjunto_b
print(difer_sim)

