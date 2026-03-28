import random;
n=random.randint(1,100);
a=-1
guesses=1;
while(a!=n):
  a=int(input("guess a number:-"))
  if(a>n):
    print("Lower no please");
    guesses+=1
  elif(a<n):
    print("higher number please")
    guesses+=1

print(f"You have gueessed the number {n} correctly in {guesses} attemp")
