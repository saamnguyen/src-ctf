name1 = "carlos"
name2 = "wiener"
length = 0

f = open("username.txt", "w+")

while length <= 100:
    f.write(f"{name1}\n")
    f.write(f"{name2}\n")
    length = length + 1

f.close()