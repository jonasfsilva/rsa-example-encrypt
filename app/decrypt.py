import base64
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


class Decrypt:

    private_key = None
    key_filename = 'certificates/private_key.pem'

    def __init__(self, key_filename=None):
        if key_filename:
            self.key_filename = key_filename
        
    def load_privatekey_from_file(self):
        with open(self.key_filename, "rb") as key_file:
            self.private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )
        return self.private_key

    def decrypt_value(self, encrypted_value):
        # TODO receive bytes (b64)| return str
        b64value = base64.b64decode(encrypted_value)
        original_data = self.private_key.decrypt(
            b64value,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return bytes.decode(original_data)


def decrypt_card_data(holder, number, cvv):
    dec_instance = Decrypt()
    dec_instance.load_privatekey_from_file()
    
    encrypted_card_data = {
        "number": dec_instance.decrypt_value(number),
        "holder": dec_instance.decrypt_value(holder),
        "cvv": dec_instance.decrypt_value(cvv)
    }
    
    return encrypted_card_data
