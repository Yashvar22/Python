class Employee:
  
  language="Py"; #this is class attribute
  salary=1200000;

harry=Employee();
harry.name="harry"; #this is obj(instance) attribute
print(harry.name,harry.language,harry.salary)

rohan=Employee();
rohan.name="roho"
print(rohan.name,rohan.salary,rohan.language)

# here name is obj attributes and salary and language are class attribute a they directly belong to class