"""
12_9_8.py 設計Father類別，也設計Son類別, Son類別繼承了Father類別,Father類別有hometown()方法，然後Father類別和Son類別物件
階會呼叫hometown()方法。
"""
class Father():
    def hometown(self):
        print("我住在臺北")

class Son(Father):
    pass

hung = Father()
ivan = Son()
hung.hometown()
ivan.hometown()