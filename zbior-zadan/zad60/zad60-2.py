file = open("liczby.txt", "r")
odp = open("wyniki.txt", "a")
odp.write("\n60.2:\n")

dzielniki = []

for item in file:
    i = 1
    while i * i <= int(item):
        if int(item) % i == 0:
            dzielniki.append(i)
            dzielniki.append(int( int(item) / i) )
        i += 1
    if len(dzielniki) == 18:
        odp.write(str(item) + "\t" + str(sorted(dzielniki)) + "\n")
        print(sorted(dzielniki))
    dzielniki.clear()


odp.close()
file.close()