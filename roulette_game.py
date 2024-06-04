import utils
import random
import os
from time import sleep
from beaupy import select, prompt
from rich.console import Console

console = Console()

def roulette(bet_amount):
  bet, multiplier = make_roulette_bet()
  utils.clear_screen()
  console.print(f"Your bet: {bet}")
  console.print(f"Bet amount: {bet_amount}")
  spinner = utils.create_spinner("🏐", "O", "Throwing ball...")
  spinner.start()
  sleep(5)
  fields = list(range(37)) + ["00"]
  result = random.choice(fields)
  spinner.stop()
  console.print(f"The outcome is: {result}")
  multiplied_bet_amount = bet_amount * multiplier
  if result in bet:
    console.print(f"[green1]You earned {bet_amount} * {multiplier} = {multiplied_bet_amount} dollars![/green1]")
    return multiplied_bet_amount
  else:
    console.print(f"[salmon1]You lost {bet_amount} * {multiplier} = {multiplied_bet_amount} dollars![/salmon1]")
    return -(multiplied_bet_amount)

def make_roulette_bet():
  console.print("[cyan1]Choose a bet type:[/cyan1]")
  bet_categories = ["Inside (higher payout, lower winrate)", "Outside (lower payout, higher winrate)"]
  chosen_category = select(bet_categories, cursor="$" if os.name=="nt" else "💰")
  match chosen_category:
    case "Inside (higher payout, lower winrate)": return make_inside_bet()
    case "Outside (lower payout, higher winrate)": return make_outside_bet()

def make_inside_bet():
  bet_types = ["0 - 35x", "00 - 35x", "Straight up (one number) - 35x", "Row (0, 00) - 17x", "Split vertical (2 adjacent numbers) - 17x", "Split horizontal (2 adjacent numbers) - 17x", "Street (3 numbers in horizontal line) - 11x", "Corner (4 numbers square shape) - 8x", "Top line (0, 00, 1, 2, 3) - 8x", "Double street (6 numbers in 2 horizontal lines) - 5x"]
  chosen_type = select(bet_types, cursor="$" if os.name=="nt" else "💰")
  match chosen_type:
    case "0 - 35x": return [0], 35
    case "00 - 35x": return ["00"], 35
    case "Straight up (one number) - 35x": return [make_number_bet(1, 36)], 35
    case "Row (0, 00) - 17x": return [0, "00"], 17
    case "Split vertical (2 adjacent numbers) - 17x":
      chosen_number = make_number_bet(1, 33)
      return [chosen_number, chosen_number+3], 17
    case "Split horizontal (2 adjacent numbers) - 17x":
      chosen_number = make_number_bet(1, 36, condition=lambda x: x % 3 != 0, condition_text="from the first or second column (1, 2, 4, 5, 7, 8 etc.)")
      return [chosen_number, chosen_number+1], 17
    case "Street (3 numbers in horizontal line) - 11x":
      chosen_number = make_number_bet(1, 36, condition=lambda x: (x - 1) % 3 == 0, condition_text="from the first column (1, 4, 7 etc.)")
      return [chosen_number+i for i in range(3)], 11
    case "Corner (4 numbers square shape) - 8x":
      chosen_number = make_number_bet(1, 32, condition=lambda x: x % 3 != 0, condition_text="from the first or second column (1, 2, 4, 5, 7, 8 etc.)")
      return [chosen_number, chosen_number+1, chosen_number+3, chosen_number+4], 8
    case "Top line (0, 00, 1, 2, 3) - 8x": return [0, "00", 1, 2, 3], 8
    case "Double street (6 numbers in 2 horizontal lines) - 5x":
      chosen_number = make_number_bet(1, 31, condition=lambda x: (x - 1) % 3 == 0, condition_text="from the first column (1, 4, 7 etc.)")
      return [chosen_number+i for i in range(6)], 5

def make_outside_bet():
  bet_types = ["Column - 2x", "Dozen - 2x", "Snake (1, 5, 9, 12, 14, 16, 19, 23, 27, 30, 32, 34) - 2x", "Odd - 1x", "Even - 1x", "Red - 1x", "Black - 1x", "Low (1 to 18) - 1x", "High (19 to 36) - 1x"]
  chosen_type = select(bet_types, cursor="$" if os.name=="nt" else "💰")
  match chosen_type:
    case "Column - 2x":
      column_bets = ["1st column - 2x", "2nd column - 2x", "3rd column - 2x"]
      chosen_column = select(column_bets, cursor="$" if os.name=="nt" else "💰", return_index=True)
      return [num for num in range(chosen_column+1, 37, 3)], 2
    case "Dozen - 2x":
      dozen_bets = ["1st dozen - 2x", "2nd dozen - 2x", "3rd dozen - 2x"]
      chosen_dozen = select(dozen_bets, cursor="$" if os.name=="nt" else "💰", return_index=True)
      match chosen_dozen:
        case 0: return [num for num in range(1, 13)], 2
        case 1: return [num for num in range(13, 25)], 2
        case 2: return [num for num in range(25, 37)], 2
    case "Snake (1, 5, 9, 12, 14, 16, 19, 23, 27, 30, 32, 34) - 2x":
      return [1, 5, 9, 12, 14, 16, 19, 23, 27, 30, 32, 34], 2
    case "Odd - 1x": return [num for num in range(1, 37) if num % 2 != 0], 1
    case "Even - 1x": return [num for num in range(1, 37) if num % 2 == 0], 1
    case "Red - 1x": return [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36], 1
    case "Black - 1x": return [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35], 1
    case "Low (1 to 18) - 1x": return [num for num in range(1, 19)], 1
    case "High (19 to 36) - 1x": return [num for num in range(19, 37)], 1

def make_number_bet(min_value, max_value, condition=lambda x: True, condition_text=""):
  while True:
    try:
      chosen_number = prompt(f"Write a number between {min_value} and {max_value} {condition_text}")
      if min_value <= int(chosen_number) <= max_value:
        if condition(int(chosen_number)):
          return int(chosen_number)
        else:
          console.print(f"[salmon1]Please provide a number {condition_text}![/salmon1]")
      else:
        console.print(f"[salmon1]Please provide a number between {min_value} and {max_value}![/salmon1]")
    except ValueError:
      console.print("[salmon1]Please provide a number![/salmon1]")