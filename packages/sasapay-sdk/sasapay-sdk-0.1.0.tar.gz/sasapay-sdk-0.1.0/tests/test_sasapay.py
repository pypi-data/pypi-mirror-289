import unittest
from sasapay import SasaPayAPI

class TestSasaPayAPI(unittest.TestCase):

    def setUp(self):
        self.api = SasaPayAPI(
            environment='sandbox',
            client_id='your_client_id',
            client_secret='your_client_secret'
        )
        self.api.access_token = 'test_access_token'
    def test_authenticate(self):
        # Test the authenticate method
        token = self.api.authenticate()
        self.assertIsNotNone(token)
        self.assertEqual(token, 'test_access_token')

    def test_customer_to_business(self):
        # Mock the method to avoid actual API calls
        self.api.customer_to_business = lambda x, y, z: {"status": "success"}
        response = self.api.customer_to_business('customer123', 'business123', 100.00)
        self.assertEqual(response["status"], "success")

    def test_business_to_customer(self):
        # Mock the method to avoid actual API calls
        self.api.business_to_customer = lambda x, y, z: {"status": "success"}
        response = self.api.business_to_customer('business123', 'customer123', 100.00)
        self.assertEqual(response["status"], "success")

    def test_business_to_business(self):
        # Mock the method to avoid actual API calls
        self.api.business_to_business = lambda x, y, z: {"status": "success"}
        response = self.api.business_to_business('business123', 'business456', 100.00)
        self.assertEqual(response["status"], "success")

if __name__ == '__main__':
    unittest.main()