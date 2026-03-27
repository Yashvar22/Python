# Can you change the self-parameter inside a class to something else (say
# “harry”). Try changing self to “slf” or “harry” and see the effects.

from random import randint

 
class Train:
  def __init__(slf,trainNo):
    slf.trainNo=trainNo;
    
  def book(self,fro,to):
    print(f"Ticket is booked in train no:{self.trainNo},from {fro} to {to}")
  
  def getstatus(self):
    print(f"Train no:{self.trainNo} is runnig on time")

  def getfair(self,fro,to):
    print(f"Ticket fair in train no:{self.trainNo},from {fro} to {to} is {randint(222,555)}")


t=Train(12344);
t.book("Rampur","delhi")
t.getstatus();
t.getfair("Rampur","delhi")