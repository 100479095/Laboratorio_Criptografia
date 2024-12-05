import struct, os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from Key import Private_Password as password
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes

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
#creamos el CSR
csr = (x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
    #Rellenamos los detalles de nuestra compañia
    x509.NameAttribute(NameOID.COUNTRY_NAME, "ES"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Madrid"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, "Leganes"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Tu Cancha Padel"),
    x509.NameAttribute(NameOID.COMMON_NAME, "tucanchapadel.com"),
])).sign(private_key, hashes.SHA256()))

with open("csr.pem", "wb") as f:
    f.write(csr.public_bytes(serialization.Encoding.PEM))

""""
.add_extension(
    x509.SubjectAlternativeName([
        # Describe what sites we want this certificate for.
        x509.DNSName("tucanchapadel.com"),
        x509.DNSName("www.tucanchapadel.com"),
        x509.DNSName("subdomain.tucanchapadel.com"),
    ]),
    critical=False,
#Firmamos el CSR con nuestra clave privada.
).sign(private_key, hashes.SHA256()))


public_key = private_key.public_key()
public_pem = public_key.public_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PublicFormat.SubjectPublicKeyInfo
)

with open("public_key.pem", "wb") as pem_file:
    pem_file.write(public_pem)
"""