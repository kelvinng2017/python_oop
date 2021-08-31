"""
12_21.py A series of tests of isinstance() functions
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
print("ivan Belong to Ivan class:", isinstance(ivan, Ivan))
print("ivan Belong to Father class:", isinstance(ivan, Father))
print("ivan Belong to GrandFather class:", isinstance(ivan, Grandfaher))
print("father Belong to Ivan Class", isinstance(father, Ivan))
print("father Belong to Father Class", isinstance(father, Father))
