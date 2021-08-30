"""
12_11_1.py Derived classes and base classes have the same simple instructions each time
"""


class Person():
    def __init__(self, name):
        self.name = name


class LawerPerson(Person):
    def __init__(self, name):
        self.name = name + "lawyer"


hung = Person("kelviinng")
lawer = LawerPerson("kelvinng")
print(hung.name)
print(lawer.name)
