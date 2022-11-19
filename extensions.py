import requests
import json
from config import currency


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        try:
            quote_ticker = currency[quote]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {quote}.")

        try:
            base_ticker = currency[base]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {base}.")

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f"Не удалось обработать количество {amount}.")

        if quote == base:
            raise APIException(f"Невозможно перевести одинаковые валюты {base}.")

        request = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
        total_base = json.loads(request.content)[currency[base]]
        total_base = total_base * amount

        return total_base
