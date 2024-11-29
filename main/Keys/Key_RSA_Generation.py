import struct, os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from Key import Private_Password as password

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)


private_pem = private_key.private_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PrivateFormat.PKCS8,
   encryption_algorithm=serialization.BestAvailableEncryption(password)
)

with open("private_key.pem", "wb") as pem_file:
    pem_file.write(private_pem)

public_key = private_key.public_key()
public_pem = public_key.public_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PublicFormat.SubjectPublicKeyInfo
)

with open("public_key.pem", "wb") as pem_file:
    pem_file.write(public_pem)