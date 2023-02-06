class A:
    def b(self): print(10)

class B(A):
    def b(self): print(20)

class C(A):
    def b(self): 
        super().b()
        print(30)

class CB(C,B):
    pass

CB().b()