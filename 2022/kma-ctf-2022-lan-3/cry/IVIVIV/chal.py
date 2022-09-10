from Crypto.Cipher import AES
from os import urandom
from secret import FLAG

assert len(FLAG) == 16

banner = """
=============================
|           HELLO           |
=============================
Options:
[1] Encrypt
[2] Decrypt
"""

class Cipher:
    def __init__(self, IV, key):
        self.IV = IV
        self.key = key
    
    def encrypt(self, plaintext):
        plaintext = plaintext + bytes(16 - (len(plaintext))%16)
        cipher = AES.new(self.key, AES.MODE_CBC, self.IV)
        return cipher.encrypt(plaintext).hex()
    
    def decrypt(self, ciphertext):
        cipher = AES.new(self.key, AES.MODE_CBC, self.IV)
        return cipher.decrypt(ciphertext).hex()

if __name__ == "__main__":
    key = urandom(16)
    IV = FLAG
    cipher = Cipher(IV, key)
    print(banner)
    while True:
        try:
            inp = int(input(">>> "))
            if inp == 1:
                plaintext = bytes.fromhex(input("Plaintext: "))
                print(cipher.encrypt(plaintext))
            elif inp == 2:
                ciphertext = bytes.fromhex(input("Ciphertext: "))
                print(cipher.decrypt(ciphertext))
            else:
                break
        except:
            break