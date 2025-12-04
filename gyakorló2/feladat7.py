"""
7. feladat – OOP: Egyszerű Osztály – Auto

Hozz létre egy Auto osztályt, amely attribútumai:

marka
tipus
evjarat

Az osztály tartalmazzon metódust, ami kiírja a teljes adatot szép formában.
"""

class Auto:
    def __init__(self, marka, tipus, evjarat ):
        self.marka = marka
        self.tipus = tipus
        self.evjarat = evjarat
    
    def kiir(self):
        print(f"{self.marka},{self.tipus},{self.evjarat}")

auto1 = Auto("Audi","a4",2022)
auto2 = Auto("Bmw","i3",2024)

auto2.kiir()