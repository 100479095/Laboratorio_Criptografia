import json
from Store.json_store import JsonStore
from Classes.User import User
import struct, os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from Keys.Key import ChaChaKey

STORE_NAME= "Keys.json"
class UserStore(JsonStore):

    def __init__(self):
        super().__init__(STORE_NAME)
        self.load_store()