import json
import random
import string

from pathlib import Path;

class Bank:
   database='data.json'
   data=[];
   try:
       if Path(database).exists():
          with open(database) as fs:
             data=json.loads(fs.read());
   
       else:
          print("No uch file exists")
   except Exception as err:
      print(f"an exception occ as {err}")

   @classmethod
   def __update(cls):
      with open(cls.database,'w') as fs:
          fs.write(json.dumps(Bank.data))

   @classmethod
   def __accountgenerate(cls):
      alpha=random.choices(string.ascii_letters,k=3);
      num=random.choices(string.digits,k=3);
      spchar=random.choices("!@#$%^&*",k=1);
      id=alpha+num+spchar;
      random.shuffle(id); #obj ke jaisa dikhega->list milti hai
      return "".join(id)
   

   def Createaccount(self):
      info={
         "name":input("Tell you name:- "),
         "age":int(input("Tell your Age:- ")),
         "email":input("tell you email:-"),
         "pin": int(input("Tell your 4  number pin:- ")),
         "accountNo":Bank.__accountgenerate(),
         "balance":0,
      }
      if(info['age']<18 or len(str(info['pin']))!=4):
         print("sorry you cannot create your account")
      else:
         print("account has been created successfully")
        
         for i in info:
            print(f"{i} : {info[i]}");
         print("please note down your account number")
         
         Bank.data.append(info)
         Bank.__update()

   def Depositmoney(self):
      accno=input("Please tell your acc Number:-")
      pin=int(input("pleae tell your pin:- "));
      #print(Bank.data)

      userdata=[i for i in Bank.data if i['accountNo']==accno and i['pin']==pin]

      if userdata==False:
         print("No data Found")
      else:
         amount=int(input("how much you want to deposit:-"))

         if amount >10000 and amount>0:
            print("sorry amt is to much you can deposit below 10000")
         else:
            print(userdata);
            userdata[0]['balance']+=amount;

            Bank.__update();
            print("bank deposited successfully")
  
   def Withdrawmoney(self):
      accno=input("Please tell your acc Number:-")
      pin=int(input("pleae tell your pin:- "));
      #print(Bank.data)

      userdata=[i for i in Bank.data if i['accountNo']==accno and i['pin']==pin]

      if userdata==False:
         print("No data Found")
      else:
         amount=int(input("how much you want to withdraw:-"))

         if userdata[0]['balance'] < amount and amount>0:
            print("sorry you dont have that much money")
         else:
            print(userdata);
            userdata[0]['balance']-=amount;

            Bank.__update();
            print("Amt withdrew successfully")
   
   def Showdetails(self): 
      accno=input("Please tell your acc Number:-")
      pin=int(input("pleae tell your pin:- "));
      
      userdata=[i for i in Bank.data if i['accountNo']==accno and i['pin']==pin]
      print(userdata)
      print("your information are \n\n\n")
      for i in userdata[0]:
         print(f"{i}:{userdata[0][i]}")
  

   def Updatedetails(self):
      accno=input("Please tell your acc Number:-")
      pin=int(input("pleae tell your pin:- "));
      #print(Bank.data)

      userdata=[i for i in Bank.data if i['accountNo']==accno and i['pin']==pin]
      
      if userdata==False:
         print("No such user found");
      
      else:
         print("You cant no change age,accountno,balance")

         print("Fill the details for change or leave it empty i no change ")

         newdata={
            "name":input("please tell your new name or enter"),
            "email":input("please tell your new email or enter"),
            "pin":input("Enter new pin or press enter to skip ")
         }

         if newdata['name']=="":
            newdata['name']=userdata[0]['name'];
         if newdata['email']=="":
            newdata['email']=userdata[0]['email'];
         if newdata['pin']=="":
            newdata['pin']=userdata[0]['pin'];
         
         newdata['age']=userdata[0]['age'];
         newdata['accountNo']=userdata[0]['accountNo'];
         newdata['balance']=userdata[0]['balance'];
        

         if type(newdata['pin'])==str:
            newdata['pin']=int(newdata['pin'])

         for i in newdata:
            if newdata[i] ==userdata[0][i]:
               continue;
            else:
               userdata[0][i]=newdata[i];
         

         Bank.__update();
         print("details updated sucessfully")

   def Delete(self):
      accno=input("Please tell your acc Number:-")
      pin=int(input("pleae tell your pin:- "));
      #print(Bank.data)

      userdata=[i for i in Bank.data if i['accountNo']==accno and i['pin']==pin]

      if userdata==False:
         print("sorry no such data exists")
        
      else:
         check=input("press y if you actually want to delete account or n to cancel: ")

         if check.lower() == 'n':
            print("bypass")
         elif check.lower() == 'y':
            idx = Bank.data.index(userdata[0])
            Bank.data.pop(idx)
            print("Account deleted successfully")
            Bank.__update()
         else:
            print("Invalid choice, delete canceled")
         

user=Bank();

print("Press 1 for creating an Account:-")
print("Press 2 for Depositing the money in the bank")
print("press 3 For withdrawing the money");
print("press 4 for details")
print("Press 5 for updating the details:")
print("press 6 for delete your account:-")


check=int(input("tell your response:-"))

if check==1:
   user.Createaccount();

if check==2:
   user.Depositmoney();

if check==3:
   user.Withdrawmoney();

if check==4:
   user.Showdetails();
if check==5:
   user.Updatedetails();
if check==6:
   user.Delete();