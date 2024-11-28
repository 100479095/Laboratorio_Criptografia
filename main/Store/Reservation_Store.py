import json
from Store.json_store import JsonStore

STORE_NAME= "Reservations.json"
class ReservationStore(JsonStore):

    def __init__(self):
        super().__init__(STORE_NAME)
        self.load_store()

    def find_reserva(self, ID, hora):
        for user in self.data_list:
            if user["id"] == ID and user["hora"] == hora:
                return user
        return None
    def reservar(self, ID, hora):
        reserva = self.find_reserva(ID, hora)
        if reserva == None:
            data = {"id": ID, "hora": hora}
            self.add_store(data)
            self.save_store()
            return True
        else:
            return False