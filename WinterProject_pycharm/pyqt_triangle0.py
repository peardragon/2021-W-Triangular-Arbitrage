import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, \
    QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QCheckBox, QPushButton, \
    QTextBrowser, QComboBox, QLabel, QMainWindow, QLineEdit
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QCoreApplication
from pyupbit import Upbit, get_orderbook
# https://github.com/sharebook-kr/pyupbit
import datetime
from sys import exit
from time import sleep
from PyQt5.QtCore import QThread, pyqtSignal, QObject
from PyQt5 import QtGui


# 백드라운드에서 함수를 넣어 실행시키는 시그널 - 슬롯
# https://m.blog.naver.com/townpharm/220959370280


class TAT(QObject):
    # Pyqt 시그널 객체 생성
    finished = pyqtSignal()

    def __init__(self, mode, text_gr2, text_gr4, val1, val2, parent=None):

        QObject.__init__(self, parent=parent)
        self.condition_run = True

        access = "0g02ZSPdlROwD5ydXpND9OTblVe7mVJoE2cbGzv5"
        secret = 'YYSSzfolyXX0NNEWUSTOdDm8rJhd6YoOuYVyphah'
        self.upbit = Upbit(access, secret)
        self.mode = mode
        self.text_gr2 = text_gr2
        self.text_gr4 = text_gr4
        self.val1 = val1
        self.val2 = val2

    def trade(self):

        text_gr2 = self.text_gr2
        text_gr4 = self.text_gr4
        Symbol = {"key1": self.val1, "key2": self.val2}

        # 거래소에 있으면, list 변수
        if type(get_orderbook(f"KRW-{Symbol['key2']}")) == list:

            upbit = self.upbit
            Option = int(self.mode)
            text_gr4.append(f"Mode: {Option + 1} : BTC-{self.val2}")

            req_iterate = 0

            diff_limit = 0.5

            if Option == 0:
                while self.condition_run:
                    QThread.msleep(100)

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

                    if diff > diff_limit:
                        upbit.buy_market_order(f"KRW-{Symbol['key2']}",
                                               format((upbit.get_balance("KRW")) * 0.9995, ".8f"))

                        while True:
                            try:
                                if upbit.get_balance(
                                        ticker=f"{Symbol['key2']}") > 0.00000001:  # .8f 로 인해 반올림 오류로 남은 자산이 있을 수 있음.
                                    upbit.sell_market_opyirder(f"{Symbol['key1']}-{Symbol['key2']}",
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
                                                            text_gr4.moveCursor(QtGui.QTextCursor.End)

                                                            break

                                                        else:
                                                            print_gr4 = upbit.get_balance(ticker="KRW")
                                                            text_gr4.append(print_gr4)
                                                            pp = (upbit.get_balance("KRW") / init) * 100
                                                            print_gr4 = f"Profit : {pp: .3f}"
                                                            text_gr4.append(print_gr4)
                                                            text_gr4.moveCursor(QtGui.QTextCursor.End)

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
                        text_gr2.moveCursor(QtGui.QTextCursor.End)

                        pass

            elif Option == 1:
                while self.condition_run:
                    QThread.msleep(100)

                    init = upbit.get_balance("KRW")
                    minutes = int(datetime.datetime.now().strftime('%M'))

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
                                                            text_gr4.moveCursor(QtGui.QTextCursor.End)

                                                            break

                                                        else:
                                                            print_gr4 = upbit.get_balance(ticker="KRW")
                                                            text_gr4.append(f"{print_gr4}")
                                                            pp = (upbit.get_balance("KRW") / init) * 100
                                                            print_gr4 = f"Profit : {pp: .3f}"
                                                            text_gr4.append(f"{print_gr4}")
                                                            text_gr4.moveCursor(QtGui.QTextCursor.End)

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
                        text_gr2.moveCursor(QtGui.QTextCursor.End)

                        pass

                # self.finished.emit()

            else:
                print_gr2 = "Stop"
                text_gr2.append(print_gr2)

        else:
            print_gr4 = "Ticker Type Error"
            text_gr4.append(print_gr4)


    # 버튼 클랙시 시그널 받아들이는 슬롯 생성
    @pyqtSlot()
    def stop(self):
        self.condition_run = False


# 백그라운드에서 돌아갈 함수 클래스


class App(QMainWindow):

    # stop_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.lbl1 = QLabel(f'Mode : None ', self)
        self.lbl2 = QLabel(f'ticker : None ', self)

        self.text_gr2 = QTextBrowser()
        self.text_gr4 = QTextBrowser()

        self.setWindowTitle('Triangular arbitrage transaction')
        self.setGeometry(300, 300, 480, 320)

        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        self.ticker = 0
        self.mode = None

        self.btn1 = QPushButton()
        self.btn1.setText("Start")

        self.btn2 = QPushButton()
        self.btn2.setText('Stop')
        self.btn2.setEnabled(False)

        self.initUI()

    def init_thread(self):

        # 따로 돌아갈 thread 생성
        self.thread = QThread()
        # 백그라운드에서 돌아갈 인스턴스 소환
        self.worker = TAT(self.mode, self.text_gr2, self.text_gr4, val1="BTC", val2=self.ticker)

        # self.stop_signal.connect(self.worker.stop)

        # worker를 만들어둔 thread에 삽입.
        self.worker.moveToThread(self.thread)

        # self.worker.finished.connect(self.thread.quit)  # connect the workers finished signal to stop thread
        # self.worker.finished.connect(self.worker.deleteLater)  # connect the workers finished signal to clean up worker
        # self.thread.finished.connect(self.thread.deleteLater)  # connect threads finished signal to clean up thread

        # self.thread.started.connect(self.worker.trade)
        # self.thread.finished.connect(self.worker.stop)

        # Start Thread
        self.thread.start()

        # Start Button action:
        self.btn1.clicked.connect(self.worker.trade)
        self.btn1.clicked.connect(self.btns_enable)

        # Stop Button action:
        self.btn2.clicked.connect(self.stop_thread)

    def btns_enable(self):
        self.btn2.setEnabled(True)
        self.cb1.setEnabled(False)
        self.cb2.setEnabled(False)

    def stop_thread(self):
        if self.thread.isRunning():
            self.thread.terminate()

            # 새롭게 thread 대기
            self.thread.wait()
            self.thread.start()

            self.btn2.setEnabled(False)

    def initUI(self):

        grid = QGridLayout()
        grid.addWidget(self.Group1, 0, 0)
        grid.addWidget(self.Group2(), 0, 1)
        grid.addWidget(self.Group3(), 1, 0)
        grid.addWidget(self.Group4(), 1, 1)

        self.generalLayout.addLayout(grid)

        # self.show()

    @property
    def Group1(self):
        groupbox = QGroupBox('Config')

        self.cb1 = QComboBox(self)
        self.cb1.addItem('Mode 1 : Market Order')
        self.cb1.addItem('Mode 2 : Limit Order')

        self.cb1.activated[str].connect(self.activated_mode)

        self.cb2 = QComboBox(self)
        self.cb2.addItem('ETH')
        self.cb2.addItem('XRP')

        self.cb2.activated[str].connect(self.activated_ticker)

        self.ticker_input = QLineEdit()

        self.cb_add = QPushButton('Add ticker')
        self.cb_add.clicked.connect(self.add_item)


        vbox = QVBoxLayout()
        vbox.addWidget(self.cb1)
        vbox.addWidget(self.lbl1)

        hbox = QHBoxLayout()
        hbox.addWidget(self.ticker_input)
        hbox.addWidget(self.cb_add)

        vbox.addLayout(hbox)
        vbox.addWidget(self.cb2)
        vbox.addWidget(self.lbl2)


        groupbox.setLayout(vbox)

        return groupbox

    def add_item(self):
        self.cb2.addItem(self.ticker_input.text().upper())


    def activated_mode(self, text):
        self.lbl1.setText(f'{text}')
        if text == 'Mode 1 : Market Order':
            self.mode = 0
        else:
            self.mode = 1

        self.lbl1.adjustSize()

        if self.mode is not None and self.ticker != 0:
            self.init_thread()

        # self.cb2.setEnabled(True)

    def activated_ticker(self, text):
        self.lbl2.setText(f'ticker : BTC-{text}')
        self.ticker = text
        self.lbl2.adjustSize()

        if self.mode is not None and self.ticker != 0:
            self.init_thread()

    def Group2(self):
        groupbox = QGroupBox('Diff')

        # self.text_gr2.append("sample")

        vbox = QVBoxLayout()
        vbox.addWidget(self.text_gr2)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox

    def Group3(self):
        groupbox = QGroupBox()

        # self.btn1.setStyleSheet("background-color: green")
        #
        # self.btn1.setCheckable(True)
        # self.btn1.toggled.connect(self.trade_start)

        btn3 = QPushButton('Quit', self)
        btn3.clicked.connect(QCoreApplication.instance().quit)

        # btn4 = QPushButton('restart', self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.btn1)
        vbox.addStretch(1)
        vbox.addWidget(self.btn2)
        vbox.addStretch(1)
        vbox.addWidget(btn3)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox

    def Group4(self):
        groupbox = QGroupBox('Logs')
        vbox = QVBoxLayout()
        vbox.addWidget(self.text_gr4)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox

    # def trade_start(self, state):
    #     self.btn1.setStyleSheet("background-color: %s" % ({True: "red", False: "green"}[state]))
    #     self.btn1.setText({True: "Stop", False: "Start"}[state])
    #
    #     mode = self.mode
    #     ticker = self.ticker
    #     text_1 = self.text_gr2
    #     text_2 = self.text_gr4
    #
    #     if state and self.ticker is not None:
    #         self.text_gr4.append(f"{state} : with BTC-{self.ticker}")
    #         t = TAT()
    #         t.trade(mode, text_1, text_2, val1="BTC", val2=ticker)
    #         # for i in range(10):
    #         #     text_1.append("test")
    #         # t.print_it(text_1)
    #     elif state and self.ticker is None or self.mode is None:
    #         print_gr4 = "Error"
    #         self.text_gr4.append(print_gr4)
    #     else:
    #         pass

    # def trade(self, mode, text_1: QTextBrowser(), text_2: QTextBrowser, , val2='XRP'):


def main():
    app = QApplication(sys.argv)
    view = App()
    view.show()
    # 함수 부분 연결
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
