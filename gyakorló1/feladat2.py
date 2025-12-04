"Kérj be egy számot, és döntsd el, hogy páros-e."

szam = int(input("Kérem a számot:"))

if szam != 0:
    if szam % 2 == 0:
        print("A szám páros.")
    else:  
        print("A szám páratlan.")
else:
     print("A szám nem lehet nulla.")


"""
szam = int(input("Kérem a számot:"))

while(szam==0):
    szam = int(input("Kérem a számot:"))

if szam % 2 == 0:
    print("A szám páros.")
else:  
    print("A szám páratlan.")

"""