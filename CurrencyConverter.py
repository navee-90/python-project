import requests

url = "https://api.exchangerate-api.com/v4/latest/USD"  # Base currency: USD
response = requests.get(url).json()

from_currency = input("From currency (e.g., USD): ").upper()
to_currency = input("To currency (e.g., EUR): ").upper()
amount = float(input("Enter amount: "))

rate = response["rates"].get(to_currency, None)
if rate:
    converted_amount = amount * rate
    print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
else:
    print("Invalid currency code!")
