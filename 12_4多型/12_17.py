"""
12_7.py Animals is a base class. Dogs is a derivative of Animals. Based on inherited properties, both classes have which() and action() methods.
An unrelated class of Monkeys is designed that also has which() and action() methods. The program then calls which() and action() methods, respectively, and determines which method to respond to the 
program based on the object category
"""


class Animals():
    """Animals class,this is base class"""

    def __init__(self, animal_name):
        self.name = animal_name  # record animal name

    def which(self):  # return animals name
        return 'My Pet ' + self.name.title()

    def action(self):  # animal behavior
        return ' sleeping'


class Dogs(Animals):
    """The Dogs category, which is a derivative of Animals"""

    def __init__(self, dog_name):  # record animals name
        super().__init__(dog_name.title())

    def action(self):  # animal behavior
        return ' running in the street'


class Monkeys():
    """moneky class, this other class"""

    def __init__(self, monkey_name):  # record animal name
        self.name = 'My moneky '+monkey_name.title()

    def which(self):  # return animal name
        return self.name

    def action(self):  # animal behavior
        return ' running in the forest'


def doing(obj):  # list animal behavior
    print(obj.which(), obj.action())


my_cat = Animals('lucky')  # Animals object
doing(my_cat)
my_dog = Dogs('gimi')  # Dogs object
doing(my_dog)
my_monkey = Monkeys('taylor')  # Monkets object
doing(my_monkey)
