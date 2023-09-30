file = open("bin.txt", "r")

m = "0"
for item in file:
    if int(item, 2) > int(m, 2):
        m = item

print(m)

file.close()
