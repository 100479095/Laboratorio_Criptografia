import os
import json

JSON_PATH = os.path.join(os.path.dirname(__file__), '../Database/')
class JsonStore:
    def __init__(self, store_name):
        self._file_name = JSON_PATH + store_name
        self._data_list = []

    def load_store(self):
        """ Leo los datos del fichero si existe , y si no devuelvo un error"""
        try:
            with open(self._file_name, "r", encoding="utf-8", newline="") as file:
                self._data_list = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("The file doesn't exist")
        except json.JSONDecodeError:
            raise TypeError("Wrong JSON Format")

        return self._data_list

    def save_store(self):
        """Subimos al almacen los datos"""
        try:
            with open(self._file_name, "w", encoding="utf-8", newline="") as file:
                json.dump(self._data_list, file, indent=2)
        except FileNotFoundError:
            raise FileNotFoundError("The file doesn't exist")

    def add_store(self, object):
        """Agregamos a la lista el objeto que queremos guardar"""
        self._data_list.append(object.__dict__)

    @property
    def data_list(self):
        return self._data_list
