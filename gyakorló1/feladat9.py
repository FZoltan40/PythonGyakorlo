"""
Adott egy lista számokkal. Készíts új listát, amelyben csak a páros számok szerepelnek.
"""

lista = [3,5,1,2,9,3,22,16,18,7]

paros = []

for i in range(len(lista)):
    if lista[i] %2 == 0:
        paros.append(lista[i])

print(paros)