#Zamienia liczbe calkowita na binarna i ja zwraca (bez uzycia wbudowanych funkcji)
def Int_to_bin(i):
    wynik = ""
    index = 0
    reversed = ""

    while i>0:
        wynik += str(i%2)
        i = i//2
    for element in wynik:
        index = index +1
    while index>0:
        reversed += wynik[index-1]
        index -= 1
    return reversed


#liczy ilsoc blokow w liczbie binarnej i ja zwraca
def countBlocks (reversed):
    index = -1
    count = 1
    i = 1
    for element in reversed:
        index += 1
    while i < index:
        if reversed[i - 1] != reversed[i]:
            count += 1
        i += 1
    return count


n = int(input("Podaj liczbę całkowitą "))

w = Int_to_bin(n)
print(w)

b = countBlocks(w)
print(b)
