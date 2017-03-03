# --- coding: utf-8 ---
"""
仮想化した世界クラスのファイル
"""
from CompanyBaseClass import CompanyBaseClass
from PriceDailyClass import PriceDailyClass
#import csv 

class DummyWorldClass:
    """仮想化した世界クラス"""
    company_list = []

    def __init__(self):
        """"""

    def load_company_price_list(self):
        """会社と価格の一覧を読み込みます。"""

        i = 1
        while i < 100:
            i = i + 1
            new_comp = CompanyBaseClass()
            new_comp.name = "COMPANY_" + '{0:04d}'.format(i)
            new_price = PriceDailyClass()
            new_price.ymd = ""
            new_price.set_price(40, 90, 120, 24)
            new_comp.price_daily_list.append(new_price)
