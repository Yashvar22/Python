#polymorphism
"""
class Animal:
  def show(self):
    print("I am Dog");


class Human(Animal):
  def show(self):
    print("I am yash")

obj=Human();
obj.show()
obj=Animal();
obj.show()
"""

#Duck typing

class Animal:
  def show(self):
    print("I am showing")

class human:
  def show(self):
    print("hello i am yash")

obj=Animal()
obj2=human()

obj.show();
obj2.show();