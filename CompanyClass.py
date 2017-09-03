# --- coding: utf-8 ---
"""
会社。
"""

class CompanyClass:
    """会社クラス。"""

    name = ''
    """名称。銘柄名。設定必須"""

    code = ''
    """コード。被らない。"""

    price_daily_list = {}
    """"""

    def __init__(self):
        """コンストラクタ。特に何もしません"""
        # print("CompanyClass init")

    def print_name(self):
        """名称を表示します。テスト用の関数。"""
        # print(self.name)

