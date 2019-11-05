import unittest
import requests
import tempfile


class TestAPIEncrypt(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://temcriptografia:5000/api/v1/"
        self.encrypt_data_url = "encrypt-card"

    def test_can_encrypt_card_data(self):
        card_data = {
            "number": "378282246310005",
            "holder": "Teste da Silva",
            "cvv": "277"
        }
        response = requests.post(f"{self.base_url}{self.encrypt_data_url}", json=card_data)
        response_json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response_json.get("number"), card_data.get('number'))
        self.assertNotEqual(response_json.get("holder"), card_data.get('number'))
        self.assertNotEqual(response_json.get("cvv"), card_data.get('number'))

    def test_cant_encrypt_card_data_without_send_data(self):
        card_data = {}
        response = requests.post(f"{self.base_url}{self.encrypt_data_url}", json=card_data)
        self.assertEqual(response.status_code, 400)

    def test_cant_encrypt_card_data_with_invalid_data(self):
        card_data = {
            "number": 1214654,
            "cvv": 11111
        }
        response = requests.post(f"{self.base_url}{self.encrypt_data_url}", json=card_data)
        self.assertEqual(response.status_code, 400)


class TestAPIDencrypt(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://temcriptografia:5000/api/v1/"
        self.base_endpoint = "decrypt-card"
        self.original_card_data = {
            "number": "378282246310005",
            "holder": "Teste da Silva",
            "cvv": "277"
        }
        encrypt_data_url = "encrypt-card"
        response = requests.post(f"{self.base_url}{encrypt_data_url}", json=self.original_card_data)
        self.response_json = response.json()

    def test_can_decrypt_card_data(self):
        card_data = self.response_json
        response = requests.post(f"{self.base_url}{self.base_endpoint}", json=card_data)
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_json.get('number'), self.original_card_data.get('number'))
        self.assertEqual(response_json.get('holder'), self.original_card_data.get('holder'))
        self.assertEqual(response_json.get('cvv'), self.original_card_data.get('cvv'))

    def test_cant_decrypt_card_data_without_send_data(self):
        card_data = {}
        response = requests.post(f"{self.base_url}{self.base_endpoint}", json=card_data)
        self.assertEqual(response.status_code, 400)

    def test_cant_decrypt_card_data_with_invalid_data(self):
        card_data = {}
        response = requests.post(f"{self.base_url}{self.base_endpoint}", json=card_data)
        self.assertEqual(response.status_code, 400)

    def test_cant_decrypt_card_data_with_invalid_hash(self):
        card_data = {
            "number": "1111222233334444",
            "holder": "Teste da Silva",
            "cvv": "277"
        }
        response = requests.post(f"{self.base_url}{self.base_endpoint}", json=card_data)
        print(response.content)
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
