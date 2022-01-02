# ip 112.149.195.170 기준
#https://www.findip.kr/

# PyJWT version 1.7.1 로 downgrade해야 decode 코드 인식.

import pyupbit

access = "0g02ZSPdlROwD5ydXpND9OTblVe7mVJoE2cbGzv5"          # 본인 값으로 변경
secret = "YYSSzfolyXX0NNEWUSTOdDm8rJhd6YoOuYVyphah"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

ticker_list = pyupbit.get_tickers()
ticker_dict = {string:None for string in ticker_list}

print(ticker_dict)
print(upbit.get_balances())

#TODO 전체 분당 총 거래소 내부 코인 시세 확인
# 코인 시세확인으로 부터 작전 세력 (폭등의심) 부분 확인 알고리즘 학습
# - 이건 이전 거래량과 달라진 거래량 같은것들로 부터 특정 시점 퍼센테이지 이상하는 종목 찾기로 해야할듯

print(len(pyupbit.get_tickers()))
#294
f"https://crix-api-tv.upbit.com/v1/crix/tradingview/history?symbol=BTCKRW&resolut" \
f"ion=1&from=1606713658&to=1606713770"


