import unittest
import requests
import tempfile
from decrypt import Decrypt
from encrypt import Encrypt
from encrypt import encrypt_card_data
from decrypt import decrypt_card_data 


class TestEncrypt(unittest.TestCase):

    def setUp(self):
        self.encrypt_instance = Encrypt()

    def test_can_load_public_key(self):
        public_key = self.encrypt_instance.load_publickey_from_file()
        self.assertTrue(public_key)
    
    def test_can_encrypt_single_value(self):        
        self.encrypt_instance.load_publickey_from_file()
        card_number = "5001222244446666"
        encrypted_card_number = self.encrypt_instance.encrypt_value(card_number)
        self.assertNotEqual(card_number, encrypted_card_number)
    
    def test_can_encrypt_all_card_data(self):
        number = "5001222244446666"
        holder = "Teste Ferreira da Silva"
        cvv = "988"
        encrypted_card_data = encrypt_card_data(holder, number, cvv)
        self.assertNotEqual(encrypted_card_data['number'], number)
        self.assertNotEqual(encrypted_card_data['holder'], holder)
        self.assertNotEqual(encrypted_card_data['cvv'], cvv)


class TestDecrypt(unittest.TestCase):
    
    def setUp(self):
        self.encrypt_instance = Encrypt()
        self.decrypt_instance = Decrypt()

    def test_can_load_private_key(self):
        private_key = self.decrypt_instance.load_privatekey_from_file()
        self.assertTrue(private_key)

    def test_can_decrypt_single_value(self):
        self.encrypt_instance.load_publickey_from_file()
        self.decrypt_instance.load_privatekey_from_file()

        card_number = "5001222244446666"
        encrypted_card_number = self.encrypt_instance.encrypt_value(card_number)
        decrypted_card_number = self.decrypt_instance.decrypt_value(
            encrypted_card_number)
        self.assertEqual(card_number, decrypted_card_number)

    def test_can_apply_full_decrypt(self):
        number = "5001222244446666"
        holder = "Teste Ferreira da Silva"
        cvv = "988"
        encrypted_card_data = encrypt_card_data(holder, number, cvv)

        enc_holder = encrypted_card_data['holder']
        enc_number = encrypted_card_data['number']
        enc_cvv = encrypted_card_data['cvv']

        decrypted_card_data = decrypt_card_data(enc_holder, enc_number, enc_cvv)
        self.assertEqual(number, decrypted_card_data['number'])
        self.assertEqual(holder, decrypted_card_data['holder'])
        self.assertEqual(cvv, decrypted_card_data['cvv'])


if __name__ == '__main__':
    unittest.main()
