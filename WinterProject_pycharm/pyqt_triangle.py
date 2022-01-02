import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, \
    QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QCheckBox, QPushButton, \
    QTextBrowser, QComboBox, QLabel, QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QCoreApplication
from pyupbit import Upbit, get_orderbook
# https://github.com/sharebook-kr/pyupbit
import datetime
from sys import exit
from time import sleep


class TAT:
    def __init__(self, view):

        access = "0g02ZSPdlROwD5ydXpND9OTblVe7mVJoE2cbGzv5"
        secret = 'YYSSzfolyXX0NNEWUSTOdDm8rJhd6YoOuYVyphah'
        self.upbit = Upbit(access, secret)
        self._view = view
        self.connect_signal()
        self.text_1 = self._view.text_gr2
        self.text_2 = self._view.text_gr4
        # self.connect_signal()
        # print("done")
        self._view.text_gr4.append(f"{self._view.mode}")

        # _view = view 인 객체에 의해 text_gr2의 전달까진 성공.이제 시그널을 다시 연결해주어야함.
        #TODO 시그널 연결결

    def trade(self, mode, text_1, text_2, val1="BTC", val2='XRP'):

        upbit = self.upbit
        Option = mode
        Symbol = {"key1": val1, "key2": val2}

        text_gr2 = text_1
        text_gr4 = text_2
        req_iterate = 0

        text_gr2.append(f"Mode :{Option}, Ticker: {val1}-{val2}")

        if Option == 0:
            while True:
                sleep(0.1)
                # print(upbit.get_balance("KRW"))
                init = upbit.get_balance("KRW")
                minutes = int(datetime.datetime.now().strftime('%M'))

                ask_1 = get_orderbook(f"KRW-{Symbol['key2']}")[0]["orderbook_units"][0]["ask_price"]
                bid_1 = get_orderbook(f"{Symbol['key1']}-{Symbol['key2']}")[0]["orderbook_units"][0]["bid_price"]
                bid_2 = get_orderbook(f"KRW-{Symbol['key1']}")[0]["orderbook_units"][0]["bid_price"]

                # when market order
                cash_out = ask_1 * (1 + 0.05 / 100)
                cash_in = bid_1 * (1 - 0.25 / 100) * bid_2 * (1 - 0.05 / 100)

                try:
                    diff = (cash_in - cash_out) / cash_in * 100
                except TypeError:
                    diff = 0
                # print(f"profit: {diff: .3f}")

                if diff > 0.1:
                    upbit.buy_market_order(f"KRW-{Symbol['key2']}", format((upbit.get_balance("KRW")) * 0.9995, ".8f"))

                    while True:
                        try:
                            if upbit.get_balance(
                                    ticker=f"{Symbol['key2']}") > 0.00000001:  # .8f 로 인해 반올림 오류로 남은 자산이 있을 수 있음.
                                upbit.sell_market_order(f"{Symbol['key1']}-{Symbol['key2']}",
                                                        format(upbit.get_balance(f"{Symbol['key2']}"), ".8f"))

                                while True:
                                    try:
                                        if upbit.get_balance(
                                                ticker=f"{Symbol['key1']}") > 0.0001:  # BTC 기준 최소 금액 (5000KRW).
                                            upbit.sell_market_order(f"KRW-{Symbol['key1']}",
                                                                    format(upbit.get_balance(f"{Symbol['key1']}"),
                                                                           ".8f"))

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
                                                        print_gr4 = "Algorithm Time Rate Error : " \
                                                                    "Loss of Balances occur. Program EXIT"
                                                        text_gr4.append(print_gr4)
                                                        print_gr4 = f"profit: {diff: .3f}"
                                                        text_gr4.append(print_gr4)

                                                        return None
                                                        # TODO exit() - input으로 계속할지 받기
                                                    else:
                                                        print_gr4 = upbit.get_balance(ticker="KRW")
                                                        text_gr4.append(print_gr4)
                                                        pp = (upbit.get_balance("KRW") / init) * 100
                                                        print_gr4 = f"Profit : {pp: .3f}"
                                                        text_gr4.append(print_gr4)

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
                    print_gr2 = f"profit: {diff: .3f}"
                    text_gr2.append(print_gr2)

                    pass

        elif Option == 1:
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
                            if upbit.get_balance(
                                    ticker=f"{Symbol['key2']}") > 0.00000001:  # .8f 로 인해 반올림 오류로 남은 자산이 있을 수 있음.
                                upbit.sell_limit_order(f"{Symbol['key1']}-{Symbol['key2']}", bid_1,
                                                       format(upbit.get_balance(f"{Symbol['key2']}"), ".8f"))

                                while True:
                                    try:
                                        if upbit.get_balance(
                                                ticker=f"{Symbol['key1']}") > 0.0001:  # BTC 기준 최소 금액 (5000KRW).
                                            upbit.sell_limit_order(f"KRW-{Symbol['key1']}", bid_2,
                                                                   format(upbit.get_balance(f"{Symbol['key1']}"),
                                                                          ".8f"))

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
                                                        print_gr4 = "Algorithm Time Rate Error : " \
                                                                    "Loss of Balances occur. Program EXIT"
                                                        text_gr4.append(print_gr4)
                                                        print_gr4 = f"profit: {diff: .3f}"
                                                        text_gr4.append(print_gr4)

                                                        return None

                                                        # TODO exit() - input으로 계속할지 받기
                                                    else:
                                                        print_gr4 = upbit.get_balance(ticker="KRW")
                                                        text_gr4.append(f"{print_gr4}")
                                                        pp = (upbit.get_balance("KRW") / init) * 100
                                                        print_gr4 = f"Profit : {pp: .3f}"
                                                        text_gr4.append(f"{print_gr4}")

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
                    print_gr2 = f"profit: {diff: .3f}"
                    text_gr2.append(print_gr2)

                    pass

        else:
            print_gr2 = "Stop"
            text_gr2.append(print_gr2)

    def trade_start(self, state):
        self._view.btn1.setStyleSheet("background-color: %s" % ({True: "red", False: "green"}[state]))
        self._view.btn1.setText({True: "Stop", False: "Start"}[state])

        if state and self._view.ticker is not None:
            self._view.text_gr4.append(f"{state} : with BTC-{self._view.ticker}")
            self.trade(self._view.mode, text_1=self.text_1, text_2=self.text_2, val1="BTC", val2=self._view.ticker)
        elif state and self._view.ticker is None or self._view.mode is None:
            print_gr4 = "Error"
            self._view.text_gr4.append(print_gr4)
        else:
            print_gr4 = "Unknown Error"
            self._view.text_gr4.append(print_gr4)

    def connect_signal(self):
        self._view.btn1.toggled.connect(self.trade_start)


class App(QMainWindow):

    def __init__(self):
        super().__init__()

        self.lbl1 = QLabel(f'Mode : None ', self)
        self.lbl2 = QLabel(f'ticker : None ', self)

        self.text_gr2 = QTextBrowser()
        self.text_gr4 = QTextBrowser()

        self.setWindowTitle('Triangular arbitrage transaction')
        self.setGeometry(300, 300, 480, 320)

        self.generalLayout = QGridLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        self.ticker = None
        self.mode = 0

        self.Group1()
        self.Group2()
        self.Group3()
        self.Group4()

    def Group1(self):
        groupbox = QGroupBox('Config')

        cb1 = QComboBox(self)
        cb1.addItem('Mode 1 : Market Order')
        cb1.addItem('Mode 2 : Limit Order')

        cb1.activated[str].connect(self.activated_mode)

        cb2 = QComboBox(self)
        cb2.addItem('ETH')
        cb2.addItem('XRP')

        cb2.activated[str].connect(self.activated_ticker)

        vbox = QVBoxLayout()
        vbox.addWidget(cb1)
        vbox.addWidget(self.lbl1)
        vbox.addWidget(cb2)
        vbox.addWidget(self.lbl2)
        groupbox.setLayout(vbox)

        self.generalLayout.addWidget(groupbox, 0, 0)


    def activated_mode(self, text):
        self.lbl1.setText(f'{text}')
        if text == 'Mode 1 : Market Order':
            self.mode = 0
        else:
            self.mode = 1

        self.lbl1.adjustSize()

    def activated_ticker(self, text):
        self.lbl2.setText(f'ticker : BTC-{text}')
        self.ticker = text
        self.lbl2.adjustSize()

    def Group2(self):
        groupbox = QGroupBox('Diff')

        # self.text_gr2.append("sample")

        vbox = QVBoxLayout()
        vbox.addWidget(self.text_gr2)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        self.generalLayout.addWidget(groupbox, 0 ,1)

    def Group3(self):
        groupbox = QGroupBox()

        self.btn1 = QPushButton('Start')
        # self.btn1.setText("Start")
        self.btn1.setStyleSheet("background-color: green")

        self.btn1.setCheckable(True)
        # self.btn1.toggled.connect(self.trade_start)

        btn2 = QPushButton('Quit', self)
        btn2.clicked.connect(QCoreApplication.instance().quit)

        vbox = QVBoxLayout()
        vbox.addWidget(self.btn1)
        vbox.addStretch(1)
        vbox.addWidget(btn2)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        self.generalLayout.addWidget(groupbox, 1, 0)

    def Group4(self):
        groupbox = QGroupBox('Logs')
        vbox = QVBoxLayout()
        vbox.addWidget(self.text_gr4)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        self.generalLayout.addWidget(groupbox, 1, 1)

    # def trade_start(self, state):
    #     self.btn1.setStyleSheet("background-color: %s" % ({True: "red", False: "green"}[state]))
    #     self.btn1.setText({True: "Stop", False: "Start"}[state])
    #     t = TAT(self.show())
    #     text_1 = t._view.text_gr2
    #     text_2 = t._view.text_gr4
    #     mode = self.mode
    #     ticker = self.ticker
    #     if state and self.ticker is not None:
    #         self.text_gr4.append(f"{state} : with BTC-{self.ticker}")
    #         self.t.trade(mode, text_1, text_2, val1="BTC", val2=ticker)
    #     elif state and self.ticker is None or self.mode is None:
    #         print_gr4 = "Error"
    #         self.text_gr4.append(print_gr4)
    #     else:
    #         print_gr4 = "Unknown Error"
    #         self.text_gr4.append(print_gr4)

    # def trade(self, mode, text_1: QTextBrowser(), text_2: QTextBrowser, , val2='XRP'):


def main():
    app = QApplication(sys.argv)
    view = App()
    view.show()
    TAT(view=view)
    # 함수 부분 연결
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
