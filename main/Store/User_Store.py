import base64
import json
from Store.json_store import JsonStore
from Classes.User import User
import struct, os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from Keys.Key import ChaChaKey
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

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
            kdf= Scrypt(
                salt = user["password_salt"],
                length =32,
                n= 2**14,
                r=8,
                p=1
            )
            token1 = user["password_token"]
            kdf.verify(base64.b64decode(password.encode()), token1)
           #if user["password"] == password:
               #return (User(user["username"], user["password"], user["name"], user["creditcard"]))
        #else:
            #return None

    def register_user(self, user=dict):
        self.add_store(user)
        self.save_store()