import os
from beaupy import confirm, prompt, select
from rich.console import Console
import games
import roulette_game
from utils import clear_screen

console = Console()

def get_bet_amount(money_available):
  while True:
    try:
      bet_amount = prompt(f"How much you bet? (1-{money_available})")
      if 0 < int(bet_amount) <= money_available:
        return int(bet_amount)
      else:
        console.print(f"[salmon1]Please provide an amount between 1 and {money_available}![/salmon1]")
    except ValueError:
      console.print("[salmon1]Please provide a number![/salmon1]")

def main():
  clear_screen()
  money = 100
  console.print("[green1]Welcome to our casino![/green1]")
  while True:
    console.print(f"[yellow]You currently have {money} dollars.[/yellow]")
    console.print("[cyan1]Choose a game type:[/cyan1]")
    game_type = select(["Coin flip", "Cho-Han", "Card draw", "Roulette", "[salmon1]Quit[/salmon1]"], cursor="$" if os.name=='nt' else "💸", return_index=True)
    if game_type == 4:
      if confirm("Are you sure you want to quit? All your sweet dollars will be lost."):
        return
    else:
      clear_screen()
      bet_amount = get_bet_amount(money)
      outcome = {
        0: games.coin_flip,
        1: games.cho_han,
        2: games.card_draw,
        3: roulette_game.roulette,
      }.get(game_type)(bet_amount)
      money += outcome
      input("\nPress Enter to continue")
    clear_screen()
    if money <= 0:
      console.print("[salmon1]You lost all your money! You are kicked out of casino![/salmon1]")
      return

main()