from funcs import *

def displayRules() -> None:
  print("Winning rules of the game 'ROCK PAPER SCISSORS' are:")
  print("Rock vs Paper -> Paper wins \nPaper vs Scissors -> Scissors wins \nScissors vs Rock -> Rock wins\n")

def displayControls() -> None:
  print("Controls are: \n 1 - Rock \n 2 - Paper \n 3 - Scissors\n", flush=True)

def displayGameModes() -> None:
  print("GameModes are: \n 1 - Play one game \n 2 - Play in tournament\n", flush=True)

def displayWinner(winner, is_bot=False) -> None:
  match winner:
    case 0:
      print(f"{getColorCode('bg')}|== It's a tie! ==|{getColorCode()}", flush=True)
    case 1:
      if is_bot:  print(f'{getColorCode('bg')}|== Player wins! ==|{getColorCode()}', flush=True)
      else:  print(f'{getColorCode('bg')}|== Player1 wins! ==|{getColorCode()}', flush=True)
    case 2:
      if is_bot:  print(f'{getColorCode('bg')}|== Computer wins! ==|{getColorCode()}', flush=True)
      else:  print(f'{getColorCode('bg')}|== Player2 wins! ==|{getColorCode()}', flush=True)
