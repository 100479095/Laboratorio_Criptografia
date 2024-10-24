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
                kdf.verify(password.encode('utf-8'), token1)

            except Exception as e:
                print("PETÓ")
           #if user["password"] == password:
               #return (User(user["username"], user["password"], user["name"], user["creditcard"]))
        #else:
            #return None

    def register_user(self, user=dict):
        self.add_store(user)
        self.save_store()