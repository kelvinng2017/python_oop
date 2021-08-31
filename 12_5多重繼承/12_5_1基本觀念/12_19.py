"""
The 12_18.py program is basically redesigned with different names for the Father and Uncle classes, Fath is action3() and Uncle is action2(), 
The program launches the actionX() method of the Ivan class separately after the Ivan object of the Ivan class is created
"""


class Grandfather():
    """define grandfather class"""

    def action1(self):
        print("Grandfather")


class Father(Grandfather):
    """define father class"""

    def action3(self):  # define action2()
        print("Father")


class Uncle(Grandfather):
    """define uncle class"""

    def action2(self):  # define action2()
        print("Uncle")


class Ivan(Father, Uncle):
    """define Ivan class"""

    def action4(self):
        print("Ivan")


ivan = Ivan()
ivan.action4()
ivan.action3()  # order Ivan
ivan.action2()  # Ivan -> Father
ivan.action1()
