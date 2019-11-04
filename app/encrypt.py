import base64
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


class Encrypt:
    
    public_key = None
    key_filename = 'certificates/public_key.pem'

    def __init__(self, key_filename=None):
        if key_filename:
            self.key_filename = key_filename

    def load_publickey_from_file(self):
        with open(self.key_filename, "rb") as key_file:
            self.public_key = serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
            )
            return self.public_key

    def encrypt_value(self, value):
        # TODO receive str | return bytes (b64)
        encrypted_value = self.public_key.encrypt(
            value.encode('utf-8'),
            padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
            )
        )
        b64value = base64.b64encode(encrypted_value)
        return b64value


def encrypt_card_data(holder, number, cvv):
    enc_instance = Encrypt()
    enc_instance.load_publickey_from_file()
    encrypted_card_data = {
        "number": enc_instance.encrypt_value(number),
        "holder": enc_instance.encrypt_value(holder),
        "cvv": enc_instance.encrypt_value(cvv)
    }
    
    return encrypted_card_data
