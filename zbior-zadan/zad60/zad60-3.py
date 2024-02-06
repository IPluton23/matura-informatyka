file = open("liczby.txt", "r")
odp = open("wyniki.txt", "a")
odp.write("\n60.3:\n")

# Liczby są względnie pierwsze gdy ich nwd = 1
def nwd(x, y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y-x
    return x


liczby = list(file) # elementy z pliku jako lista
najwieksza = 0  # najwieksza liczba wzglednie pierwsza z innymi

for i in range(200):
    czyPierwsza = True

    for j in range(i, 200):
        if (nwd(int(liczby[i]), int(liczby[j])) > 1 and i != j):
            czyPierwsza = False # Jeżeli nwd dwoch liczb jest >1 to nie są wzglednie pierwsze

    if(czyPierwsza and int(liczby[i]) > int(najwieksza)):
        najwieksza = liczby[i]

odp.write("Największa liczba względnie pierwsza: " + str(najwieksza))

odp.close()
file.close()