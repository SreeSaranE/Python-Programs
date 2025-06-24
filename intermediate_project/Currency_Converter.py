import requests
from typing import Final
import json
import datetime

API_KEY: Final[str] = 'bf8f82bf9880f304078eb9bc83de32fe'
Base_URL: Final[str] = 'http://api.exchangeratesapi.io/v1/latest'

def get_rates() -> dict:
    with open('rates.json', 'r') as file:
        data =  json.load(file)
        old_date = data["date"]
        today = str(datetime.date.today())
        old_string = old_date.replace("-", "")
        today_string = today.replace("-", "")
        if old_string < today_string:
            payload: dict = {'access_key': API_KEY}
            request = requests.get(url=Base_URL, params=payload)
            web_data: dict = request.json()
            with open('rates.json', 'w') as file:
                json.dump(web_data, file)
            rate = data.get('rates')
            return rate
        else:
            rate = data.get('rates')
            return rate

def get_currency(currency: str, rates: dict):
    if currency in rates.keys():
        return (rates[currency])
    else:
        raise ValueError(f"{currency} is not a valid Currency!")
    
def convert_currency(amount: float, base: str, vs: str, rates: dict):
    base_rate: float = get_currency(base, rates)
    vs_rate: float = get_currency(vs, rates)
    conver: float = round((vs_rate/base_rate)*amount,2)
    print(f"{amount:,.2f} {base} = {conver:,.2f} {vs}")

def main():
    data = get_rates()
    while True:
        try:
            amount = int(input("Enter the amount: "))
        except ValueError:
            print("Enter a valid Currency!")
        else:
            break

    base_curr = (input("Enter base Currency: ")).upper()
    vs_curr = (input("Enter vs Currency: ")).upper()
    while True:
        if base_curr not in data.keys():
            base_curr = (input("Enter a valid base Currency: ")).upper()
        elif vs_curr not in data.keys():
            vs_curr = (input("Enter a valid vs Currency: ")).upper()
        else:
            break

    convert_currency(amount, base_curr, vs_curr, data)

if __name__ == '__main__':
    main()
