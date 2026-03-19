#question 1
# n=int(input("Please tell your number"))

"""
for i in range(n):
  print("hello world")
"""


#Print natural number upto n

"""
for i in range(1,n+1):
     print(i)

Reverse Loop
for i in range(n, 0, -1):
    print(i);
"""


#Print table 5*1=5
"""
for i in range(1,11):
  print(f"{n} * {i}={n*i}")
  """

#Sum upto n terms
"""
sum=0;
for i in range(1,n+1):
  sum+=i;

print(f"your sum is {sum}")
"""

# Factorial of number ->5!=5*4*3*2*1

"""
fact=1;
for i in range(1,n+1):
  fact*=i;
print(f"your sum is {fact}")
"""

#  Print the sum of all even & odd numbers in a range 
"""
even=0;
odd=0;
for i in range(1,n+1):
     if i%2==0:
         even+=i;
     else:
          odd+=i;
print(f"your even and odd sum are {even},{odd}")
"""
# Print all the factors of a number 
"""
for i in range(1,n+1):
  if n%i==0:
    print(i);
"""

          

#Accept a number and check if it a perfect number or not.
#Perfect Number=>A number whose sum of factors is equal to the number itself

"""
sum=0;
for i in range(1,n):
  if n%i==0:
    sum+=i;

if sum==n:
  print("Your number is perfeect")
else:
  print("not a perfect numner")"""


# check Prime number

"""
cnt=0;
for i in range(1,n+1):
    if n%i==0:
       cnt+=1;
if(cnt==2):
    print("It is prime number")
else:
    print("It is not Prime number")
"""


#- Reverse a string without using in build functions.

"""
a="Sheriyans";
b=""
for i in range(len(a)-1,-1,-1):
  b=b+a[i];

print(b)
"""

#Check String is Plaindrome or not

"""
a="NAMAN";
b=""
for i in range(len(a)-1,-1,-1):
  b=b+a[i];
print(b)
if b==a:
  print(" your string is palindrome");
else:
  print("its not a palindrone");
"""

#Count all letters, digits, and special symbols from a given 

# Given: str1 = "P@#yn26at^&i5ve"
# Expected Outcome:
# Total counts of chars, digits, and symbols
# Chars = 8
# Digits = 3
# Symbol = 4

"""
str1 = "P@#yn26at^&i5ve"
ch=0;
dig=0;
sym=0;

for i in str1:
   if i.isdigit():
     dig+=1;
   elif i.isalpha():
     ch+=1;
   else:
     sym+=1;
print(f"your digit are {dig}\n your alphabets are {ch}\n your special characters are {sym}\n")

"""

print(dir(str));
