file = open("dane_obrazki.txt", "r")
odp = open("wyniki_obrazki.txt", "a")
#odp.write("Zad. 64.1:\n")


calosc = []  # Przechowanie obrazów
obraz = []  # Pojedynczy obraz

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
            cwiartka1[i] = obraz[i][:len(obraz)//2]  # :len(obraz)//2 -> od 0 do połowy linijki obrazu
            cwiartka2[i] = obraz[i][len(obraz)//2:]  # len(obraz)//2: -> od połowy linijki obrazu do końca linijki obrazu
        else:
            cwiartka3[i - 10] = obraz[i][:len(obraz)//2]
            cwiartka4[i - 10] = obraz[i][len(obraz)//2:]

    if cwiartka1 == cwiartka2 == cwiartka3 == cwiartka4:
        return True
    else:
        return False

# Sprawdzenie poprawności i naprawialności obrazów (zad 64.3)
def poprawnosc(obraz):
    pion_obraz = [""]*20  # 20-elementowa tablica zawierająca obraz czytany od góry na dół, bez bitów parzystości wierszy

    pion_bity = []  # tablica zawierająca bity parzystości z ostatniej linii obrazu
    poziom_bity = []  # tablica zawierająca bity parzystosci z ostatniej kolumny

    new_obraz = usun_ramke(obraz)

    bledy_pion = 0  # ilość błędów w ostatnim wierszu obrazu
    bledy_poziom = 0  # ilość błędów w ostatniej kolumnie obrazu

    nr_wiersza = 0  # nr wiersza w którym znajduje się błąd
    nr_kolumny = 0  # nr kolumny w której znajduje się błąd

    for line in obraz:
        # Obrócenie obrazu
        for i in range(20):
            pion_obraz[i] += line[i]
    # Zapis bitów parzystości do tablic
    for i in range(20):
        poziom_bity.append(obraz[i][-1])
        pion_bity.append(pion_obraz[i][-1])
    # Zliczanie błędów parzystości w poziomie i pionie
    for i in range(20):
        bit1 = new_obraz[i].count("1") % 2
        if str(bit1) != poziom_bity[i]:
            bledy_poziom += 1
            nr_wiersza = i + 1

        bit2 = pion_obraz[i][:20].count("1") % 2
        if str(bit2) != pion_bity[i]:
            bledy_pion += 1
            nr_kolumny = i + 1

    if bledy_poziom == 0 and bledy_pion == 0:
        return ["poprawny", bledy_pion + bledy_poziom]
    elif bledy_poziom >1 or bledy_pion > 1:
        return ["nienaprawialny", bledy_pion + bledy_poziom]
    else:
        return ["naprawialny", bledy_pion + bledy_poziom, nr_wiersza, nr_kolumny]



# Przekazanie obrazów do listy calosc[]
for line in file:
    if line == "\n":
        calosc.append(obraz)
        obraz = []
        continue
    obraz.append(line.strip())
calosc.append(obraz)

rewersy = []  # tablica z obrazami będącymi rewersami
max_czarne = 0  # najwieksza liczba czarnych pikseli

rekurencyjne = []  # tablica z obrazami rekurencyjnymi

naprawialnosc = []  # przechowuje info o poprawnosci/naprawialnosci/nienaprawialnosci i liczbie bledow kazdego z obrazka
max_bledy = 0  # maksymalna ilosc bledow w jednym obrazku
poprawne = 0  # ilość poprawnych obrazków
naprawialne = 0  # ilość naprawialnych obrazków
nienaprawialne = 0  # ilość nienaprawialnych obrazków

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
    # ZADANIE 3
    naprawialnosc.append(poprawnosc(obraz))

print(naprawialnosc)

# ZADANIE 3 i 4
for i, item in enumerate(naprawialnosc):
    # Sprawdzanie największej ilości błędów
    if item[1] > max_bledy:
        max_bledy = item[1]
    # Zliczanie ilości obrazów pop./napraw./nienapraw.
    if item[0] == "poprawny":
        poprawne += 1
    elif item[0] == "naprawialny":
        naprawialne += 1

        # jezeli wiersz / kolumna == 0 to błąd występuje w bicie parzystości
        if item[2] == 0: item[2] = 21
        if item [3] == 0: item[3] = 21
        odp.write("\n\n Numer obrazka naprawialnego: {} \tWiersz: {} \tKolumna:{}".format(i, item[2], item[3]) )
    else:
        nienaprawialne += 1


# Zapis odpowiedzi do pliku
odp.write("Ilość rewersów: {} najwięcej pikseli: {}".format(len(rewersy), max_czarne))
odp.write("\n\nIlość obrazów rekurencyjnych: {} \nPierwszy obrazek rekurencyjny:".format(len(rekurencyjne)) )
for line in usun_ramke(rekurencyjne[0]):
    odp.write("\n" + line)
odp.write("\n\nIlość obrazków poprawnych: {} \nnaprawialnych: {} \nnienaprawialnych: {} \nNajwiększa ilość błędów w jednym obrazku: {}".format(poprawne, naprawialne, nienaprawialne, max_bledy))


odp.close()
file.close()