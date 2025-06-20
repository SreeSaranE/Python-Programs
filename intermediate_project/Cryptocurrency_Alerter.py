from dataclasses import dataclass
from typing import Final
import requests
import time

BASE_URL: Final[str] = "https://api.coingecko.com/api/v3/coins/markets"

@dataclass
class Coin:
    name: str
    symbol: str
    current_price: float

    def __str__(self):
        return f"{self.name}({self.symbol}): {self.current_price:,}"

def get_coins() -> list[Coin]:
    coin_list = []
    payload: dict = {'vs_currency': 'inr', 'order': 'market_cap_desc'}
    try:
        response = requests.get(BASE_URL, params=payload)
        response.raise_for_status()
        data = response.json()

        if isinstance(data, list):
            for item in data:
                current_coin = Coin(
                    name=item.get('name'),
                    symbol=item.get('symbol'),
                    current_price=item.get('current_price')
                )
                coin_list.append(current_coin)
        else:
            print("Unexpected API response:", data)

    except requests.RequestException as e:
        print("Request failed:", e)
    except ValueError as e:
        print("JSON decode error:", e)

    return coin_list

def alert(symbol: str, bottom: float, top: float, coins_list: list[Coin]):
    for coin in coins_list:
        if coin.symbol == symbol:
            if coin.current_price > top or coin.current_price < bottom:
                print(coin, "Trigger")
            else:
                print(coin, "Nothing")

if __name__ == '__main__':
    while True:
        coin_list = []
        coins = get_coins()
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print("Current Time =", current_time)
        alert('btc', bottom=9000000, top=10000000, coins_list= coins)
        alert('eth', bottom=9000000, top=10000000, coins_list= coins)
        print("----")
        time.sleep(10)
