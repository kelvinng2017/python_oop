"""
12_14_1.py: Extend 12_4 .py to make the Dogs category have its own method sleeping()
"""


class Animals():
    """Animals class, this us the base category"""

    def __init__(self, animal_name, animal_age):
        self.name = animal_name  # record animals name
        self.age = animal_age  # record animals age

    def run(self):  # Output animal is running
        print(self.name.title(), " is  running")


class Dogs(Animals):
    """The Dogs category, which is a derivative of Animal"""

    def __init__(self, dog_name, dog_age):
        super().__init__('My pet '+dog_name.title(), dog_age)

    def sleeping(self):
        print("My pet", "is sleeping")


mycat = Animals('lucy', 5)  # create animal object and tests
print(mycat.name.title(), ' is ', mycat.age, " years old")
mycat.run()

mydog = Dogs('lily', 6)  # create dogs object and test
print(mydog.name.title(), ' is ', mydog.age, " years old")
mydog.run()
mydog.sleeping()
