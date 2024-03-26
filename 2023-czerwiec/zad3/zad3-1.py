file = open("anagram.txt","r")
odp = open("wyniki3.txt", "a")

typ = [0, 0]  # Do zliczania zrównowazonych i prawie zrównoważonych - index 0 zrówn., index 1 prawie zrówn.

for item in  file:
    zera = item.count("0")          # Zliczanie zer
    jedynki = item.count("1")       # Zliczanie jedynek
    if zera == jedynki:
        typ[0] += 1                 # Zrównoważona
    elif zera == jedynki + 1 or zera == jedynki - 1:
        typ[1] += 1                 # Prawie zrównoważona


print("Zrównoważone: ",typ[0] ," Prawie zrównoważone:", typ[1])
odp.write("Zrównoważone: " + str(typ[0]) + " Prawie zrównoważone: " + str(typ[1]))

odp.close()
file.close()
