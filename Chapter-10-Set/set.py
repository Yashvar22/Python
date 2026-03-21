# s={}  #dictionary
# set={1,2,3,4,5,4,5,5}

# print(set)

#how set stores value in Python

# b=hash("hello")
# print(b)

# c=hash((1,2,3,4,5))
# print(c)


#Set Traversing

# set={1,8,9,"hello",2,3,4,5};  

# for i in set:
#   print(i)


#Set methods
"""

set={8,1,2,3};

set.add(4);
set.remove(2)
set.discard(2)
set.pop()
set.clear()

print(set)"""


#

A={1,2,3,4,5};
B={4,5,6,7,8};

# s=A.union(B); #A|B
# s=A.intersection(B) #A&B
# s=B.difference(A) #B-A
# s=A.symmetric_difference(B) #A^B
B-=A;
print(B)



