#abstraction

from abc import ABC,abstractmethod

class Abstract(ABC): #Abstaract Class
  @abstractmethod
  def perimeter(self):
    pass;
  
  @abstractmethod
  def area(self):
    pass;
 
class Square(Abstract):
   def __init__(self,side):
     self.side=side;
   def perimeter(self):
     print("i have created")
   def area(self):
     print("i have done")
   

class Circle(Abstract):
  def __init__(self,radius):
    self.radius=radius;
  def perimeter(self):
     print("i have created")
  def area(self):
     print("i have done")

obj=Circle(7)
obj.perimeter()
obj2=Square(5)