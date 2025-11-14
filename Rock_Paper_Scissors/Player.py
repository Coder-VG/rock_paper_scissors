import random
import time

from funcs import *

class Player:
  def __init__(self, player:int, p2IsPlayer:bool):
    self.playerCount:int = player
    self.p2IsPlayer:int = p2IsPlayer
    self.choice = self.getChoice()
      
  def getChoiceNum(self) -> int:
    while True:
      try:
        if self.playerCount == 1:
          if self.p2IsPlayer:  self.choiceNum = int(input("\n\nEnter your choice (Player1): "))
          else:  self.choiceNum = int(input("\n\nEnter your choice: "))
        else:  self.choiceNum = int(input("\nEnter your choice (Player2): "))

        if self.choiceNum<1 or self.choiceNum>3: 
          print("Sorry, please enter a number between 1-3")
          time.sleep(0.5)
          if self.playerCount == 1: clearLastLine(4)
          else: clearLastLine(3)
          continue
        
        if not self.p2IsPlayer:
          time.sleep(0.5)
          clearLastLine()
          return self.choiceNum
        
        if self.playerCount == 1:
          clearLastLine(2)
          print(f'{getColorCode('gray')}--Player{self.playerCount} Choice hidden--{getColorCode()}')
        if self.playerCount == 2:
          clearLastLine(2)
          print(f'{getColorCode('gray')}--Player{self.playerCount} Choice hidden--{getColorCode()}')
          
        return self.choiceNum
      
      except ValueError:
        print("Sorry, please enter a number between 1-3")
        time.sleep(0.5)
        if self.playerCount == 1:  clearLastLine(4)
        else:  clearLastLine(3)
        continue

  def getChoice(self) -> str:
    return {1: 'Rock', 2: 'Paper', 3: 'Scissors'}.get(self.getChoiceNum())
  

class Player1(Player):
  def __init__(self, p2IsP):
    super().__init__(1, p2IsPlayer=p2IsP)

class Player2(Player):
  def __init__(self, p2IsP):
    super().__init__(2, p2IsPlayer=p2IsP)

class Player2_Auto:
  def __init__(self):
    self.choice = self.getChoice()

  def getChoice(self) -> str:
    return random.choice(['Rock', 'Paper', 'Scissors'])
