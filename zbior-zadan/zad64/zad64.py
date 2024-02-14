file = open("dane_obrazki.txt", "r")
odp = open("wyniki_obrazki.txt", "a")
#odp.write("Zad. 64.1:\n")


calosc = [] # Przechowanie obrazów
obraz = [] # Pojedynczy obraz

# Usunięcie bitów parzystości z obrazu
def usun_ramke(obraz):
    new_obraz = []
    for line in obraz[:len(obraz)-1]:
        new_obraz.append(line[:len(line)-1] )
    return new_obraz

# Sprawdzenie czy obraz jest rewersem (zadanie 64.1)
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

# Sprawdzanie czy obrazki sa rekurencyjne (zad 64.2)
def czyRekurencyjny(obraz):
    # tablica 10x10 jest ćwiartką obrazu 20x20
    cwiartka1 = [[0] * 10] * 10
    cwiartka2 = [[0] * 10] * 10
    cwiartka3 = [[0] * 10] * 10
    cwiartka4 = [[0] * 10] * 10

    for i in range(20):
        # ćwiartka 1. i 2. znajdują się w tych samych wierszach, ale różnią się kolumnami. Tak samo ćwiartki 3. i 4.
        if i < 10:
            cwiartka1[i] = obraz[i][:len(obraz)//2] # :len(obraz)//2 -> od 0 do połowy linijki obrazu
            cwiartka2[i] = obraz[i][len(obraz)//2:] # len(obraz)//2: -> od połowy linijki obrazu do końca linijki obrazu
        else:
            cwiartka3[i - 10] = obraz[i][:len(obraz)//2]
            cwiartka4[i - 10] = obraz[i][len(obraz)//2:]

    if cwiartka1 == cwiartka2 == cwiartka3 == cwiartka4:
        return True
    else:
        return False

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

rekurencyjne = [] # tablica z obrazami rekurencyjnymi

for obraz in calosc:
    # ZADANIE 1
    sprawdz = czyRewers(usun_ramke(obraz))
    if sprawdz[0]:
        rewersy.append(line)
        if sprawdz[1] > max_czarne:
            max_czarne = sprawdz[1]
    # ZADANIE 2
    if czyRekurencyjny(usun_ramke(obraz)):
        rekurencyjne.append(obraz)


# Zapis odpowiedzi do pliku
odp.write("Ilość rewersów: " + str(len(rewersy)) + " najwięcej pikseli: " + str(max_czarne))
odp.write("\n\nIlość obrazów rekurencyjnych: " + str(len(rekurencyjne)) + "\nPierwszy obrazek rekurencyjny:")
for line in usun_ramke(rekurencyjne[0]):
    odp.write("\n" + line)

odp.close()
file.close()