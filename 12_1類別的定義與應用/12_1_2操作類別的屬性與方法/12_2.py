"""
12_2.py擴充12_1.py，列出銀行名稱與服務宗旨
"""


class Banks():
    '''定義銀行類別'''
    bankname = 'Taipei Bank'  # 定義屬性

    def motto(self):  # 定義方法
        return "以客爲尊"


userbank = Banks()
print("目前服務的銀行是 ", userbank.bankname)
print("銀行服務的理念是 ", userbank.motto())
