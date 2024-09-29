import os
import json

JSON_PATH = os.path.join(os.path.dirname(__file__), '../Database/')
class JsonStore:
    def __init__(self, store_name):
        self._file_name = JSON_PATH + store_name
        self._data_list = []