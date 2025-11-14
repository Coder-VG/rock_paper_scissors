import time

from Game import *
from Player import *
from Input import *
from Display import *
from funcs import *

class Tournament(Game):
  def __init__(self):
    self.rounds = self.getRounds()
    self.playerWon = []  # 0 - Tie, 1 - Player1, 2 - Player2
    self.score = [0, 0]
  

  def getRounds(self):
    while True:
      try:
        rounds = int(input("Enter the number of rounds you want to play: "))
        
        if rounds>=2 and rounds<=100:  return rounds
        
        print("Sorry, please enter a number between 2-100")
        time.sleep(0.5)
        clearLastLine(2)
      
      except ValueError:
        print("Sorry, please enter a number between 2-100")
        time.sleep(0.5)
        clearLastLine(2)
        continue
      

  def increaseScore(self, winner):
    match winner:
      case 0:
        self.playerWon.append(0)
      case 1:
        self.score[0] += 1
        self.playerWon.append(1)
      case 2:
        self.score[1] += 1
        self.playerWon.append(2)


  def displayScore(self, p2IsP):
    print("\n┌──────┬────────┐")
    print(  "│ Game │ Player │")
    print(  "├──────┼────────┤")
    
    for i in range(self.rounds):
      print(f"│ {'0'*(3-len(str(i)))}{i+1}  │", end="")
      
      if self.playerWon[i] == 0:
        print(f"  Tie   │")
      
      elif (not p2IsP) and (self.playerWon[i] == 2):  print("Computer│")
      else:  print(f"   {self.playerWon[i]}  │")
      
    print("└──────┴────────┘\n")
  

  def run(self, p2IsP):     
    for i in range(self.rounds):
      print(f'\n{self.score[0]} | {self.score[1]}')
      print(f'Round {i+1}')   
      
      self.runGame(p2IsP)  
      self.runGameEnd(p2IsP)
      self.increaseScore(self.winner)        
      
      time.sleep(2)
      clearLastLine(11)
      
    time.sleep(0.5)  
      
    self.displayScore(p2IsP)
    
    displayWinner(self.winner, not p2IsP)
    time.sleep(1)
    getResetChoice()

class OneGame(Game):   
  def run(self, p2IsP):
    self.runGame(p2IsP)
    self.runGameEnd(p2IsP)
          
    time.sleep(1)
    getResetChoice()