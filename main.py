import random
import sys
import os
from time import sleep
from beaupy import confirm, prompt, select
from beaupy.spinners import *
from rich.console import Console

console = Console()

def coin_flip(bet_amount):
  bet = make_bet(["Heads", "Tails"])
  console.print(f"Your bet: {bet}")
  console.print(f"Bet amount: {bet_amount}")
  spinner = create_spinner("🪙", "O", "Flipping coin...")
  spinner.start()
  sleep(5)
  result = random.choice(["Heads", "Tails"])
  spinner.stop()
  console.print(f"The outcome is: {result}")
  if bet == result:
    console.print(f"[green1]You earned {bet_amount} dollars![/green1]")
    return bet_amount
  else:
    console.print(f"[salmon1]You lost {bet_amount} dollars![/salmon1]")
    return -(bet_amount)

def cho_han(bet_amount):
  bet = make_bet(["Even", "Odd"])
  console.print(f"Your bet: {bet}")
  console.print(f"Bet amount: {bet_amount}")
  spinner = create_spinner("🎲", "■", "Rolling dices...")
  spinner.start()
  sleep(5)
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  result = dice1 + dice2
  spinner.stop()
  console.print(f"The outcome is: {dice1} + {dice2} = {result}")
  if (result % 2 == 0 and bet == "Even") or (result % 2 == 1 and bet == "Odd"):
    console.print(f"[green1]You earned {bet_amount} dollars![/green1]")
    return bet_amount
  else:
    console.print(f"[salmon1]You lost {bet_amount} dollars![/salmon1]")
    return -(bet_amount)

def card_draw(bet_amount):
  pass

def roulette(bet_amount):
  pass

def make_bet(options):
  console.print("Your bet:")
  bet = select(options, cursor="$" if os.name=="nt" else "💰")
  clear_screen()
  return bet

def create_spinner(spinner_char, spinner_char_windows, spinner_text):
  spinner_char = spinner_char_windows if os.name=="nt" else spinner_char
  spinner_animation = [f"{spinner_char}    \n      ", f"  {spinner_char}  \n      ", f"    {spinner_char}\n      ", f"      \n    {spinner_char}", f"      \n  {spinner_char}  ", f"      \n{spinner_char}    "]
  spinner = Spinner(spinner_animation, spinner_text)
  return spinner

def get_bet_amount(money_available):
  while True:
    try:
      bet_amount = prompt("How much you bet?")
      if 0 < int(bet_amount) <= money_available:
        return int(bet_amount)
      else:
        console.print(f"[salmon1]Please provide an amount between 1 and {money_available}![/salmon1]")
    except ValueError:
      console.print("[salmon1]Please provide a number![/salmon1]")

def clear_screen():
  os.system('cls' if os.name=='nt' else 'clear')

def main():
  clear_screen()
  money = 100
  console.print("[green1]Welcome![/green1]")
  while True:
    console.print(f"[yellow]You currently have {money} dollars.[/yellow]")
    console.print("[cyan1]Choose a game type:[/cyan1]")
    game_type = select(["Coin flip", "Cho-Han", "Card draw", "Roulette", "[salmon1]Quit[/salmon1]"], cursor="$" if os.name=='nt' else "💸", return_index=True)
    if game_type == 4:
      if confirm("Are you sure you want to quit? All your sweet dollars will be lost."):
        sys.exit()
    else:
      clear_screen()
      print(game_type)
      bet_amount = get_bet_amount(money)
      outcome = {
        0: coin_flip,
        1: cho_han,
        2: card_draw,
        3: roulette,
      }.get(game_type)(bet_amount)
      money += outcome
      input("\nPress Enter to continue")
    clear_screen()

main()