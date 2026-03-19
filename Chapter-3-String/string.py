""" String"""
a='A';
print(ord(a))#65
b=65;
print(chr(b))#A

#String Indexing

st="SHER CODER"

print(st[-1],st[3])

#String Slicing [st_idx,end_idx,]
print(st[5::2])#CDR SkIP values


#String funtions
str="yashvardhan"

#1 len() funtion
print(len(str))
#2 String.endswith("yash")
print(str.endswith("an"))
#3 str.count("a")
print(str.count('y'))
#4 capitazile()->first ch capital
print(str.capitalize())
#5 find(word)
print(str.find('h'))
#6 replace(old,new)
print(str.replace('yashvardhan','Anchal'))


