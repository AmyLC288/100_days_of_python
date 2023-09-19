#Logo to introduce my game's name
import random
from art import logo
print(logo)


#Function to check number
def check_number(player_guess, number):
  """Function to check player guess against computer number."""
  if player_guess == number:
    return f"You win, the number was {number}."
  elif player_guess > number:
    return "Too high."
  else: 
    return "Too low."


player_lives = 0
game_over = False

#Welcome message printed
print("Welcome to the number guessing game. \nI'm thinking of a number between 1 and 100.")
# Computer choice of number between 1-100
number = random.randint(1, 100)

#Select a difficulty level, easy has 10 lives, hard only has 5.
difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard': ")
if difficulty_level == 'easy':
  player_lives = 10
elif difficulty_level == 'hard':
    player_lives = 5
else: 
  print("Incorrect input.Try again.")
  input("Choose a difficulty level. Type 'easy' or 'hard': ")
  


# While loop to continue checking while the player still has lives left.
while not game_over:
  if player_lives == 1:
    game_over = True
  print(f"You have {player_lives} attempts remaining to guess the number correctly.")
  player_guess = int(input("Make a guess: "))
  if player_guess <1 or player_guess >100:
    print("Choose a number between 1-100 and guess again.")
    player_guess = int(input("Make a guess: "))
  game_active = check_number(player_guess, number)
  print(game_active)
  if game_active == f"You win, the number was {number}.":
    game_over = True
  player_lives -= 1
  if player_lives >1 and game_over == False:
    print("Guess again.")
  
 
if game_over == True and player_lives == 0: 
  print(f"You have no more lives remaining. The number was {number}.")