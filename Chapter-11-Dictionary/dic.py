# d={
#    1:"hello",
#    2:56,
#    6:"hello" 
# }
# print(type(d))

"""
d={10:100,20:200,30:300,40:400}

# d[10]=1000# update
d.update({50:500}) #or  d[50]=500;  #creating 

# del d[30] #deleting
print(d.get(30))

print(d)
"""



"""
a = {
"key": "value",
"harry": "code",
"marks": "100",
"list": [1, 2, 9]
}
print(a["key"]) # Output: "value"
print(a["list"]) # Output: [1, 2, 9]
"""


# Dict Traversing
"""
d={10:100,20:200,30:300,40:400}

for i in d:
  print(d.get(i))"""

#Dic methods
# print(help(dict))



#concept of deep copy vs shallow copy
"""
# deep copy in list same as dict
a=[1,2,3,4,5]

b=a;

b[0]=100;
print(a)
print(b)

#shallow copy in list same as dict
a=[1,2,3,4,5]

b=a.copy();

b[0]=100;
print(a)
print(b)"""

d={10:100,20:200,30:300,40:400}

# d2=d.copy();

d2=d.get(20) #200;
print(d.items())
print(d.values())

