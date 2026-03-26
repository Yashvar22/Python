
f=open("file.txt");
"""

#lines=f.readlines() 
line1=f.readline() 
line2=f.readline() 

#print(lines,type(lines)) #=>list
print(line1,type(line1)) #=>str
print(line2,type(line2)) #=>str
"""




#read line using while loop in file.txt 

line=f.readline();
while(line != ""):
  print(line);
  line=f.readline();

f.close()