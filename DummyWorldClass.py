# --- coding: utf-8 ---
"""
仮想化した世界クラスのファイル
"""
import csv 
import os
import re

import gl # 自前のグローバルなアレ
from CompanyClass import CompanyClass
from PriceDailyClass import PriceDailyClass

class DummyWorldClass:
    """仮想化した世界クラス"""

    def __init__(self):
        """"""

    def load_company_price_list(self, csv_dir_path):
        """
        会社と価格の一覧を読み込みます。
        @param csv_dir_path CSVのあるフォルダのパス。末尾にディレクトリ記号。
        """

        COL_CODE = 0
        COL_NAME = 2
        COL_START_PRICE = 3
        COL_END_PRICE = 4
        COL_MAX_PRICE = 5
        COL_MIN_PRICE = 6

        
        files = os.listdir(csv_dir_path)
        files_file = [f for f in files if os.path.isfile(os.path.join(csv_dir_path, f))]

        ymd = "" # CSVファイルの日付をYYYYMMDD形式

        # 1日のCSV情報を元に会社情報等を作成
        for csv_path in files_file:

            pattern = "([0-9]{4}\-[0-9]{2}\-[0-9]{2})"
            repatter = re.compile(pattern)
            matched = repatter.search(csv_path)
            ymd = matched.group(1).replace("-","")
            # print(ymd)

            with open(os.path.join(csv_dir_path, csv_path), 'r',encoding='shift_jis') as f:
                reader = csv.reader(f)
                header = next(reader)  # ヘッダーを読み飛ばしたい時

                for row in reader:
                    # CSV1行をもとに、未搭乗の会社であればCompanyClassを作成する。
                    # また、PriceDailyClassも作成する。
                    if row[COL_CODE] in gl.company_list:
                        pass
                    else:
                        # 未登場の会社
                        comp_new = CompanyClass()
                        comp_new.code = row[COL_CODE]
                        comp_new.name = row[COL_NAME]
                        comp_new.price_daily_list = {}
                        gl.company_list[row[COL_CODE]] = comp_new

                    # 価格を登録
                    price = PriceDailyClass()
                    price.max_price = row[COL_MAX_PRICE]
                    price.min_price = row[COL_MIN_PRICE]
                    price.end_price = row[COL_END_PRICE]
                    price.start_price = row[COL_START_PRICE]
                    price.ymd = ymd
                    gl.company_list[row[COL_CODE]].price_daily_list[ymd] = price

                #gl.company_list に価格と会社を登録しおえた
