# --- coding: utf-8 ---

class FounderBaseClass:
    """Founderの基底クラス"""

    name = ''
    """設定必須"""


    def __init__(self):
        """コンストラクタ。特に何もしません"""
        print("FounderBaseClass init")

    def printName(self):
        """名称を表示します。テスト用の関数。"""
        print(self.name)

        
        
