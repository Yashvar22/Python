#1 approach
# a=12;
# b=12;
# print(a+b)

#2 approach ->function
# def add(a,b):
#   print(a+b);

# add(12,45);
# add(4,5)


#OOP's

class Factory:
    a=12 #attributes

    def hello(self): #method
        print("how are you")

    print("hello how are you i am getting intialized")


print(Factory().a)
Factory().hello()