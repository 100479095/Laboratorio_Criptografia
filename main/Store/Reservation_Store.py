import json
from json_store import JsonStore

STORE_NAME= "Reservations.json"
class ReservationStore(JsonStore):

    def __init__(self):
        super().__init__(STORE_NAME)

    def load_store(self):
        """ Leo los datos del fichero si existe , y si no existe creo una lista vacia"""
        try:
            with open(self._file_name, "r", encoding="utf-8", newline="") as file:
                self._data_list = json.load(file)
        except FileNotFoundError:
            self._data_list = []
        except json.JSONDecodeError:
            raise FileNotFoundError("The file doesn't exist")

        return self._data_list

    def save_store(self):
        """Subimos al almacen los datos"""
        try:
            with open(self._file_name, "w", encoding="utf-8", newline="") as file:
                json.dump(self._data_list, file, indent=2)
        except FileNotFoundError:
            raise FileNotFoundError("The file doesn't exist")