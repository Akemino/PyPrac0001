"""
当ファイルの説明文を記述
"""
# import time
import ConfigParser
from DummyWorldClass import DummyWorldClass


# a = FounderBaseClass()
# a.name = '1234312'
# a.print_name()
def main():
    """メイン処理"""

    setting_main = []
    inifile = ConfigParser.SafeConfigParser()
    inifile.read('./setting.ini')
    for key in inifile.options('main'):
        setting_main[key] = inifile.get('main', key)

    world = DummyWorldClass()
    #world.load_company_price_list(setting_main['csvPath'])

    # mar_sample = FounderSampleClass()
    # mar_sample.name = 'sampleSubClass'
    # mar_sample.print_name()

    




main()
