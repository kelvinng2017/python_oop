"""
12_2_1.py:a derived class has the same name as a base class
"""


class Person():
    def job(self):
        print("i am teacher")


class LawerPerson(Person):
    def job(self):
        print("i am lawer")


hung = Person()
ivan = LawerPerson()
hung.job()
ivan.job()
