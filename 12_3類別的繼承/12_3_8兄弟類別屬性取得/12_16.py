"""
12_16.py The Father class is the parrent of Ivan and Ira classes,so Ivan and Ira are siblings. This Program reads the Father and Ira asset attributes from Ivan
and Ira classes,respectively
"""


class Father():
    """define father's assets"""

    def __init__(self):
        self.fathermoney = 1000


class Ira(Father):  # Father class is Father
    """define Ira's assets"""

    def __init__(self):
        self.iramoney = 8000
        super().__init__()


class Ivan(Father):  # Father class is Father
    """define Ivan's assets"""

    def __init__(self):
        self.ivanmoney = 3000
        super().__init__()

    def get_money(self):  # Obtain asset details
        print("Ivan asset:", self.ivanmoney,
              "\nfather asset:", self.fathermoney,
              "\nIra asset:", Ira().iramoney)


ivan = Ivan()
ivan.get_money()
