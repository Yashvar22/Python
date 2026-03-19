# question 1
"""
num1=int(input("please tell your first number:-"))
num2=int(input("please tell your second number:-"))

if num1>num2:
  print(f"{num1} is greater then {num2}")
elif num2>num1:
   print(f"{num2} is greater then {num1}")
else :
   print("Both number are same")
"""

#Question 2
"""
gen=input("Pleae tell your gender as character (M or F):-")

if gen=='M' or gen=='m':
  print("Good mornig Sir")
elif gen=='F'or gen=='f':
  print("Good morning mam")
else:
  print("please give me valid character")
"""

#Question 3
"""
num=int(input("Please tel your number:-"))

if num%2==0:
  print("even number")
else:
  print('odd num')"""


#Question 4
"""
name=input("Please tell your name:-")
age=int(input("please tell your age:-"))

if age>=18:
  print(f"hello {name} you are a valid vote")
else :
  print("you are not valid voter")
"""

#question 5 leap year

"""
year=int(input("Tell your year:-"))

if year%100==0 and year%400==0:
  print("Its a leap year")

elif year%100 !=0 and year%4==0:
  print("Its a leap year")
else:
  print("its not leap year")
"""

#if-elif ladder

temp=int(input("Please tell the temperature:- "))

if temp<0:
  print("Freezing Cold")
elif temp>=0 and temp<10:
  print('Very Cold')
elif temp>=10 and temp<20:
  print("COld")
elif temp>=20 and temp<30:
  print("Pleasant")
elif temp>=30 and temp<40:
  print("Hot")
else :
  print("Very Hot")










