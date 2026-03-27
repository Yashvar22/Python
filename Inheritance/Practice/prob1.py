class TwoDvector:
    def __init__(self,i,j):
        self.i=i;
        self.j=j
    
    def show(self):
      print(f"the vec is {self.i}i+{self.j}j")

class ThreeDvector(TwoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j);
        self.k=k;
    def show(self):
      print(f"the vec is {self.i}i+{self.j}j+{self.k}k")
a=TwoDvector(1,2);
b=ThreeDvector(5,2,3);
a.show();
b.show()