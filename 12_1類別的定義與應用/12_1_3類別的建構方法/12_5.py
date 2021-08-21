"""
12_5.py:使用與12_4.py相同的Banks類別，然後定義2個物件使用操作這個類別
"""


class Banks():
    '''定義銀行類別'''
    bankname = 'Taipei Bank'  # 定義屬性

    def __init__(self, uname, money):  # 初始化發放 init是initalization的縮寫
        self.name = uname  # 設定存款者名字
        self.balance = money  # 設定所存的錢

    def save_money(self, money):  # 設定存款方法
        self.balance = self.balance + money  # 執行存款
        print("存款 ", money, " 完成")  # 列印存款完成

    def withdraw_money(self, money):  # 設定提款方法
        self.balance = self.balance - money  # 執行提款
        print("提款 ", money, " 完成")  # 列印提款完成

    def get_balance(self):  # 獲得存款餘額
        print(self.name.title(), " 目前餘額: ", self.balance)


hungbank = Banks('huang', 100)  # 定義物件 hungbank
johnbank = Banks('john', 300)  # 定義物件johnbank
hungbank.get_balance()  # 獲得hung存款餘額
johnbank.get_balance()  # 獲得john存款餘額
hungbank.save_money(100)  # hung存款100元
johnbank.withdraw_money(150)  # john 提款150
hungbank.get_balance()  # 獲得hung存款餘額
johnbank.get_balance()  # 獲得john存款餘額
