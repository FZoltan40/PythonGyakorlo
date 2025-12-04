szam = int(input("Kérem N értékét:"))

ossz = 0
for i in range(1, szam + 1):
    ossz = ossz + i

print(f"A szémok összege: {ossz}")