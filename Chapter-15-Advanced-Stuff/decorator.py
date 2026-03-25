# class Animal:
#   @property
#   def show(self):
#     print("hello how are you")

# obj=Animal();
# obj.show


# how to create decorator
def decorate(func):
    def wrapper(*args,**kwargs):
       print("the addition to your number are")
       func(*args,**kwargs);
       print("thankyou i hope you like it")
    return wrapper

# @decorate
# def hello():
#   print("hello i am yash")

# hello()
@decorate
def addition(a,b):
  print(f"your total is {a+b}")

addition(12,67)


