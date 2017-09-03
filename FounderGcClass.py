# --- coding: utf-8 ---
"""
ゴールデンクロス法で予想する人たちのクラス
"""

import gl
import CompanyClass
from FounderBaseClass import FounderBaseClass


class FounderGcClass(FounderBaseClass):
    """Classの継承サンプル"""

    def __init__(self):
        super().__init__()

    def forecast_by_date(self, ymd_from):
        """指定した日付毎にスコア一覧を作成します。"""

        # 指定した日付より前の日付を見て、会社ごとのスコアを算出
        for comp in gl.company_list:
            

            
        