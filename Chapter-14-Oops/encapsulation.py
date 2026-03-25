#encapsulation

"""
class Factory:
   _a="pune";
   def show(self):
      print("i am a pune factory")

class Bhopal(Factory):
   def show2(self):
      print(super()._a)

obj=Bhopal();
obj.show2()"""





class Factory:
   __a="pune"; #private access modifiers
   def show(self):
      print(Factory.__a)

obj=Factory();

obj.show()

