"""
12_30s.py Define a __repr__() method that has the same content as __str__() and can be replaced with an equal sign
"""


class Name:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '%s' % self.name
    __repr__ = __str__


a = Name('hung')
print(a)
