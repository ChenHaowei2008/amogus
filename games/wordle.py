#Done, needs cleaning up

from colorama import Fore, Back, Style
from time import sleep
from random import choice

print("Welcome to wordle!")
print("You know the rules and so do I.\n")
while True:
  diff = input("Select difficulty (E, N, H, Custom) ").upper()
  if(diff == "N"):
    print("You chose Normal")
    difficulty = 5
  if(diff == "E"):
    print("You chose Easy")
    difficulty = 3
  if(diff == "H"):
    print("You chose Hard")
    difficulty = 7
  if(diff == "CUSTOM"):
    #Did not convert length to int to avoid errors when player enters nothing or a string
    length = input("Please enter word length(1-9) ")
    while length not in [str(i) for i in range(1,10)]:
      length = input("Please enter word length(1-9) ")
    difficulty = length
  try:
    difficulty
  except NameError:
    pass
  else:
    break


#PySpellChecker, enchant and literally every other english dictionary/spell checker does not work on replit for some reason, so im stuck with this "do it myself" method
if(int(difficulty) not in [3,5,7]):
  print("Note: Setting up may take some time")
  with open("games/assets/words_alpha.txt") as file:
    #using this hard to read list comprehensions because it is faster
    #gotta have that optimisation baby
    words = [word for word in file.read().splitlines() if len(word) == int(difficulty)]

else:
  #easy and hard are not done yet
  with open("games/assets/" + str(difficulty) + "letter.txt") as file:
    words = file.read().splitlines()
  
word = choice(words)

print("The word is",difficulty,"characters long")
print(Fore.BLUE + "Start by typing a word!")

attempts = 0
while attempts < 6:
  while True:
    attempt = input(Style.RESET_ALL)
    print('\033[1A' + '\033[K', end='')
    if(len(attempt) != int(difficulty)):
      print(Fore.RED + "Word is too long/short!")
      sleep(0.5)
      print('\033[1A' + '\033[K', end='')
    elif(attempt not in words):
      print(Fore.RED + "Not an English word")
      sleep(0.5)
      print('\033[1A' + '\033[K', end='')
    else:
      break
        
  output = ""
  for i in range(len(attempt)):
    if attempt[i] not in word:
      output = output + Style.RESET_ALL + attempt[i] 
    elif attempt[i] == word[i]: output = output + Back.GREEN + attempt[i]
    else: output = output + Back.YELLOW + attempt[i]
  print(output)
  
  if(attempt == word): print(Style.RESET_ALL + Fore.GREEN + "Congrats!"); break
  attempts += 1
print(Style.RESET_ALL + "The word was " + Fore.GREEN + word + Style.RESET_ALL)

del difficulty
del diff
del attempts
del words
del word