import requests

from config import settings


def create_payment(amount, currency):
    endpoint = 'https://api.stripe.com/v1/payment_intents'
    headers = {'Authorization': f'Bearer {settings.STRIPE_SECRET_KEY}'}
    data = {
        'amount': amount,
        'currency': currency,
        'payment_method': 'card'
    }

    response = requests.post(endpoint, headers=headers, data=data)
    return response.json()['id']


def make_payment(bill_id, number, exp_month, exp_year, cvc):
    endpoint = 'https://api.stripe.com/v1/payment_methods'
    headers = {'Authorization': f'Bearer {settings.STRIPE_SECRET_KEY}'}
    data = {
        'type': 'card',
        'card[number]': number,
        'card[exp_month]': exp_month,
        'card[exp_year]': exp_year,
        'card[cvc]': cvc,

    }

    response = requests.post(endpoint, headers=headers, data=data)
    payment_method_id = response.json()['id']

    endpoint = f'https://api.stripe.com/v1/payment_intents/{bill_id}/confirm'
    headers = {'Authorization': f'Bearer {settings.STRIPE_SECRET_KEY}'}
    data = {
        'payment_method': payment_method_id
    }

    response = requests.post(endpoint, headers=headers, data=data)
    return response.json()['status']


def retrieve_payment(payment_id: str):
    endpoint = f'https://api.stripe.com/v1/payment_intents/{payment_id}'
    headers = {'Authorization': f'Bearer {settings.STRIPE_SECRET_KEY}'}

    response = requests.get(endpoint, headers=headers)
    return response.json()
