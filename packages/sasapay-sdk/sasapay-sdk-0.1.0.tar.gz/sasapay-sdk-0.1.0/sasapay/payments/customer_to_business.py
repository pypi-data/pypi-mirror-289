import requests


def customer_to_business(base_url, token, merchant_code, network_code, phone_number, amount, description, account_reference, callback_url):

    url = f'{base_url}/api/v1/payments/request-payment/'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    payload = {
        "MerchantCode": merchant_code,
        "NetworkCode": network_code,
        "TransactionFee": "0",
        "Currency": "KES",
        "Amount": amount,
        "PhoneNumber": phone_number,
        "TransactionDesc": description,
        "AccountReference": account_reference,
        "CallBackURL": callback_url
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()
