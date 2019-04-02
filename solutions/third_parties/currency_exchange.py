import requests

api_entrypoint = 'https://api.exchangeratesapi.io/latest'
response = requests.get(api_entrypoint)

response = response.json()
exchange_rate = response['rates']['CAD']

eur2cad = 5 * exchange_rate
print(eur2cad)
