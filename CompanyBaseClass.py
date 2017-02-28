# --- coding: utf-8 ---
"""
継承の練習。親クラスです。
"""

class CompanyBaseClass:
    """Companyの基底クラス"""

    name = ''
    """設定必須"""


    def __init__(self):
        """コンストラクタ。特に何もしません"""
        print("CompanyBaseClass init")

    def print_name(self):
        """名称を表示します。テスト用の関数。"""
        print(self.name)
