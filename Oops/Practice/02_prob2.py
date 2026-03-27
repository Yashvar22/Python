#2 Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator:
   def __init__(self,n):
      self.n=n;
   
   def Square(self):
      print(f"the square is {self.n*self.n}");
   def Cube(self):
      print(f"the square is {self.n*self.n*self.n}");
   def Squareroot(self):
      print(f"the square is {self.n**1/2}");
 
a=Calculator(4);
a.Square()
a.Cube()
a.Squareroot()