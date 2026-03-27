#.Create a class with a class attribute a; create an object from it and set ‘a’
#directly using ‘object.a = 0’. Does this change the class attribute?

class Demo:
  a=4;

o=Demo();
print(o.a) # print the class att because instance att is not present
o.a=7#instance att is set 
print(o.a)# Print the instance att because instance att is present
print(Demo.a) #

#Ans=N, it change
