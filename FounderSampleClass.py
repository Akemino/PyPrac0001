# --- coding: utf-8 ---
"""
当ファイルの説明文を記述
"""

from FounderBaseClass import FounderBaseClass

class FounderSampleClass(FounderBaseClass):
    """Classの継承サンプル"""

    def __init__(self):
        super().__init__()

    def forecast_by_date(self, ymd_from):
        """指定した日付毎にスコア一覧を作成します。"""

        
        
