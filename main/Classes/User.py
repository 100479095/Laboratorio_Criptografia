import struct, os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from Keys.Key import ChaChaKey as key

class User():
    def __init__(self, username, password, name, creditcard):
        self.username = username
        self.password = password
        self.name = name
        self.creditcard = creditcard

    def encrypt(self):
        #esto es lo que necesitamos para completar el cifrado
        user = {}
        nonce = os.urandom(8)
        counter =0
        full_nonce = struct.pack("<Q", counter) + nonce
        algorithm = algorithms.ChaCha20(key, full_nonce)
        cipher = Cipher(algorithm, mode=None)
        encryptor = cipher.encryptor()
        #ciframos cada uno de los parámetros
        username = encryptor.update(self.username)
        password = encryptor.update(self.password)
        name = encryptor.update(self.name)
        creditcard = encryptor.update(self.creditcard)
        #los guardamos en el diccionario y devolvemos el usuario encryptado
        user['username'] = username
        user['password'] = password
        user['name'] = name
        user['creditcard'] = creditcard
        return user
    def __dict__(self):
        return self.__dict__()