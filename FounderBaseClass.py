# --- coding: utf-8 ---
"""
継承の練習。親クラスです。
"""

class FounderBaseClass:
    """Founderの基底クラス"""

    name = ''
    """設定必須"""


    def __init__(self):
        """コンストラクタ。特に何もしません"""
        print("FounderBaseClass init")

    def print_name(self):
        """名称を表示します。テスト用の関数。"""
        print(self.name)

    def forecast_by_date(self, ymd):
        """指定した日付毎にスコア一覧を作成します。"""
