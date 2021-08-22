"""
定義成績類別Score，這時外部可以列印與修改成績
"""


class Score():
    def __init__(self, score):
        self.score = score


stu = Score(50)
print(stu.score)
stu.score = 100
print(stu.score)
