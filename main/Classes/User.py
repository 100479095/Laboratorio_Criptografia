import struct, os
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
import base64

class User():
    def __init__(self, username, password, name, creditcard):
        self.username = username
        self.password = password
        self.name = name
        self.creditcard = creditcard

    def user_encrypt(self):
        #esto es lo que necesitamos para completar el cifrado
        aad = self.password.encode('utf-8')
        key = ChaCha20Poly1305.generate_key()
        #aquí guardaremos los datos cifrados
        user = {}

        #ciframos cada uno de los datos, creando el nonce correspondiente
        username_nonce = os.urandom(12)
        username = self.encrypt(key, aad, username_nonce, self.username.encode('utf-8'))
        user['username'] = base64.b64encode(username).decode('utf-8')
        user['username_nonce'] = base64.b64encode(username_nonce).decode('utf-8')


        password_nonce = os.urandom(12)
        password = self.encrypt(key, aad, password_nonce, self.password.encode('utf-8'))
        user['password'] = base64.b64encode(password).decode('utf-8')
        user['password_nonce'] = base64.b64encode(password_nonce).decode('utf-8')

        name_nonce = os.urandom(12)
        name = self.encrypt(key, aad, name_nonce, self.name.encode('utf-8'))
        user['name'] = base64.b64encode(name).decode('utf-8')
        user['name_nonce'] = base64.b64encode(name_nonce).decode('utf-8')

        creditcard_nonce = os.urandom(12)
        creditcard = self.encrypt(key, aad, creditcard_nonce, self.creditcard.encode('utf-8'))
        user['creditcard'] = base64.b64encode(creditcard).decode('utf-8')
        user['creditcard_nonce'] = base64.b64encode(creditcard_nonce).decode('utf-8')

        return user
    def encrypt(self, key, aad, nonce, dato):
        chacha = ChaCha20Poly1305(key)
        return chacha.encrypt(nonce, dato, aad)
