import random;
n=random.randint(1,100);
a=-1
guesses=0;
while(a!=n):
  guesses+=1
  a=int(input("guess a number:-"))
  if(a>n):
    print("Lower no please");
  else:
    print("higher number please")

print(f"You have gueessed the number correctly in {guesses} attemp")
