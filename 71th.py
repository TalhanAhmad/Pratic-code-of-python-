class TwoDvector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"The 2D vector is {self.i}i and {self.j}j")    
class ThreeDvector(TwoDvector):
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
    def show(self):
        print(f"The 3D vector is {self.i}i and {self.j}j and {self.k}k")    

a = TwoDvector(1,2)
a.show()
b =ThreeDvector(1,2,3)
b.show()