#I think shortest
from random import choice
while True:
  if(input("(R)ock, (P)aper or (S)cissors?").lower() in ("r", "p", "s")):
    break
print(choice(["GG you won", "You lost :(", "Tie"]))