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
print("father Belong to Grandfaher Class", isinstance(father, Grandfaher))
print("grandfather Belong to Ivan Class", isinstance(grandfaher, Ivan))
print("grandfather Belong to Father Class", isinstance(grandfaher, Father))
print("grandfather Belong to Grandfaher Class",
      isinstance(grandfaher, Grandfaher))
