import os
from beaupy.spinners import *

def create_spinner(spinner_char, spinner_char_windows, spinner_text):
  spinner_char = spinner_char_windows if os.name=="nt" else spinner_char
  spinner_animation = [f"{spinner_char}    \n      ", f"  {spinner_char}  \n      ", f"    {spinner_char}\n      ", f"      \n    {spinner_char}", f"      \n  {spinner_char}  ", f"      \n{spinner_char}    "]
  spinner = Spinner(spinner_animation, spinner_text)
  return spinner

def clear_screen():
  os.system('cls' if os.name=='nt' else 'clear')