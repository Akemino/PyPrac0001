# --- coding: utf-8 ---
"""
仮想化した世界クラスのファイル
"""
import csv 
import os
from CompanyBaseClass import CompanyBaseClass
from PriceDailyClass import PriceDailyClass

class DummyWorldClass:
    """仮想化した世界クラス"""
    company_list = []

    def __init__(self):
        """"""

    def load_company_price_list(self, csv_dir_path):
        """
        会社と価格の一覧を読み込みます。
        @param csv_dir_path CSVのあるフォルダのパス。末尾にディレクトリ記号。
        """

        files = os.listdir(csv_dir_path)
        files_file = [f for f in files if os.path.isfile(os.path.join(csv_dir_path, f))]

        companyes = {}
        # 1日のCSV情報を元に会社情報等を作成
        for csv_path in files_file:
            with open(os.path.join(csv_dir_path, csv_path), 'r',encoding='shift_jis') as f:
                reader = csv.reader(f)
                header = next(reader)  # ヘッダーを読み飛ばしたい時

                for row in reader:
                    print(row)







        #while i < 100:
        #    i = i + 1
        #    new_comp = CompanyBaseClass()
        #    new_comp.name = "COMPANY_" + '{0:04d}'.format(i)
        #    new_price = PriceDailyClass()
        #    new_price.ymd = ""
        #    new_price.set_price(40, 90, 120, 24)
        #    new_comp.price_daily_list.append(new_price)
