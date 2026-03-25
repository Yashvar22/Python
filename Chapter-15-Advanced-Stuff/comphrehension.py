
"""
#create a list of 1 to 20 even no

# l=[];
# for i in range(1,21):
#   if i%2==0:
#     l.append(i);

# print(l)

# list comphrehensation
l=[i for i in range(1,21) if i%2==0]
print(l)
"""


#dic compherehenstion
dic={i : i**2 for i in range(1,21)}

print(dic)

#set compherehenstion

set={x*x for x in range(1,10) if x%2 ==0}

print(set)