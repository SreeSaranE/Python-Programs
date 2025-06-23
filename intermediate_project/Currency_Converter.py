import requests
from typing import Final
import json

API_KEY: Final[str] = 'b3f448b3037e176b79d4efd637ec8781'
Base_URL: Final[str] = 'http://api.exchangeratesapi.io/v1/latest'

def get_rates(mock: bool = False) -> dict:
    if mock:
        with open('rates.json', 'r') as file:
            return json.load(file)
    
    payload: dict = {'access_key': API_KEY}
    request = requests.get(url=Base_URL, params=payload)
    data: dict = request.json()
    with open('rates.json', 'w') as file:
        json.dump(data, file)
    return data

def get_currency(currency: str, rates: dict):
    currency: str = currency.upper()
    if currency in rates.keys():
        return (rates.get(currency))
    else:
        raise ValueError(f"{currency} is not a valid Currency!")
    
def convert_currecy(amount: float, base: str, vs: str, rates: dict):
    base_rate: float = get_currency(base, rates)
    vs_rate: float = get_currency(vs, rates)
    conver: float = round((vs_rate/base_rate)*amount,2)
    print(f"{amount:,.2f} {base} = {conver:,.2f} {vs}")

def main():
    data = get_rates(mock=True)
    rate = data.get('rates')
    amount = int(input("Enter the amount: "))
    base_curr = input("Enter base Currency: ")
    vs_curr = input("Enter vs Currency: ")
    convert_currecy(amount, base_curr, vs_curr, rate)

if __name__ == '__main__':
    main()
