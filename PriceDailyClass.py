# --- coding: utf-8 ---
"""
価格変動一日分の構造体
"""
import datetime


class PriceDailyClass:
    """価格変動一日分の構造体"""

    ymd = datetime.datetime(2001, 1, 1)
    """いつの情報か"""

    start_price = 0
    """始値"""

    end_price = 0
    """終値"""

    max_price = 0
    """最高値"""

    min_price = 0
    """最安値"""

    def __init__(self):
        """"""
        print("")

    def set_price(self, st_price, en_price, ma_price, mi_price):
        """
        価格セット用メソッド
        @param st_price 始値
        @param en_price 終値
        @param ma_price 最高値
        @param mi_price 最安値
        """
        self.start_price = st_price
        self.end_price = en_price
        self.max_price = ma_price
        self.min_price = mi_price


    def is_down(self):
        """その日に下がっていた場合はTrueを返す"""
        ret = False
        if self.start_price > self.end_price:
            ret = True
        return ret
