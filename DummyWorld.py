# --- coding: utf-8 ---
"""
仮想化した世界クラスのファイル
"""

from PriceDailyClass import PriceDailyClass

class FounderBaseClass:
    """仮想化した世界クラス"""

    price_daily_list = []
    """"""

    def __init__(self):
        """"""
        self.price_daily_list = []

    def load_price_list(self):
        """CSVから価格リストを読み込む"""
        self.price_daily_list = []

        temp_price = PriceDailyClass()
        temp_price.set_price(30, 90, 20, 100)

        print(self.price_daily_list.count)
