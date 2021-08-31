"""
12_19_2.py The redesign 12_19_1.py To solveCommon supper() is applied to multiple inheritance problems
"""


class A():
    def __init__(self):
        super().__init__()
        print('class A')


class B():
    def __init__(self):
        super().__init__()
        print('class B')


class C(A, B):
    def __init__(self):
        super().__init__()
        print('class C')


x = C()
