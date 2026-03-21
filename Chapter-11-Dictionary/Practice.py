#1->pyhton script to merge two python dict

"""
d={10:100,20:200,30:300,40:400};
d2={5:500,6:600}

for i in d2:
  d[i]=d2[i]

print(d)
"""

#2->Python program to sum all the values in a dict
"""
d={10:100,20:200,30:300,40:400};

sum=0
for i in d:
   sum=sum+d[i]

print(sum)"""


#3->Count the freq of each elem
"""
a=[1,1,1,2,2,2,3,3,3,3,3,4,4,4,4,5,6,7,8];

d={};
for i in a:
  if i in d.keys():
     d[i]+=1;
  else:
     d[i]=1;
print(d)
"""

#4->Write a Python program to combine two dictionary by adding values for common keys
d={10:100,20:200,40:300};
d2={40:400,50:500,60:600};

for i in d2:
    if i in d.keys():
        d[i]=d[i]+d2[i]
    else:
        d[i]=d2[i]
print(d)
