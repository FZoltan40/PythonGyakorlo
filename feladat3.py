
tomb = [] 
for i in range(3):
    tomb.append(int(input(f"Kérem {i}. számot:")))


max = tomb[0]
id = 0

for i in range(3):
    if tomb[i] > max:
        max = tomb[i]
        id = i

print(f"A legnagyob eleme a {max} ami a {id+1}. helyen van.")

"""
szam1 = int(input("Kérem az 1. számot"))
szam2 = int(input("Kérem az 2. számot"))
szam3 = int(input("Kérem az 3. számot"))

print(f"A legnagyobb szám: {max(szam1,szam2,szam3)}") 
"""