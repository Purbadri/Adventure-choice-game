def start():
  # give some prompts.
  print("\nYou are standing in a dark road.")
  print("There is a hut to your left and villa to your right, which one do you take? (l or r)")
  
  # convert the player's input() to lower_case
  answer = input(">").lower()

  if "l" in answer:
    # if player typed "left" or "l" lead him to bear_room()
    hut()
  elif "r" in answer:
    # else if player typed "right" or "r" lead him to monster_room()
    villa()
  else:
    # else call game_over() function with the "reason" argument
    game_over("Did you type properly?")
    

# hut
def hut():
  # give some prompts
  # '\n' is to print the line in a new line
  print("\nYou entered the hut.")
  print("It has got two rooms.")
  print("Which room you want to go (1 or 2)")
# take input()
  answer = input(">")
  
  if answer == "1":
    # the player is dead!
    game_over("There is a hidden monster that killed you.")
  elif answer == "2":
    # lead him to the treasure()
    print("\nYayyy you found a treasure")
    treasure()
  else:
    # else call game_over() function with the "reason" argument
    game_over("Did you type properly?")

# villa
def villa():
  # some prompts
  # '\n' is to print the line in a new line
  print("\nNow you entered the villa!")
  print("It has got two rooms. Where do you want to go? (1 or 2)")
  

  # take input()
  answer = input(">")

  if answer == "1":
    # lead him to the treasure()
    treasure()
  elif answer == "2":
    # the player is dead, call game_over() with "reason"
    game_over("There is a monster there he was hungry and ate you.")
  else:
    # game_over() with "reason"
    game_over("Go and learn how to type a number.")

# treasure
def treasure():
  # some prompts
  print("\nYou are now in a room filled with diamonds!")
  print("And there is a door too!")
  print("What would you do? (1 or 2)")
  print("1). Take some diamonds and go through the door.")
  print("2). Just go through the door.")

  # take input()
  answer = input(">")
  
  if answer == "1":
    # the player is dead, call game_over() function with the "reason"
    game_over("They were cursed diamonds! The moment you touched it, the building collapsed, and you die!")
  elif answer == "2":
    # the player won the game
    print("\nNice, you're are an honest man! Congrats you win the game!")
    # activate play_again() function
    play_again()
  else:
    # call game_over() with "reason"
    game_over("Go and learn how to type a number.")

# game_over function accepts an argument called "reason"
def game_over(reason):
  # print the "reason" in a new line (\n)
  print("\n" + reason)
  print("Game Over!")
  # ask player to play again or not by activating play_again() function
  play_again()

# function to ask play again or not
def play_again():
  print("\nDo you want to play again? (y or n)")
  
  # convert the player's input to lower_case
  answer = input(">").lower()

  if "y" in answer:
    # if player typed "yes" or "y" start the game from the beginning
    start()
  else:
    # if user types anything besides "yes" or "y", exit() the program
    exit()
       
    
    # start the game
start()
