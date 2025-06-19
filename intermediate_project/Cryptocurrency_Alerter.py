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
    data = requests.get(BASE_URL, params=payload)
    json: dict = data.json()

    for item in json:
        current_coin: Coin = Coin(name=item.get('name'),
                                  symbol=item.get('symbol'),
                                  current_price=item.get('current_price'))
        
        coin_list.append(current_coin)

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
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print("Current Time =", current_time)
        alert('btc', bottom=9000000, top=10000000, coins_list= coins)
        time.sleep(2)
        coin_list.clear()
        print("----")
#        for coin in coins:
#            print(coin)
