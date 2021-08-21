"""
12_3.py：重新設計ch12_2.py 設定初始化的方法同時存在第一筆的錢100元入銀行，然後列出存款金額。
"""


class Banks():
    '''定義銀行類別'''
    bankname = 'Taipei Bank'  # 定義屬性

    def __init__(self, uname, money):  # 初始化發放 init是initalization的縮寫
        self.name = uname  # 設定存款者名稱
        self.balance = money  # 設定所存的錢

    def get_blance(self):  # 獲得存款餘額
        return self.balance


hungbank = Banks('huang', 100)
print(hungbank.name.title(), " 存款餘額是 ", hungbank.get_blance())
