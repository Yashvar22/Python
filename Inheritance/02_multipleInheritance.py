class Employee:
  company="ITC";
  name="Yashvardhan"
  def show(self):
    print(f"the name is {self.name},company is {self.company}")

class Coder:
   language="Python";
   
   def printLan(self):
      print(f"out of all language is here your lan:{self.language}")

class Programmer(Employee,Coder):
    company="ITC infotech";
    def showLan(self):
        print(f"the name is {self.company} and he is good with {self.language} language")


a=Employee();
b=Programmer();

b.show();
b.showLan();
b.printLan()