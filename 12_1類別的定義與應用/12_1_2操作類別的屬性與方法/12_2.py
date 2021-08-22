#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
擴充ch12_1.py,列出銀行名稱與服務宗旨
"""
class Banks():
    '''定義銀行類別'''
    bankname = "Taipei Bank" #定義屬性
    def motto(self): #定義方法
        return "以客為尊"

userbank = Banks() #定義物件userbank
print userbank.bankname
print userbank.motto()

