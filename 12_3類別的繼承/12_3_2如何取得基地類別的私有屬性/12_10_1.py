"""
12_10_1.py:設計一個子類別Son的物件存取父類別的私有屬性的應用
"""



class Father():
    def __init__(self):
        self.__address = "臺北市儸散福路";
    
    def getaddr(self):
        return self.__address

class Soon(Father):
    pass

hung = Father()
ivan = Soon()
print("父類別:",hung.getaddr())
print("子類別:",ivan.getaddr())