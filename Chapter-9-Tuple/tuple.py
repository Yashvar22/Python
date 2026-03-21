"""
a=(1,2,3,4,5,5,5,5,"hello");
# a[0]=12;
print(a[4])
print(type(a))

#1st way of traversing
for i in a:
  print(i)

#2st way of traversing
for i in range(len(a)):
  print(a[i])
"""

#methods of tuple

# a=(1,2,3,4,5,5,5.5,"hello");

# idx=a.index(5);
# cnt=a.count(5)
# print(idx,cnt)



#Tuple unpacking

a,b,c,d=(1,2,3,4);#unpacking variables

print(a,b,c,d)

d=(1);
print(type(d)) #int



