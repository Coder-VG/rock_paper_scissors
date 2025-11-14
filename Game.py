import time

from Player import *
from Display import *

class Game:
  def getWinner(self):
    match self.p1.choice:
      case 'Rock':
        match self.p2.choice:
          case 'Rock': return 0
          case 'Paper': return 2
          case 'Scissors': return 1
      case 'Paper':
        match self.p2.choice:
          case 'Rock': return 1
          case 'Paper': return 0
          case 'Scissors': return 2
      case 'Scissors':
        match self.p2.choice:
          case 'Rock': return 2
          case 'Paper': return 1
          case 'Scissors': return 0
          
  def runGame(self, p2IsP):
    self.p1 = Player1(p2IsP)
    self.p2 = Player2(p2IsP) if (p2IsP) else Player2_Auto()
    self.winner = self.getWinner()
    
  def runGameEnd(self, p2IsP):    
    if p2IsP:
      print("\nPlayer1 choice was: ", end='', flush=True)
      time.sleep(0.5)
      print(f'{getColorCode('g')}{self.p1.choice}{getColorCode()}', flush=True)
      time.sleep(1)

      print("Player2 choice was: ", end='', flush=True)
      time.sleep(0.5)
      print(f'{getColorCode('g')}{self.p2.choice}{getColorCode()}\n', flush=True)
      time.sleep(1)

      displayWinner(self.winner, is_bot=False)
    
    else:
      print("Player choice is: ", end='', flush=True)
      time.sleep(0.5)
      print(f'{getColorCode('g')}{self.p1.choice}{getColorCode()}')
      time.sleep(0.5)

      print("\nNow it's Computer's turn", end='')
      for i in range(3):
        time.sleep(0.5)
        print(".", end='', flush=True)
      time.sleep(1)

      print("\nComputer choice is: ", end='', flush=True)
      time.sleep(0.5)
      print(f'{getColorCode('g')}{self.p2.choice}{getColorCode()}\n')
      time.sleep(1)

      displayWinner(self.winner, is_bot=True)


    def getResetChoice() -> bool:
      while True:
        rChoice = input("\nDo you want to play again? (Y/N): ").lower()
        
        match rChoice:
          case 'y':
            clearTerminal()
            if (not main == None): main()
          case 'n':
            quitProgram()
          case _:
            print("Sorry, please enter (Y/N)")