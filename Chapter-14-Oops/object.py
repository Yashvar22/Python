# class Factory:
#     a=12 #attributes

#     def hello(self): #method
#         print("how are you")

#     print("hello how are you i am getting intialized")


# obj=Factory() # this is how obj is created
# obj2=Factory()
# obj3=Factory()
# print(obj.a)
# obj.hello()

#constructors
"""
class Factory:
    
    def __init__(self,material,zips, pockets): #intialisation keyword
           self.material=material;
           self.zips=zips;
           self.pockets=pockets
    
    def show(self):
          print(f"your object details are {self.material},{self.zips},{self.pockets} ")
reebok=Factory("Leather",3,2)
campus=Factory("nylon",3,3)

reebok.show()
print(reebok.pockets);
print(campus.pockets)

  

"""


#Type of attributes

class Animal:
  name="Lion"; #class atribute
  
  def __init__(self,age):
      self.age=age; #instance attribute
  
  def show(self):  #instance method
     print(f"how are you and your age is {self.age}")
     
  @classmethod
  def hello(cls):  #class method
     print("how are you brother !")

  @staticmethod
  def static():
     print("how are you")


obj=Animal(12)

obj.show()
obj.hello()
obj.static()