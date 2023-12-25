file = open("pi.txt", "r")
odp = open("wyniki3.txt", "a")

count = 0
x = "0"

# a = xy  -  x==9, y>0

for y in file:
    y = str(y)[:1]
    print(x, y)
    if x == "9" and y > "0":
        count += 1
    x = y
print(count)

odp.write("3.1:\n" + str(count))

file.close()
odp.close()
