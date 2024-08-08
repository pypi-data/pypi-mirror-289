from .auth.authentication import authenticate
from .payments.customer_to_business import customer_to_business
from .payments.business_to_customer import business_to_customer
from .payments.business_to_business import business_to_business


class SasaPayAPI:
    def __init__(
            self,
            environment='sandbox',
            client_id=None,
            client_secret=None,
            sandbox_base_url='https://sandbox.sasapay.app',
            production_base_url='https://api.sasapay.app'):

        self.environment = environment
        self.client_id = client_id
        self.client_secret = client_secret
        self.sandbox_base_url = sandbox_base_url
        self.production_base_url = production_base_url
        self.access_token = None
        self.base_url = sandbox_base_url if environment == 'sandbox' else production_base_url

    def authenticate(self):
        self.access_token = authenticate(
            self.base_url, self.client_id, self.client_secret)
        return self.access_token

    def customer_to_business(self, merchant_code, network_code, phone_number, amount, description, account_reference, callback_url):
        return customer_to_business(self.base_url, self.access_token, merchant_code, network_code, phone_number, amount, description, account_reference, callback_url)

    def business_to_customer(self, merchant_code, channel, receiver_account_number, amount, description, merchant_reference, callback_url):
        return business_to_customer(self.base_url, self.access_token, merchant_code, channel, receiver_account_number, amount, description, merchant_reference, callback_url)

    def business_to_business(self, merchant_code, network_code, receiver_merchant_code, amount, description, merchant_reference, account_reference, receiver_account_type, callback_url):
        return business_to_business(self.base_url, self.access_token, merchant_code, network_code, receiver_merchant_code, amount, description, merchant_reference, account_reference, receiver_account_type, callback_url)


__all__ = ['SasaPayAPI']
