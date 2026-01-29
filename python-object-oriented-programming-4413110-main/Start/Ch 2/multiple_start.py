# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance

# 对于类 C，MRO 列表是这样的： [C, A, B, object] Method Resolution Order
class A:
    def __init__(self):
        # 一定要写
        super().__init__()
        self.prop1 = "prop1"
        self.name = "Class A"


class B:
    def __init__(self):
        # 良好习惯，继承Object
        super().__init__()
        self.prop2 = "prop2"
        self.name = "Class B"


class C(A, B):
    def __init__(self):
        super().__init__()
    def showprops(self):
        print(self.prop1)
        print(self.prop2) 
        print(self.name) 


c = C()
# 看到链
print(C.__mro__)
c.showprops()
