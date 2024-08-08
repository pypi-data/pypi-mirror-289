import requests


def business_to_business(base_url, token, merchant_code, network_code, receiver_merchant_code, amount, description, merchant_reference, account_reference, receiver_account_type, callback_url):
    url = f'{base_url}/api/v1/payments/b2b/'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    payload = {
        "MerchantCode": merchant_code,
        "MerchantTransactionReference": merchant_reference,
        "Currency": "KES",
        "Amount": amount,
        "ReceiverMerchantCode": receiver_merchant_code,
        "AccountReference": account_reference,
        "ReceiverAccountType": receiver_account_type,
        "NetworkCode": network_code,
        "CallBackURL": callback_url,
        "Reason": description
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()
