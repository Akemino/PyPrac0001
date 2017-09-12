"""
当ファイルの説明文を記述
"""
# import time
import configparser
import gl
from DummyWorldClass import DummyWorldClass
from FounderGcClass import FounderGcClass

# a = FounderBaseClass()
# a.name = '1234312'
# a.print_name()
def main():
    """メイン処理"""

    # gl.setting_main

    inifile = configparser.SafeConfigParser()
    inifile.read('./setting.ini', encoding='utf-8')
    for key in inifile.options('main'):
        gl.setting_main[key] = inifile.get('main', key)

    # CSVから価格推移を読み込む
    world = DummyWorldClass()
    world.load_company_price_list(gl.setting_main['csv_path'])

    # 投資する人のリストを作成
    gc1 = FounderGcClass()
    gc1.name = "7-25型"
    


    print("DEBUG")
    print(gl.company_list["1327-T"].price_daily_list["20170822"].start_price)


    # mar_sample = FounderSampleClass()
    # mar_sample.name = 'sampleSubClass'
    # mar_sample.print_name()

main()
