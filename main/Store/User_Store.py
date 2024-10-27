import base64
import json
from Store.json_store import JsonStore
from Classes.User import User
import struct, os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from Keys.Key import ChaChaKey
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from tkinter import messagebox
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from Store.Keys_Store import KeysStore
STORE_NAME= "Users.json"
class UserStore(JsonStore):

    def __init__(self):
        super().__init__(STORE_NAME)
        self.load_store()

    def find_user(self, username):
        """"Buscamos en la base de datos al usuario con el username dado y lo devolvemos, de no existir
        devolvemos None"""
        for user in self.data_list:
            if user["username"] == username:
                return user
        return None

    def autenthicate_user(self, username, password):
        """"Verificamos si el usuario existe en la base de datos y lo autenticamos con su contraseña"""
        user = self.find_user(username)
        if user is not None:
            pass_salt = base64.b64decode(user['password_salt'].encode('utf-8'))
            kdf= Scrypt(
                salt = pass_salt,
                length =32,
                n= 2**14,
                r=8,
                p=1
            )
            token1 = base64.b64decode(user['password_token'].encode('utf-8'))
            try:
                coded_pass = password.encode('utf-8')
                kdf.verify(coded_pass, token1)
                return True
            except Exception as e:
                return False
        else:
            return None

    def register_user(self, user=dict):
        self.add_store(user)
        self.save_store()
    def user_data(self, username):
        user = self.find_user(username)
        Store = KeysStore()
        key = Store.key_decryption(username)
        nombre_decodificado = base64.b64decode(user['name'].encode('utf-8'))
        tarjeta_decodificada = base64.b64decode(user['creditcard'].encode('utf-8'))
        nonce_nombre =  base64.b64decode(user["name_nonce"].encode('utf-8'))
        nombre = self.decrypt(key, None, nonce_nombre, nombre_decodificado)
        tarjeta_nonce = base64.b64decode(user["creditcard_nonce"].encode('utf-8'))
        tarjeta = self.decrypt(key, None, tarjeta_nonce, tarjeta_decodificada)
        return User(username, nombre, tarjeta)
    def decrypt(self, key, aad, nonce, dato):
        chacha = ChaCha20Poly1305(key)
        return chacha.decrypt(nonce, dato, aad)