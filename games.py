import utils
import random
import os
from time import sleep
from beaupy import select, prompt
from rich.console import Console

console = Console()

def coin_flip(bet_amount):
  bet = make_bet(["Heads", "Tails"])
  console.print(f"Your bet: {bet}")
  console.print(f"Bet amount: {bet_amount}")
  spinner = utils.create_spinner("🌕", "O", "Flipping coin...")
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
  spinner = utils.create_spinner("🎲", "■", "Rolling dices...")
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
  options = list(range(1, 11))
  console.print(f"Bet amount: {bet_amount}")
  spinner = utils.create_spinner("🃏", "O", "Drawing cards...")
  spinner.start()
  sleep(5)
  player_card = options.pop(random.randint(0, len(options)-1))
  opponent_card = options.pop(random.randint(0, len(options)-1))
  spinner.stop()
  console.print(f"You drew {player_card}.")
  console.print(f"Your opponent drew {opponent_card}.")
  if (player_card > opponent_card):
    console.print(f"[green1]You earned {bet_amount} dollars![/green1]")
    return bet_amount
  else:
    console.print(f"[salmon1]You lost {bet_amount} dollars![/salmon1]")
    return -(bet_amount)

def make_bet(options):
  console.print("Your bet:")
  bet = select(options, cursor="$" if os.name=="nt" else "💰")
  utils.clear_screen()
  return bet