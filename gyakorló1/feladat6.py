
tm = []

for i in range(5):
    tm.append(int(input(f"Kérem a {i+1}. számot: ")))

ossz = 0

for i in range(5):
    ossz = ossz + tm[i]

print(f"A lista elmeinek az átlaga: {ossz/len(tm)}")

