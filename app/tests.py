import unittest
import requests
import tempfile
from decrypt import Decrypt
from encrypt import Encrypt


class TestDecrypt(unittest.TestCase):

    def setUp(self):
        self.decrypt_instance = Decrypt()

    def test_can_load_private_key(self):
        private_key = self.decrypt_instance.load_privatekey_from_file()
        # private_key = generate_privatekey()
        print(private_key)
        self.assertTrue(private_key)

    def test_can_decrypt_single_value(self):
        # private_key = generate_privatekey()
        # pem_file = save_private_key(private_key, 'test_private_key.pem')
        # print(pem_file)
        self.assertTrue(False)

    def test_can_apply_full_decrypt(self):
        self.assertTrue(False)
    
    def test_cant_generate_pubkey_without_private_key(self):
        self.assertTrue(False)
    #     pass
    
    def test_can_encrypt_dict_values_with_publickey(self):
        self.assertTrue(False)
    

class TestEncrypt(unittest.TestCase):

    def setUp(self):
        self.encrypt_instance = Encrypt()

    def test_can_load_public_key(self):
        private_key = self.encrypt_instance.load_publickey_from_file()
        # private_key = generate_privatekey()
        print(private_key)
        self.assertTrue(private_key)


if __name__ == '__main__':
    unittest.main()
