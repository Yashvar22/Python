#. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animal:
   def __init__(self):
      pass
   
class Pets(Animal):
   def __init__(self):
      pass
   
class Dog(Pets):
   
   @staticmethod
   def bark():
      print("dog is barking")


o=Dog();
o.bark()
Dog.bark()