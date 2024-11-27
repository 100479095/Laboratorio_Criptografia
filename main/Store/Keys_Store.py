import json
import os
from Store.json_store import JsonStore
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
import base64

STORE_NAME= "Keys.json"
class KeysStore(JsonStore):
    def __init__(self):
        super().__init__(STORE_NAME)
        self.load_store()

    def find_user_key(self, username):
        """"Buscamos en la base de datos al usuario con el username dado y lo devolvemos, de no existir
        devolvemos None"""
        for user in self.data_list:
            if user["username"] == username:
                return user["key"]
        return None

    def find_user_nonce(self, username):
        """"Buscamos en la base de datos al usuario con el username dado y lo devolvemos, de no existir
        devolvemos None"""
        for user in self.data_list:
            if user["username"] == username:
                return user["key_nonce"]
        return None

    def key_encryption(self, username, key):
        from Keys.Key import ChaChaKey
        json_key = {}
        nonce = os.urandom(12)

        cypher_key = self.encrypt(ChaChaKey, None, nonce, key)
        json_key['username'] = username
        json_key['key'] = base64.b64encode(cypher_key).decode('utf-8')
        json_key['key_nonce'] = base64.b64encode(nonce).decode('utf-8')

        self.registration_key(json_key)
    def encrypt(self, key, aad, nonce, dato):
        chacha = ChaCha20Poly1305(key)
        return chacha.encrypt(nonce, dato, aad)
    def key_decryption(self, user):
        from Keys.Key import ChaChaKey
        user_key = self.find_user_key(user)
        key_nonce = self.find_user_nonce(user)
        key = base64.b64decode(user_key.encode('utf-8'))
        nonce = base64.b64decode(key_nonce.encode('utf-8'))
        return self.decrypt(ChaChaKey, None, nonce, key)
    def decrypt(self, key, aad, nonce, dato):
        chacha = ChaCha20Poly1305(key)
        return chacha.decrypt(nonce, dato, aad)

    def registration_key(self, json_key=dict):
        self.add_store(json_key)
        self.save_store()