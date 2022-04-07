#not done
#borken
import random
import colorama
import os

class cards:
  def __init__(self, suit, value):
    self.suit = suit
    self.value = value

#I love list comprehensions
deck = [cards(suit, value) for value in range(2,14) for suit in ["Diamonds", "Hearts", "Spades", "Clubs"]]


print("Welcome to blackjack")
print("Note: the value of Ace is fixed at 11\n")
print("Your cards:")

while True:
  random.shuffle(deck)

  cards = [deck[0].value, deck[1].value]
  if(sum(cards) < 21):
    for i in range(2):
      if(deck[i].suit in ["Diamonds", "Hearts"]):
        print(str(deck[i].value) + " of " + colorama.Fore.RED + deck[i].suit + colorama.Style.RESET_ALL)
      else:
        print(str(deck[i].value) + " of " + colorama.Style.DIM + deck[i].suit + colorama.Style.RESET_ALL)
      deck.pop(0)
    break
    
print("Total value is", sum(cards), "\n")
#something is wrong i can feel it

while True:
  dealer = [deck[0].value, deck[1].value]
  if(sum(dealer) < 21):
    print("Dealer's deck")
    if(deck[0].suit in ["Diamonds", "Hearts"]):
      print(str(deck[0].value) + " of " + colorama.Fore.RED + deck[0].suit + colorama.Style.RESET_ALL)
    else:
      print(str(deck[0].value) + " of " + colorama.Style.DIM + deck[0].suit + colorama.Style.RESET_ALL)
    print("??? of ???")
    deck.pop(0)
    deck.pop(0)
    break
  random.shuffle(deck)
  
print("Total known value:", dealer[0], "\n")

while sum(dealer) < 17:
  dealer.append(deck[0].value)
  deck.pop(0)

while True:
  option = input("(H)it or (S)tand? ").lower()
  if(option not in ["h", "s"]):
    continue
  
  os.system("clear")
  
  if(option == "h"):
    cards.append(deck[0].value)
    if(deck[0].suit in ["Diamonds", "Hearts"]):
      print(str(deck[0].value) + " of " + colorama.Fore.RED + deck[0].suit + colorama.Style.RESET_ALL)
    else:
      print(str(deck[0].value) + " of " + colorama.Style.DIM + deck[0].suit + colorama.Style.RESET_ALL)
  