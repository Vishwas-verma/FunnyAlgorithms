import random

def guess_num():
  num=random.randint(1,100)
  chance=1
  while chance<=5:
    n=int(input("Guess The Number : "))
    if num==n:
      return "You Win"
     else:
      chance+=1
      return "Try Again"
    return "You Lose"
 
game_play='Y'
while game_play='y' or game_play='Y':
  guess_num()
  game_play=input("Do You Wanna PLay Again? ")
