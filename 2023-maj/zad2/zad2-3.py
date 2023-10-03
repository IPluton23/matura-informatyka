file = open("bin.txt", "r")
odp = open("wyniki2.txt","a")

m = "0"
for item in file:
    if int(item, 2) > int(m, 2):
        m = item

print(m)
odp.write("\n2.3:\n" + m)

file.close()
