import json
from json_store import JsonStore

STORE_NAME= "Reservations.json"
class ReservationStore(JsonStore):

    def __init__(self):
        super().__init__(STORE_NAME)