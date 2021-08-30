"""
12_15.py This program creates an Ivan class object,Ivan and calls the Father and GrandFathe methods to print the information
and then gets the Father and GrandFather attributes,respectively
"""


class Grandfather():
    """Define grandfather's assets"""

    def __init__(self):
        self.grandfathermoney = 10000

    def get_info1(self):
        print("Grand's in formation")


class Father(Grandfather):  # father class is Grandfather
    """Define father's assets"""

    def __init__(self):
        self.fathermoney = 8000
        super().__init__()

    def get_info2(self):
        print("Father's in formation")


class Ivan(Father):  # father class is Father
    """Define Ivan's assets"""

    def __init__(self):
        self.ivanmoney = 3000
        super().__init__()

    def get_info3(self):
        print("Ivan's in formation")

    def get_money(self):
        print("\nIvan assets:", self.ivanmoney,
              "\nfather assets:", self.fathermoney,
              "\ngrandfather assets", self.grandfathermoney)


ivan = Ivan()
ivan.get_info3()  # Obtained from Ivan
ivan.get_info2()  # process Ivan ->Father
ivan.get_info1()  # process Ivan -> Father -> GrandFather
ivan.get_money()  # Acquisition of assets obviously
