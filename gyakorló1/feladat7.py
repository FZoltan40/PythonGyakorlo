"""
Adj meg egy listát tetszőleges egész számokkal, majd írd ki:
a legnagyobb értéket
a legkisebb értéket
"""

lista = [4,6,8,11,4,2,6]

max = lista[0]

for i in range(len(lista)):
    if lista[i] > max:
        max = lista[i]

print(f"A legnagyobb elem a {max}")

min = lista[0]

for i in range(len(lista)):
    if lista[i] < min:
        min = lista[i]
        
print(f"A legkisebb elem a {min}")