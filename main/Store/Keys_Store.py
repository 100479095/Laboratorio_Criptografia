import json
from Store.json_store import JsonStore
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
import base64

STORE_NAME= "Keys.json"
class KeysStore(JsonStore):
    def __init__(self):
        super().__init__(STORE_NAME)
        self.load_store()

    def key_encryption(self, username, key):
        from Keys.Key import ChaChaKey
        from Keys.Key import ChaChaNonce
        json_key = {}

        cypher_key = self.encrypt(ChaChaKey, None, ChaChaNonce, key)
        json_key['username'] = username
        json_key['key'] = base64.b64encode(cypher_key).decode('utf-8')

        self.registration_key(json_key)
    def encrypt(self, key, aad, nonce, dato):
        chacha = ChaCha20Poly1305(key)
        return chacha.encrypt(nonce, dato, aad)

    def registration_key(self, json_key=dict):
        self.add_store(json_key)
        self.save_store()