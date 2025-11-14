import time
from funcs import *

def getResetChoice() -> bool:
  while True:
    rChoice = input("\nDo you want to play again? (Y/N): ").lower()
    
    match rChoice:
      case 'y':
        clearTerminal()
        try:
          main()
        except NotImplementedError:
          print("Sorry, an error occurred.");
          quit()
      case 'n':
        quitProgram()
      case _:
        print("Sorry, please enter (Y/N)")
          
  
def getPlayer2Choice() -> bool:
  while True:
    p2Choice = input("Do you want Player2 to be a Computer? (Y/N): ").lower()

    if p2Choice != 'y' and p2Choice != 'n':  print("Sorry, please enter (Y/N)")
    elif p2Choice == 'y':  return True
    else:  return False

def getTournamentChoice() -> bool:
  while True:
    try:
      tChoice = int(input("\nWhich game mode do you want to play in? (1/2): "))

      if tChoice<1 or tChoice>2: 
        print("Sorry, please enter a number between 1-2")
        time.sleep(0.5)
        clearLastLine(3)
        continue

      if tChoice == 1:  return False
      else:  return True

    except ValueError:
      print("Sorry, please enter a number between 1-2")
      time.sleep(0.5)
      clearLastLine(3)
      continue
