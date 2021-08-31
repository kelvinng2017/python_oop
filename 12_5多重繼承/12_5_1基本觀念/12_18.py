"""
12_18.py This program's Ivan class inherits the Father and Uncle classes, and theGrandfather class is the parent of the Father and Uncle classes
In this program, we create an object named Ivan of the Ivan class. This class calls action(),actuion() and action1(), respectively. The father and Uncle classes have action2() methods. 
You can see which action2() method is executed at the end
"""


class Grandfather():
    """define grandfather class"""

    def action1(self):
        print("Grandfather")


class Father(Grandfather):
    """define father class"""

    def action2(self):  # define action2()
        print("Father")


class Uncle(Grandfather):
    """define uncle class"""

    def action2(self):  # define action2()
        print("Uncle")


class Ivan(Father, Uncle):
    """define Ivan class"""

    def action3(self):
        print("Ivan")


ivan = Ivan()
ivan.action3()  # order Ivan
ivan.action2()  # Ivan -> Father
ivan.action1()
