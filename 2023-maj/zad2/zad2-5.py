#p XOR (p//2)
file = open("bin.txt", "r")
odp = open("wyniki2_5.txt","a")

for item in file:
    item2 = int(item, 2) // 2
    item2 = bin(item2)[2:]
    if( len(item) > len(item2) ):
        item2 = "0" + item2
    wynik = ""
    for i in range(0, len(item)-1 ):
        if item[i] != item2[i]:
            wynik += "1"
        else:
            wynik += "0"
    print(wynik)
    odp.write(wynik+"\n")

file.close()
