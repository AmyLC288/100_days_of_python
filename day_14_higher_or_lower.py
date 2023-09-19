#Import logo, vs, game_data, clear and random
from art import logo, vs
from game_data import data
import random
import os, platform
 
def clear():
   if platform.system() == 'Windows':
      os.system('cls')
   else:
      os.system('clear')


def choose_account():
  """Choose a random account from data list"""
  return random.choice(data)

def clean_data(account):
  """Change data to be formatted how I want it to be"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def compare(guess, follower_count_a, follower_count_b):
  if follower_count_a > follower_count_b:
    return guess == "a"
  else:
    return guess == "b"
  
def play_game():
  print(logo)
  score = 0
  game_over = False
  account_a = choose_account()
  account_b = choose_account()

  while not game_over:
    account_a = account_b
    account_b = choose_account()

    print(f"Compare A: {clean_data(account_a)}.")
    print(vs)
    print(f"Against B: {clean_data(account_b)}.")
    follower_count_a = account_a["follower_count"]
    follower_count_b = account_b["follower_count"]
    guess = input("Who has more followers? Type 'a' or 'b': ")
    is_correct = compare(guess, follower_count_a, follower_count_b)
    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_over == True
      print(f"Sorry that's wrong. Final score: {score}")
      return 
      

play_game()