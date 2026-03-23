"""
1 for snake
-1 for water
0 for gun

"""
import random;
computer=random.choice([-1,0,1]);
youstr=input("Enter you choice:-");

youDict = {
  "s":1,
  "w":-1,
  "g":0,
};

you=youDict[youstr]


if(computer==you):
  print("its a draw")

else:
  if(computer==-1 and you==1):
     print("you win");
  elif(computer==-1 and you==0):
     print("You Loose");
  elif(computer==1 and you==-1):
     print("You Loose");
  elif(computer==1 and you==0):
     print("You win");
  elif(computer==0 and you==-1):
     print("You Losse");
  elif(computer==0 and you==1):
     print("You win");
  else:
     print("some thing went wrong")