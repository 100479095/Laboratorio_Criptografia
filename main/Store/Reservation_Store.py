import json, os
import base64
from Store.json_store import JsonStore
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

JSON_PATH = os.path.join(os.path.dirname(__file__), '../Keys/private_key.pem')

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
            message = f"Usted ha reservado la cancha con ID {ID} a las {hora}:00 horas".encode(
                'utf-8')
            firma = self.firma_reserva(message)
            self.verificar_firma(firma)
            firma_64 = base64.b64encode(firma).decode('utf-8')
            data = {"id": ID, "hora": hora, "user_signature": firma_64}
            self.add_store(data)
            self.save_store()
            return True
        else:
            return False

    def firma_reserva(self, message):
        with open(JSON_PATH, "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
            )
        signature = private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature




