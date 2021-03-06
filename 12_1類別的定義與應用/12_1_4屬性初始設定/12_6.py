"""
12_6.py:設定開戶(定義Banks類別物件)只要姓名，同時設定開戶金額書0元，讀者可留意第7和第8行的設定
"""


class Banks():
    """定義銀行類別"""

    def __init__(self, uname):  # 設定存款者名字
        self.name = uname  # 初始化存款金額
        self.balance = 0  # 設定開戶金額是0
        self.bankname = "Taipei Bank"  # 設定銀行名稱

    def save_money(self, money):  # 設定存款方法
        self.balance = self.balance + money  # 執行存款
        print("存款 ", money, " 完成")  # 列印存款完成

    def withdraw_money(self, money):  # 設定提款方法
        self.balance = self.balance - money  # 執行提款
        print("提款 ", money, " 完成")  # 列印提款完成

    def get_balance(self):  # 獲得存款餘額
        print(self.name.title(), " 目前餘額: ", self.balance)


hungbank = Banks('hung')  # 定義物件hungbank
print("目前開戶銀行 ", hungbank.bankname)  # 列出目前開戶銀行
hungbank.get_balance()  # 列出目前開戶銀行
hungbank.save_money(100)  # hung存款100
hungbank.get_balance()  # 獲得hung存款餘額
