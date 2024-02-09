file = open("dane_obrazki.txt", "r")
odp = open("wyniki_obrazki.txt", "a")
odp.write("Zad. 64.1:\n")


calosc = [] # Przechowanie obrazów
obraz = [] # Pojedynczy obraz

# Usunięcie bitów parzystości z obrazu
def usun_ramke(obraz):
    new_obraz = []
    for line in obraz[:len(obraz)-1]:
        new_obraz.append(line[:len(line)-1] )
    return new_obraz

# Sprawdzenie czy obraz jest rewersem
def czyRewers(obraz):
    zera = 0
    jedynki = 0
    for line in obraz:
        zera += line.count("0")
        jedynki += line.count("1")
    if jedynki > zera:
        return [True, jedynki]
    else:
        return [False, jedynki]

# Przekazanie obrazów do listy calosc[]
for line in file:
    if line == "\n":
        calosc.append(obraz)
        obraz = []
        continue
    obraz.append(line.strip())
calosc.append(obraz)

rewersy = [] # tablica z obrazami będącymi rewersami
max_czarne = 0 # najwieksza liczba czarnych pikseli

for obraz in calosc:
    sprawdz = czyRewers(usun_ramke(obraz))
    if sprawdz[0]:
        rewersy.append(line)
        if sprawdz[1] > max_czarne:
            max_czarne = sprawdz[1]

odp.write("Ilość rewersów: " + str(len(rewersy)) + " najwięcej pikseli: " + str(max_czarne))

odp.close()
file.close()