import json
from json_store import JsonStore

STORE_NAME= "Firmas.json"
class FirmasStore(JsonStore):
    def __init__(self):
        super().__init__(STORE_NAME)
        self.load_store()
