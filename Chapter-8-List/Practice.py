
#1- print postive first and then negative
"""
l=[-45,67,-68,-69,34]


print("Positive elements are:-")
for i in l:
    if i>=0:
        print(i);
print("negative elements are:-")
for i in l:
    if i<0:
        print(i)
"""
# 2-mean of list elemet

"""
l=[1,2,3,4];

sum=0;
for i in l:
  sum+=i;

print(sum/len(l))
"""

#3- Find the gretes elements and print its idx too

"""
l=[12,36,14,19,128,6,13];

larger=l[0];
idx=0;
for i in range(len(l)):
   if l[i]>larger:
      larger=l[i];
      idx=i;

print(f"your largest number is {larger} and at idx of {idx}")"""



#4- Second greatest number

"""
l=[12,16,13,19,17];

larger=l[0];
second_lar=l[0];
idx=0;
for i in range(len(l)):
   if l[i]>larger:
      second_lar=larger;
      larger=l[i];
   elif l[i]>second_lar:
      second_lar=l[i];
     
print(f"your second largest number is {second_lar}")"""

#5- check list is sorted or not
a=[12,13,14,15,16];

for i in range(len(a)-1):
   if a[i]<a[i+1]:
      continue;
   else:
      print("your list is not sorted")
      break;
else:
   print("yor list is sorted")




