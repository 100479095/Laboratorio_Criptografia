import json
from json_store import JsonStore

STORE_NAME= "Users.json"
class UserStore(JsonStore):

    def __init__(self):
        super().__init__(STORE_NAME)

