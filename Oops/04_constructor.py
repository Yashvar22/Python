class Employee:
  
  language="Python"; #this is class attribute
  salary=1200000;
  
  def __init__(self,name,salary,language): #dunder method which is automatically called .
    self.name=name;
    self.salary=salary;
    self.language=language;
    print("I am creating an object")
    print(f"Name:{name} Salary:{salary} Language:{language}")


  def getInfo(self):
    print(f"the language is {self.language}, the salary is :{self.salary}");
 
 
  @staticmethod
  def greet():
    print("Good moring")


harry=Employee("harry",130000,"JavaScript");

#harry.name="Yashvardhan Singh"
#print(Employee.language) Acessing class attribute by class name
print(harry.name,harry.salary)