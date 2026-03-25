#Dunder-Mathod
class Animal:
  def __init__(self,name,age):
    self.name=name;
    self.age=age;

  def __str__(self):
     return f"hello how are you and your name is {self.name}";

  def __add__(self, other):
     sum=0;
     for i in other:
        sum=sum+i.age;
     return f"your sum of ages are {self.age + sum}"
obj=Animal("Cow",67);
obj2=Animal("dolphinc",88)
obj3=Animal("Tiger",34)
print(obj+(obj2,obj3))