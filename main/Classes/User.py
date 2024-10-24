import struct, os
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import base64
from Store.Keys_Store import KeysStore

class User():
    def __init__(self, username, name, creditcard):
        self.username = username
        self.name = name
        self.creditcard = creditcard

    def user_encrypt(self, password):
        #esto es lo que necesitamos para completar el cifrado
        aad = None
        key = ChaCha20Poly1305.generate_key()
        store = KeysStore()
        store.key_encryption(self.username, key)
        #aquí guardaremos los datos cifrados
        user = {}

        #Dejamos el username en blanco para poder buscar al usuario con mayor facilia
        user['username'] =self.username

        #Creamos y guardamos el password_token y el password salt
        password_salt = os.urandom(12)
        kdf= Scrypt(
            salt = password_salt,
            length = 32,
            n=2**14,
            r=8,
            p=1
        )
        user_password = password.encode('utf-8')
        password_token = kdf.derive(user_password)
        user['password_token'] = base64.b64encode(password_token).decode('utf-8')
        user['password_salt'] = base64.b64encode(password_salt).decode('utf-8')

        #ciframos el resto de datos
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
