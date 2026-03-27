class Employee:
  
  language="Python"; #this is class attribute
  salary=1200000;
  
  def getInfo(self):
    print(f"the language is {self.language}, the salary is :{self.salary}");
 
 
  @staticmethod
  def greet():
    print("Good moring")


harry=Employee();
harry.language="Javascript"; #this is obj(instance) attribute
print(harry.language,harry.salary)
harry.getInfo();
Employee.greet() # static method can acces by Class Name

#Employee.getInfo(harry)