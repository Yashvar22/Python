# def addition(*args):
#   sum=0;
#   for i in args:
#     sum=sum+i;  
#   print(sum);
# addition(23,3,4,44,6,7)


#kwargs
def information(**kwargs):
   for i in kwargs:
      print(f"{i} : {kwargs.get(i)}")



information(name="yash",age=45,designation="Ai/ml")


