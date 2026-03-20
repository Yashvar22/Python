# def hello():
#   print("This is a hello function")

# hello();

#possitional argument
def sum(a,b):
  print(f"The sum of your number is {a+b}")

sum(5,6);
sum(13,90);


#Keyword argument
# def hello(name,age):
#   print(f"your name is {name} and your age is {age}")

# hello(age=22,name="yash")


#Default Argument
def sum(a,b=45):
  print(f"sum is {a+b}");

sum(4,7)


#Wheter string is plaindrome is not

def palindrome(str):
  rev="";
  for i in range(len(str)-1,-1,-1):
      rev+=str[i];
   
  if(rev==str):
     print(f"{str} is palindrome");
  else:
     print(f"{str} is Not palindrome")


palindrome("NAMAN");
palindrome("CURSOR")


#return vs print

def hello():
   return "hello how are you!"

print(hello());
