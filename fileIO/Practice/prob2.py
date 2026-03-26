import random;
def game():
  print("Your are playing the game");
  score=random.randint(1,62)

  #fetch the highscore
  with open("fileIO/Practice/hi-score.txt") as f:
    hiscore=f.read(); #string mai aata hai res
    if hiscore!="":
      hiscore=int(hiscore);
    else:
      hiscore=0
  print(f"your score:{score}")

  if (score>hiscore or hiscore==""):
       # write this highscore to file
       with open("fileIO/Practice/hi-score.txt","w") as f:
          f.write(str(score));  
          
  return score ;

game();