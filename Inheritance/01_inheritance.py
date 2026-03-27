class Employee:
  company="ITC";

  def show(self):
    print(f"the name is {self.name},salary is {self.salary}")

# class Programmer: instead of doing thi Use Inheritance
#    def show(self):
#     print(f"the name is {self.name},salary is {self.salary}")

#    def showLan(self):
#      print("the name is {self.name} and he is good with {self.language} language")

class Programmer(Employee):
    company="ITC infotech";
    def showLan(self):
        print("the name is {self.name} and he is good with {self.language} language")


a=Employee();
b=Programmer();

print(a.company,b.company)