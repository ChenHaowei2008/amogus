#directions to the team without mental disabilities?
#no maidens?
import os
import time
while True:
  print("Enter the name of the game from the following list:")
  with os.scandir('games/') as games:
    i = 0
    for game in games:
      if(game.name.endswith(".py")):
        i += 1
        print("[" + str(i) + "] " + game.name[:-3])
    
  selected = input("")
  try:
    with open("games/" + selected.lower() + ".py") as game:
      os.system("clear")
      print("You have chosen " + selected + "\n")
      exec(game.read())
  except FileNotFoundError:
    if(selected.isdigit()):
      print("Choose the name, not the number. I am too lazy to add this feature in")
    else:
      print("That isn't an option")
  time.sleep(3)
  os.system("clear")