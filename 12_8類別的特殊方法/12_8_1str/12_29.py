"""
12_29.py In defining the __str()__ method. reprogram
"""


class Name:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '%s' % self.name


a = Name('hung')
print(a)
