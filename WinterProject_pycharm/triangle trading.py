# class TAT:
#     def __init__(self, mode, val1="BTC", val2="XRP"):
#         self.mode = mode
#         self.Symbol = {"key1": val1, "key2": val2}
#
#     def trade(self):
#
#         Option = self.mode
#         Symbol = self.Symbol
#
#         req_iterate = 0
#         if Option == 1:
#             while True:
#                 sleep(0.1)
#                 # print(upbit.get_balance("KRW"))
#                 init = upbit.get_balance("KRW")
#                 minutes = int(datetime.datetime.now().strftime('%M'))
#
#                 ask_1 = get_orderbook(f"KRW-{Symbol['key2']}")[0]["orderbook_units"][0]["ask_price"]
#                 bid_1 = get_orderbook(f"{Symbol['key1']}-{Symbol['key2']}")[0]["orderbook_units"][0]["bid_price"]
#                 bid_2 = get_orderbook(f"KRW-{Symbol['key1']}")[0]["orderbook_units"][0]["bid_price"]
#
#                 # when market order
#                 cash_out = ask_1 * (1 + 0.05 / 100)
#                 cash_in = bid_1 * (1 - 0.25 / 100) * bid_2 * (1 - 0.05 / 100)
#
#                 try:
#                     diff = (cash_in - cash_out) / cash_in * 100
#                 except TypeError:
#                     diff = 0
#                 # print(f"profit: {diff: .3f}")
#
#                 if diff > 0.1:
#                     upbit.buy_market_order(f"KRW-{Symbol['key2']}", format((upbit.get_balance("KRW")) * 0.9995, ".8f"))
#
#                     while True:
#                         if upbit.get_balance(ticker=f"{Symbol['key2']}") is not None:
#                             if upbit.get_balance(
#                                     ticker=f"{Symbol['key2']}") > 0.00000001:  # .8f 로 인해 반올림 오류로 남은 자산이 있을 수 있음.
#                                 upbit.sell_market_order(f"{Symbol['key1']}-{Symbol['key2']}",
#                                                         format(upbit.get_balance(f"{Symbol['key2']}"), ".8f"))
#
#                                 while True:
#                                     if upbit.get_balance(ticker=f"{Symbol['key1']}") is not None:
#                                         if upbit.get_balance(
#                                                 ticker=f"{Symbol['key1']}") > 0.0001:  # BTC 기준 최소 금액 (5000KRW).
#                                             upbit.sell_market_order(f"KRW-{Symbol['key1']}",
#                                                                     format(upbit.get_balance(f"{Symbol['key1']}"),
#                                                                            ".8f"))
#
#                                             if minutes == int(datetime.datetime.now().strftime('%M')):
#                                                 req_iterate += 1
#
#                                                 if req_iterate >= 66:
#                                                     req_iterate = 0
#                                                     sleep(60 - int(datetime.datetime.now().strftime('%S')))
#                                                 else:
#                                                     pass
#
#                                             else:
#                                                 req_iterate = 0
#
#                                             while True:
#                                                 if upbit.get_balance(ticker="KRW") > 5000:
#                                                     if init > upbit.get_balance(ticker="KRW"):
#                                                         print(
#                                                             "Algorithm Time Rate Error : Loss of Balances occur. Program EXIT")
#                                                         print(f"profit: {diff: .3f}")
#                                                         exit()
#                                                     else:
#                                                         print(upbit.get_balance(ticker="KRW"))
#                                                         pp = (upbit.get_balance("KRW") / init) * 100
#                                                         print(f"Profit : {pp: .3f}")
#                                                         break
#
#                                                 else:
#                                                     pass
#
#                                             break
#
#                                         else:
#                                             pass
#                                     else:
#                                         pass
#                                 break
#
#                             else:
#                                 pass
#                         else:
#                             pass
#                 else:
#                     print(f"profit: {diff: .3f}")
#                     pass
#
#         elif Option == 2:
#             while True:
#                 sleep(0.1)
#                 # print(upbit.get_balance("KRW"))
#                 init = upbit.get_balance("KRW")
#                 minutes = int(datetime.datetime.now().strftime('%M'))
#                 # try:
#
#                 ask_1 = get_orderbook(f"KRW-{Symbol['key2']}")[0]["orderbook_units"][0]["ask_price"]
#                 bid_1 = get_orderbook(f"{Symbol['key1']}-{Symbol['key2']}")[0]["orderbook_units"][0]["bid_price"]
#                 bid_2 = get_orderbook(f"KRW-{Symbol['key1']}")[0]["orderbook_units"][0]["bid_price"]
#
#                 # when limit order
#                 cash_out = ask_1 * (1 + 0.139 / 100)
#                 cash_in = bid_1 * 0.9975 * bid_2 * (1 - 0.139 / 100)
#
#                 try:
#                     diff = (cash_in - cash_out) / cash_in * 100
#                 except TypeError:
#                     diff = 0
#                 # print(f"profit: {diff: .3f}")
#
#                 if diff > 0:
#                     upbit.buy_limit_order(f"KRW-{Symbol['key2']}", ask_1,
#                                           format((upbit.get_balance("KRW") / ask_1) * 0.9995, ".8f"))
#                     while True:
#                         if upbit.get_balance(ticker=f"{Symbol['key2']}") is not None:
#                             if upbit.get_balance(
#                                     ticker=f"{Symbol['key2']}") > 0.00000001:  # .8f 로 인해 반올림 오류로 남은 자산이 있을 수 있음.
#                                 upbit.sell_limit_order(f"{Symbol['key1']}-{Symbol['key2']}", bid_1,
#                                                        format(upbit.get_balance(f"{Symbol['key2']}"), ".8f"))
#
#                                 while True:
#                                     if upbit.get_balance(ticker=f"{Symbol['key1']}") is not None:
#                                         if upbit.get_balance(
#                                                 ticker=f"{Symbol['key1']}") > 0.0001:  # BTC 기준 최소 금액 (5000KRW).
#                                             upbit.sell_limit_order(f"KRW-{Symbol['key1']}", bid_2,
#                                                                    format(upbit.get_balance(f"{Symbol['key1']}"),
#                                                                           ".8f"))
#
#                                             if minutes == int(datetime.datetime.now().strftime('%M')):
#                                                 req_iterate += 1
#
#                                                 if req_iterate >= 66:
#                                                     req_iterate = 0
#                                                     sleep(60 - int(datetime.datetime.now().strftime('%S')))
#                                                 else:
#                                                     pass
#
#                                             else:
#                                                 req_iterate = 0
#
#                                             while True:
#                                                 if upbit.get_balance(ticker="KRW") > 5000:
#                                                     if init > upbit.get_balance(ticker="KRW"):
#                                                         print(
#                                                             "Algorithm Time Rate Error : Loss of Balances occur. Program EXIT")
#                                                         exit()
#                                                     else:
#                                                         print(upbit.get_balance(ticker="KRW"))
#                                                         pp = (upbit.get_balance("KRW") / init) * 100
#                                                         print(f"Profit : {pp: .3f}")
#                                                         break
#
#                                                 else:
#                                                     pass
#
#                                             break
#
#                                         else:
#                                             pass
#                                     else:
#                                         pass
#                                 break
#
#                             else:
#                                 pass
#                         else:
#                             pass
#                 else:
#                     print(f"profit: {diff: .3f}")
#                     pass
#
#         else:
#             print("Option Undefined")


# 실제로 완전해 질려면, BTC 를 일정량 구입해 둔 다음,

from pyupbit import Upbit, get_current_price, get_orderbook
# https://github.com/sharebook-kr/pyupbit
import datetime
from sys import exit
from time import sleep

access = "0g02ZSPdlROwD5ydXpND9OTblVe7mVJoE2cbGzv5"
secret = 'YYSSzfolyXX0NNEWUSTOdDm8rJhd6YoOuYVyphah'
upbit = Upbit(access, secret)

# KRW/BTC - BTC/ETH - ETH/KRW 삼각차익거래 - reverse, 반대방향
Symbol = {"key1": "BTC", "key2": "XRP"}

# fee = {"KRW": 0.05, "BTC": 0.25, "USDT": 0.05}
# min_price = {"KRW": 500, "BTC": 0.0005, "USDT": 0.0005}
# 초당 8회, 분당 200회 : 주문
# 초당 30회, 분당 900회 : 주문외

Option = 1
# 1 : market 2 : Limit
req_iterate = 0

#         diff = get_current_price(f"KRW-{Symbol['key1']}") * (1 + 0.05 / 100) - \
#             ((1 / (1 + 0.25 / 100)) / get_current_price(f"{Symbol['key1']}-{Symbol['key2']}")) * \
#             get_current_price(f"KRW-{Symbol['key2']}") * (1 - 0.05 / 100)
#
#         reverse_diff = get_current_price(f"KRW-{Symbol['key2']}") * (1 + 0.05 / 100) -  \
#             get_current_price(f"{Symbol['key1']}-{Symbol['key2']}") * (1 - 0.25 / 100) * \
#             get_current_price(f"KRW-{Symbol['key1']}") * (1 - 0.05 / 100)

# general ask bid diff = ~ 2 %

# 호가로 거래 해야함

# 매수 매도 매도 triangle.

# 매수 주문 시 정산금액 = 체결금액(주문수량 x 주문가격) + 거래수수료
# 예시) 1BTC를 10,000,000원에 매수(거래수수료 0.139%) 시 내 계정에 1BTC 반영, 10,013,900원 차감
# 매수시, 원하는 만큼 정확한 양이 매수됨. 거래시 수수료 발생 .

# 매도 주문 시 정산금액 = 체결금액(주문수량 x 주문가격) – 거래수수료
# 예시) 1BTC를 10,000,000원에 매도(거래수수료 0.139%) 시 내 계정에 9,986,100원 반영, 1 BTC 차감
# 매도시, 원하는 만큼 정확한 양이 매도됨. 거래시 수수료 발생 .

# Market order
# buy at the asking price or sell at the bid price.

# bid 는 주식에 매수자가 주식에 기꺼이 지불하려고 하는 최대 금액 : 내가 팔때의 가격
# ask 는 주식 소유자가 판매하고자 하는 최소 금액 : 내가 살때의 가격
# ask 는 bid 보다 약간 높음.
# The price : 마지막 매매가 /  ask or buy 둘 다 가능

if Option == 1:
    while True:
        sleep(0.1)
        # print(upbit.get_balance("KRW"))
        init = upbit.get_balance("KRW")
        minutes = int(datetime.datetime.now().strftime('%M'))

        ask_1 = get_orderbook(f"KRW-{Symbol['key2']}")[0]["orderbook_units"][1]["ask_price"]
        bid_1 = get_orderbook(f"{Symbol['key1']}-{Symbol['key2']}")[0]["orderbook_units"][1]["bid_price"]
        bid_2 = get_orderbook(f"KRW-{Symbol['key1']}")[0]["orderbook_units"][1]["bid_price"]

        # when market order
        cash_out = ask_1 * (1 + 0.05 / 100)
        cash_in = bid_1 * (1 - 0.25/100) * bid_2 * (1 - 0.05 / 100)

        try:
            diff = (cash_in - cash_out) / cash_in * 100
        except TypeError:
            diff = 0
        # print(f"profit: {diff: .3f}")

        if diff > 0.5:
            upbit.buy_market_order(f"KRW-{Symbol['key2']}", format((upbit.get_balance("KRW")) * 0.9995, ".8f"))

            while True:
                try:
                    if upbit.get_balance(ticker=f"{Symbol['key2']}") > 0.00000001:  # .8f 로 인해 반올림 오류로 남은 자산이 있을 수 있음.
                        upbit.sell_market_order(f"{Symbol['key1']}-{Symbol['key2']}",
                                                format(upbit.get_balance(f"{Symbol['key2']}"), ".8f"))

                        while True:
                            try:
                                if upbit.get_balance(ticker=f"{Symbol['key1']}") > 0.0001:  # BTC 기준 최소 금액 (5000KRW).
                                    upbit.sell_market_order(f"KRW-{Symbol['key1']}",
                                                            format(upbit.get_balance(f"{Symbol['key1']}"), ".8f"))

                                    if minutes == int(datetime.datetime.now().strftime('%M')):
                                        req_iterate += 1

                                        if req_iterate >= 66:
                                            req_iterate = 0
                                            sleep(60 - int(datetime.datetime.now().strftime('%S')))
                                        else:
                                            pass

                                    else:
                                        req_iterate = 0

                                    while True:
                                        if upbit.get_balance(ticker="KRW") > 5000:
                                            if init > upbit.get_balance(ticker="KRW"):
                                                print("Algorithm Time Rate Error : Loss of Balances occur. Program EXIT")
                                                print(f"profit: {diff: .3f}")
                                                exit()
                                            else:
                                                print(upbit.get_balance(ticker="KRW"))
                                                pp = (upbit.get_balance("KRW") / init) * 100
                                                print(f"Profit : {pp: .3f}")
                                                break

                                        else:
                                            pass

                                    break

                                else:
                                    pass
                            except TypeError:
                                pass
                        break

                    else:
                        pass
                except TypeError:
                    pass
        else:
            print(f"profit: {diff: .3f}")
            pass

elif Option == 2:
    while True:
        sleep(0.1)
        # print(upbit.get_balance("KRW"))
        init = upbit.get_balance("KRW")
        minutes = int(datetime.datetime.now().strftime('%M'))
        # try:

        ask_1 = get_orderbook(f"KRW-{Symbol['key2']}")[0]["orderbook_units"][0]["ask_price"]
        bid_1 = get_orderbook(f"{Symbol['key1']}-{Symbol['key2']}")[0]["orderbook_units"][0]["bid_price"]
        bid_2 = get_orderbook(f"KRW-{Symbol['key1']}")[0]["orderbook_units"][0]["bid_price"]

        # when limit order
        cash_out = ask_1 * (1 + 0.139 / 100)
        cash_in = bid_1 * 0.9975 * bid_2 * (1 - 0.139 / 100)

        try:
            diff = (cash_in - cash_out) / cash_in * 100
        except TypeError:
            diff = 0
        # print(f"profit: {diff: .3f}")

        if diff > 0:
            upbit.buy_limit_order(f"KRW-{Symbol['key2']}", ask_1,
                                  format((upbit.get_balance("KRW") / ask_1) * 0.9995, ".8f"))
            while True:
                try:
                    if upbit.get_balance(ticker=f"{Symbol['key2']}") > 0.00000001:  # .8f 로 인해 반올림 오류로 남은 자산이 있을 수 있음.
                        upbit.sell_limit_order(f"{Symbol['key1']}-{Symbol['key2']}", bid_1,
                                               format(upbit.get_balance(f"{Symbol['key2']}"), ".8f"))

                        while True:
                            try:
                                if upbit.get_balance(ticker=f"{Symbol['key1']}") > 0.0001:  # BTC 기준 최소 금액 (5000KRW).
                                    upbit.sell_limit_order(f"KRW-{Symbol['key1']}", bid_2,
                                                           format(upbit.get_balance(f"{Symbol['key1']}"), ".8f"))

                                    if minutes == int(datetime.datetime.now().strftime('%M')):
                                        req_iterate += 1

                                        if req_iterate >= 66:
                                            req_iterate = 0
                                            sleep(60 - int(datetime.datetime.now().strftime('%S')))
                                        else:
                                            pass

                                    else:
                                        req_iterate = 0

                                    while True:
                                        if upbit.get_balance(ticker="KRW") > 5000:
                                            if init > upbit.get_balance(ticker="KRW"):
                                                print("Algorithm Time Rate Error : Loss of Balances occur. Program EXIT")
                                                exit()
                                            else:
                                                print(upbit.get_balance(ticker="KRW"))
                                                pp = (upbit.get_balance("KRW") / init) * 100
                                                print(f"Profit : {pp: .3f}")
                                                break

                                        else:
                                            pass

                                    break

                                else:
                                    pass
                            except TypeError:
                                pass
                        break

                    else:
                        pass
                except TypeError:
                    pass
        else:
            print(f"profit: {diff: .3f}")
            pass

else:
    print("Option Undefined")
