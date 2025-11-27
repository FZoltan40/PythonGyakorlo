"""
Kérj be egy számot és döntsd el, hogy benne van-e az előre adott listában.
"""

lista = [3,7,4,2,9,11,77,22]

szam = int(input("Kérek egy egész számot:"))

if szam in lista:
     print("Van találat.")
else:
    print("Nincs találat.")

"""
vane = False

for i in range(len(lista)):
    if lista[i] == szam:
        vane = True
        break

if vane == True:
    print("Van találat.")
else:
    print("Nincs találat.")
"""
