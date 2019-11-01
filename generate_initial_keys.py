from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization


def generate_privatekey():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    return private_key

def generate_pubkey(private_key):
    public_key = private_key.public_key()
    return public_key

def make_privatekey_pem(private_key):
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    return pem

def make_pubkey_pem(public_key):
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return pem

def save_pem_on_file(content, filename='private_key.pem'):
    with open("certificates/{}".format(filename), 'wb') as f:
        f.write(content)


if __name__ == "__main__":
    private_key = generate_privatekey()
    public_key = generate_pubkey(private_key)
    private_pem = make_privatekey_pem(private_key)
    public_pem = make_pubkey_pem(public_key)
    save_pem_on_file(private_pem, 'private_key.pem')
    save_pem_on_file(public_pem, 'public_key.pem')



