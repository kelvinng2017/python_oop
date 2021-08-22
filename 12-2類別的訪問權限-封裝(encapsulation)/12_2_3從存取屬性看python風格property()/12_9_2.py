"""
將score設為私有屬性，設計含getter觀念的getscore()和setter觀念的setscore()存取分數，這時外部無法直接存取score。
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


stu = Score(0)
print(stu.getscore())
stu.setscore(80)
print(stu.getscore())

stu.score = 100
print(stu.getscore())
