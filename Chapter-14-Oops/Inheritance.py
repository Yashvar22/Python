#inheritance-> single inheritance
"""


class Factorymumbai:#parent
  a="I am anattributes mentioned inide factory";
  def hello(self):
    print("hello i am a method mentioned inside factory")


class Factorypune(Factorymumbai):  #child class
    pass;


obj=Factorymumbai();
obj2=Factorypune()
# print(obj.a);
# print(obj.hello())
obj2.hello()
"""


#Constructor
"""
class Animal:
   def __init__(self,name):
       self.name=name;
   
   def show(self):
       print(f"hello this is your name is {self.name} ")



class Human(Animal):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age;
   
    def show(self):
       print(f"hello this is your name is {self.name} and your age is {self.age}") 

ani1=Animal("Cow")
per1=Human("Yash",34)

ani1.show()
per1.show()"""


#Multiple inheritance

"""
class Animal:
 
  def __init__(self,name):
    pass
class Human:
   def __init__(self,name,age):
    pass

class Robot(Animal,Human):
  name3="charlie273"

obj1=Robot();
print(obj1.name1);
print(obj1.name2);
print(obj1.name3);"""


#MultiLevel Inheritance

"""
class Factory:
  def __init__(self,material,zips):
    self.material=material;
    self.zips=zips;

class bhopalFacory(Factory):
   def __init__(self,material,zips,color):
     super().__init__(material,zips);
     self.color=color;

   def show_bhopal_details(self):
     print(f"Material: {self.material}")
     print(f"Zips: {self.zips}")
     print(f"Color: {self.color}")

class PuneFactory(bhopalFacory):
   def __init__(self,material,zips,color,pocket):
    super().__init__(material,zips,color);
    self.pocket=pocket;


obj = PuneFactory("Leather", 2, "Black", 5)

# Access all properties
print(obj.material)
print(obj.zips)
print(obj.color)
print(obj.pocket)
obj.show_bhopal_details()


"""