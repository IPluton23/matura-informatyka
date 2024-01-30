file = open("liczby.txt", "r")
odp = open("wyniki.txt", "a")

lista = list(file)

wynik = 0       #ilosc liczb <1000
liczby = [0, 0] #dwie ostatnie liczby <1000

#lista sprawdzana od konca
for i in range(-1, -200, -1):
    if int(lista[i]) < 1000:
        if wynik < 2:   #dwie ostatnie liczby <1000 są ostatnie w pliku ale pierwsze w pętli
            liczby[wynik] = int(lista[i])
        wynik += 1

print(liczby)
print(wynik)

odp.write("60.1: \n")
odp.write(str(wynik) + "\t")
odp.write(str(liczby[0]) + "\t")
odp.write(str(liczby[1]) + "\n")

odp.close()
file.close()
