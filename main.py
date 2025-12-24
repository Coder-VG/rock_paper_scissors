import time

from Game import *
from GameModes import *
from Player import *
from Input import *
from Display import *
from Funcs import *


def main() -> None:

  displayRules()
  time.sleep(1)

  displayControls()
  time.sleep(1)

  displayGameModes()
  time.sleep(1)
  
  print()

  p2IsPlayer = not getPlayer2Choice()
  tournamentChoice = getTournamentChoice()
  
  game = Tournament() if (tournamentChoice) else OneGame()
  game.run(p2IsPlayer)
    

if __name__ == '__main__':
  main()
