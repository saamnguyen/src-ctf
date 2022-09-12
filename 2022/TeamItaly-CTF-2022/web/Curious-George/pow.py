from hashlib import md5
from sys import argv, exit
import os

def collide(coll):
    while True:
        s = os.urandom(20)
        h = md5(s).hexdigest()
        if h[:len(coll)] == coll:
            print(f"String: {s.hex()}")
            print(f"Hash: {h}")
            break

if __name__ == "__main__":
    if len(argv) != 2:
        print(f"Usage:\t{argv[0]} <PARTIAL-COLLISION>")
        exit(-1)
    tocoll = argv[1]
    print("Colliding stars...")
    collide(tocoll)
    exit(0)


