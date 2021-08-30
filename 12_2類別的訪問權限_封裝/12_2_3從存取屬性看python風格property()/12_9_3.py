"""
12_9_3.py 使用Python風格重新設計12_19_2.py，讀者需留意第11行的property(),在這裏設定sc當作property()的傳回值，未來可以直接有sc
存取私有屬性__score。
"""


class Score():
    def __init__(self, score):
        self.__score = score

    def getscore(self):
        print("inside the getscore")
        return self.__score

    def setscore(self, score):
        print("inside the setscore")
        self.__score = score

    sc = property(getscore, setscore)  # Python 風格


stu = Score(0)
print(stu.sc)
stu.sc = 80
print(stu.sc)
