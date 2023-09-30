file = open("bin.txt", "r")

ilosc = 0
for x in file:
    i = 1
    blok = 0
    while i < len(x):
        if x[i - 1] != x[i]:
            blok += 1
        i += 1
    if blok < 3:
        ilosc += 1
print(ilosc)

file.close()
