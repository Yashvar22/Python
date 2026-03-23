
# print("hello word"->Syntax error


#Indentation error
# a=12;2

# if a==12:
# print("hello")

"""
a=int(input("tell your number:-"))
# print(10/a)
# print("ok i have done the division")

try:
  print(10/a);
except Exception as err:
  print(f"sorry there is error as {err}");

print("ok i have done the divion")
"""
#Name error
# a=int(input("tell your number:-"))

# try:
#   print(10/a);
# except Exception as err:
#     print(f"sorry there is error as {err}");
# else:
#    print("good ther is no exception")
# finally:
#    print("i will run no matter what")

# print("ok i have done the divion")


#how raise works

age=int(input("tell your age:-"));
try:
   if age < 10 or age>8:
      raise ValueError("your age must be between 10 and 18");
   else :
      print("welcome to the club");
except Exception as err:
      print(f"an error occur as {err}")

print("the club will strt soon")