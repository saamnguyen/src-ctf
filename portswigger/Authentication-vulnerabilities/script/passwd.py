passwd = "peter"

f = open("passwdold.txt", "r")
d = open("passwdnew.txt", "w+")

for i in f:
    d.write(f"{i}")
    d.write(f"{passwd}\n")

f.close()
d.close()