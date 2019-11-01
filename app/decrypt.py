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
        original_data = self.private_key.decrypt(
            encrypted_value,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return original_data

    def apply_decrypt(self, encrypted):
        decrypted = {}
        if isinstance(dict, encrypted):
            for key, value in encrypted.items():
                result = self.decrypt_value(value)
                decrypted[key] = result
        return decrypted


# generate private_key
    # save key on certificates folder
# generate public_key
    # save key on certificates folder
# encrypt with public_key
    # receive dict and encrypt
# dencrypt with public_key
    # receive dict and encrypt

# ter as chaves geradas localmente e aplicar a criptografia com a public
# ter as chaves geradas localmente e aplicar a decriptografia com a privada