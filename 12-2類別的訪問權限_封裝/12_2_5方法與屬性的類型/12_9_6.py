"""
類別方法與屬性的應用，這個程式執行時，每次建立Counter()類別物件(11-13行)，類別屬性值會更新，此外這個程式使用類別每次就可以直接調用類別屬性與方法
"""

class Counter():
    counter = 0 #類別屬性，可由類別本身調用
    def __init__(self):
        Counter.counter = Counter.counter + 1 #更新指標
    
    @classmethod
    
    def show_counter(cls): #類別方法，可由類別本身調用
        print("class method")
        print("counter = ",cls.counter) #也可以用Counter.counter調用
        print("counter = ",Counter.counter)

one = Counter()
two = Counter()
three = Counter()
Counter.show_counter()