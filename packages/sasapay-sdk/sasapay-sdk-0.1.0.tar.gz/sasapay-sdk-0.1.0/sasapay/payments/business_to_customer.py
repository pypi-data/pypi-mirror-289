import requests


def business_to_customer(base_url, token, merchant_code, channel, receiver_account_number, amount, description, merchant_reference, callback_url):
    url = f'{base_url}/api/v1/payments/b2c/'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    payload = {
        "MerchantCode": merchant_code,
        "MerchantTransactionReference": merchant_reference,
        "Currency": "KES",
        "Amount": amount,
        "ReceiverNumber": receiver_account_number,
        "Channel": channel,
        "CallBackURL": callback_url,
        "Reason": description
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()
