"""
12_28.py List ofther objects without defining the __str()__ method
"""


class Name:
    def __init__(self, name):
        self.name = name


a = Name('hung')
print(a)
