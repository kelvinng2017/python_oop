"""
12_20.py Lists the data forms of class objects and methods within them
"""


class Grandfaher():
    """define grandfather class"""
    pass


class Father(Grandfaher):
    """define father class"""
    pass


class Ivan(Father):
    """define Ivan class"""

    def fn(self):
        pass


grandfaher = Grandfaher()
father = Father()
ivan = Ivan()
print("grandfather object item: ", type(grandfaher))
print("father object item: ", type(father))
print('ivan object item:', type(ivan))
print("ivan object fn method item:", type(ivan.fn))
