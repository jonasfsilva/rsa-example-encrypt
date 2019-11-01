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
        encrypted_value = self.public_key.encrypt(
            value,
            padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
            )
        )
        return encrypted_value

    def apply_encrypt(self, decrypted):
        decrypted = {}
        if isinstance(dict, decrypted):
            for key, value in decrypted.items():
                result = self.encrypt_value(value)
                decrypted[key] = result
        return decrypted
