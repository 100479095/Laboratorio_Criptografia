import json, os
import base64
from tkinter import messagebox

from Store.json_store import JsonStore
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography import x509
from Keys.Key import Private_Password
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from cryptography.hazmat.primitives.hashes import SHA256

PRIVATE_KEY_PATH = os.path.join(os.path.dirname(__file__), '../Keys/private_key.pem')
CERTIFICATE_PATH = os.path.join(os.path.dirname(__file__), '../Keys/02.pem')
AC1_PATH = os.path.join(os.path.dirname(__file__), '../Keys/AC1/ac1cert.pem')

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
    def reservar(self, user, ID, hora):
        reserva = self.find_reserva(ID, hora)
        if reserva == None:
            message = f"El usuario {user.username} ha reservado la cancha con ID {ID} a las {hora}:00 horas".encode(
                'utf-8')
            firma = self.firma_reserva(message)
            firma_64 = base64.b64encode(firma).decode('utf-8')
            data = {"user": user.username,"id": ID, "hora": hora, "user_signature": firma_64}
            self.add_store(data)
            self.save_store()
            if self.verificar_firma(user, ID, hora):
                return True
            else:
                messagebox.showerror("Error de verificación de reserva", "Verificación de firma no válida")
        else:
            return False

    def firma_reserva(self, message):
        with open(PRIVATE_KEY_PATH, "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=Private_Password,
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

    def verificar_firma(self, user, ID, hora):
        with open(CERTIFICATE_PATH, "rb") as cert_file:
            cert = x509.load_pem_x509_certificate(cert_file.read())

        self.verificar_certificado(cert)
        reserva = False
        self.load_store()
        for usuario in self.data_list:
            if (usuario["user"] == user.username) and (usuario["id"] == ID) and (usuario["hora"] == hora):
                reserva = True
                firma = base64.b64decode(usuario["user_signature"].encode('utf-8'))
        if reserva==True:
            message = f"El usuario {user.username} ha reservado la cancha con ID {ID} a las {hora}:00 horas".encode(
                'utf-8')
            public_key = cert.public_key()
            public_key.verify(
                firma,
                message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        else:
            return False

    def verificar_certificado(self, cert):
        #Cargamos el certificado de AC1 y su clave pública
        with open(AC1_PATH, "rb") as cert_file:
            ac1_cert = x509.load_pem_x509_certificate(cert_file.read())

        # verificamos el certificado del sistema
        ac1_public_key = ac1_cert.public_key()
        tbs_certificate = cert.tbs_certificate_bytes
        signature = cert.signature
        ac1_public_key.verify(
            signature,
            tbs_certificate,
            padding.PKCS1v15(),
            hashes.SHA1()
        )

        # verificamos el certificado de ac1
        tbs_certificate = ac1_cert.tbs_certificate_bytes
        signature = ac1_cert.signature
        ac1_public_key.verify(
            signature,
            tbs_certificate,
            padding.PKCS1v15(),
            hashes.SHA1()
        )
        return True
