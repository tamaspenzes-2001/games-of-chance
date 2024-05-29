import random
import sys
from beaupy import confirm, prompt, select
from beaupy.spinners import *
from rich.console import Console

console = Console()

def coin_flip():
  pass

def cho_han():
  pass

def card_draw():
  pass

def roulette():
  pass

def main():
  console.print("Welcome!")
  money = 100
  while True:
    console.print(f"[yellow]You currently have {money} dollars.[/yellow]")
    console.print("[cyan1]Choose a game type:[/cyan1]")
    game_type = select(["Coin flip", "Cho-Han", "Card draw", "Roulette", "[red1]Quit[/red1]"], cursor="💸", return_index=True)
    outcome = {
      0: coin_flip(),
      1: cho_han(),
      2: card_draw(),
      3: roulette(),
    }.get(game_type)
    if outcome is None:
      if confirm("Are you sure you want to quit? All your sweet dollars will be lost."):
        sys.exit()
    else:
      money += outcome

main()