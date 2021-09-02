"""
12_23.py  Methods that apply file annotations to categories and withn categories
"""


from re import X
from this import d


class Myclass:
    """
    File string instances of the Myclass class application
    """

    def __init__(self, x):
        self.x = x

    def printMe(self):
        """
        Application of the printMe method in the MyClass class of literal string instances
        """
        print("Hi", self.x)


data = Myclass(100)
data.printMe()
print(data.__doc__)
print(data.printMe.__doc__)
