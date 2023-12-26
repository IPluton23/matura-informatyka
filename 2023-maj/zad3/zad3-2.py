file = open("pi.txt", "r")
odp = open("wyniki3.txt", "a")
odp.write("\n3.2\n")

a = ""  # liczba 2-cyfrowa
x = ""  # 1. cyfra liczby

# tworzenie pustej listy
list = [None] * 100  # fragmnety 2-cyfrowe = index listy

# lista wypelniana zerami
for i in range(100):
    list[i] = 0


i = 0                       # liczba a jest 2-cyfrowa dopiero w drugiej petli, zmienna sprawdza ktora to pętla


# tworzenie 2-cyfrowych fragmentow + ile razy wystepują
for y in file:
    y = str(y)[:1]          # usuwanie dopisku '\n' w zmiennej po pobraniu zawartosci z plku
    a = x + y               # zmienna a jest liczbą 2-cyfrowa gdzie x jest 1. cyfra,natomiast y 2. cyfrą
    if i >= 0:              # liczba a jest 2-cyfrowa dopiero w drugiej petli
        list[int(a)] += 1   # zliczanie 2-cyfrowych fragmentow
    x = y                   # x musi przyjac wartosc y aby nie ominąć żadnych kolejnych 2-cyfrowych fragmentó
    i += 1




mn = min(list)              # pobranie najmniejszej liczby wystapien

# poprawnosc formatu zapisu - index (fragment) w zakresie 0-9 jest 1-cyfrowy, a poprawnym formatem jest 2-cyfrowy zapis np. 00, 02
if len( str( list.index(mn) ) ) == 1:
    odp.write("0"+str(list.index(mn)) +" "+ str(mn))      # index() sprawdza pierwszy index ktory przyjmuje wartosc mn
else:
    odp.write(str(list.index(mn)) +" "+ str(mn))

mx = max(list)              # pobranie najwiekszej liczby wystapien
if len( str( list.index(mx) ) ) == 1:
    odp.write("\n0"+str(list.index(mx)) +" "+ str(mx))      # index() sprawdza pierwszy index ktory przyjmuje wartosc mx
else:
    odp.write("\n" + str(list.index(mx)) +" "+ str(mx))


file.close()
odp.close()
