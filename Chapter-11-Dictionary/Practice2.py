# Write a program to create a dictionary of Hindi words with values as their English


"""
words={
  "madad":"help",
  "kursi":"chair",
  "billi":"cat",
  "kuttta":"dog"
}


word=input("Enter the word you want meaning of:-");

print(words[word])
"""

#Write a program to input eight numbers from the user and display all the unique numbers (once).

"""
s=set();
n=input("Enter number:-")
s.add(int(n));
n=input("Enter number:-")
s.add(int(n));
n=input("Enter number:-")
s.add(int(n));
n=input("Enter number:-")
s.add(int(n));
n=input("Enter number:-")
s.add(int(n));
n=input("Enter number:-")
s.add(int(n));

print(s);
"""

#Can we have a set with 18 (int) and '18' (str) as a value in it?

"""
s=set();
s.add(18);
s.add('18');
print(s)
"""
#Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
"""
d={};
name=input("Enter friends name:-");
lang=input("Enter lang name:- ")
d.update({name:lang})

name=input("Enter friends name:-");
lang=input("Enter lang name:- ")
d.update({name:lang})

name=input("Enter friends name:-");
lang=input("Enter lang name:- ")
d.update({name:lang})

name=input("Enter friends name:-");
lang=input("Enter lang name:- ")

d.update({name:lang})

print(d)
"""

#If the names of 2 friends are same; what will happen to the program in problem 6?


#Can you change the values inside a list which is contained in set S?


# s={8,7,12,"harry",[1,2]};
# why not update
# 1. hum list ko set mai use ni kr skte beacuse list are mutable and set are immuatable