import pyupbit
from pyupbit import Upbit, get_current_price, get_orderbook
# https://github.com/sharebook-kr/pyupbit
import datetime
from sys import exit
from time import sleep
from functools import partial

access = "0g02ZSPdlROwD5ydXpND9OTblVe7mVJoE2cbGzv5"
secret = 'YYSSzfolyXX0NNEWUSTOdDm8rJhd6YoOuYVyphah'

# def withdraw(self, currency, amount, address, contain_req=False, transaction_type="default"):
#     try:
#         url = "https://api.upbit.com/v1/withdraws/coin"
#         data = {'currency': currency,
#                 'amount': amount,
#                 'address': address,
#                 'transaction_type': transaction_type}
#
#         headers = self._request_headers(data)
#         result = _send_post_request(url, headers=headers, data=data)
#         if contain_req:
#             return result
#         else:
#             return result[0]
#     except Exception as x:
#         print(x.__class__.__name__)
#         return None
#
# def withdraw_info(self, currency, contain_req=False):
#     try:
#         url = "https://api.upbit.com/v1/withdraws/chance"
#         data = {'currency': currency}
#
#         headers = self._request_headers(data)
#         result = _send_post_request(url, headers=headers, data=data)
#         if contain_req:
#             return result
#         else:
#             return result[0]
#     except Exception as x:
#         print(x.__class__.__name__)
#         return None

upbit = Upbit(access, secret)


Symbol = {"key1": "BTC", "key2": "XRP"}

# bid 는 주식에 매수자가 주식에 기꺼이 지불하려고 하는 최대 금액 : 내가 팔때의 가격
# ask 는 주식 소유자가 판매하고자 하는 최소 금액 : 내가 살때의 가격
# ask 는 bid 보다 약간 높음.
# The price : 마지막 매매가 /  ask or buy 둘 다 가능
from pyupbit.request_api import _send_get_request, _send_post_request, _send_delete_request

print(get_orderbook(f"KRW-{Symbol['key2']}")[0]["orderbook_units"][1]["ask_price"])
print(upbit.get_balances())
# print(upbit.get_chance('KRW-BTC'))
print(upbit.withdraw_chance(currency='KRW'))
print(upbit.deposit_list())
print(upbit.deposit_("BTC"))
