# ---------------------------------------------
# Title: Castle Dungeon Explorer
# Assignment: RPG Modules
# Class: CS 30
# Date : 03/04/23
# Coders Name:  Ben Chu
# Version:'4.0'
# ---------------------------------------------
'''
Current Assignment: RPG Inventory

This is a simple text based game that contains a small databse of actions 
and rooms that the player can access, 
it has been updated to house a user inventory.
'''
# =============================================================================
import pickle
import database
# Global variable containging players current location
current_location = "Main Hall"
# Empty list to be filled with items player discover
inventory = []
# =============================================================================
# Write Rooms dictionary into external file
with open('rooms.pickle', 'wb') as handle:
    pickle.dump(database.rooms, handle, protocol=pickle.HIGHEST_PROTOCOL)
# Functions
# Spacer function (for aesthetics)
def spacer():
  print("===============================")
# Movement function
def movement():
  '''
  Displays directions possible by user within the current location
  then moves user into room under the input location the player selected
  '''
  global current_location
  current_room = next((room for room in database.rooms if room[0] == current_location), None)
  if current_room is not None:
    for direction in current_room[1]:
      print(f"- {direction.capitalize()}")
  print("\n")
  choice_direc = input("Select a direction or quit: ").lower()
  print("\n")
  if choice_direc == "quit":
    print("Exiting Game")
    quit()
  input_direction = current_room[1].get(choice_direc)
  if input_direction is not None:
    current_location = input_direction
    print(f"You are now in the {current_location.capitalize()}")
  else:
    print("Please select a valid direction!")
# Search function
def find():
  '''
  Locates items that are under the room name of the current location and 
  adds them to inventory list while also removing them from items dictionary.
  Also prints out item name and description when found
  '''
  global current_location
  global inventory
  if current_location in database.items:
    found_items = database.items[current_location]["item"]
    for item in found_items:
      inventory.append(item)
      item_description = database.items[current_location]["description"][0]
      spacer()
      print(
        f"You've found a {item} within the {current_location.capitalize()}"
      )
      print("-------------------------------")
      print(f"DESCRIPTION: {item_description}")
      spacer()
      print(f"\nThe {item} has been added to your inventory!")
      database.items.pop(current_location)
  else:
    print("No items found.")
# Loops the game for continuous gameplay
try:
  while True:
    print("\n")
    # Displays actions possible by user
    for action in database.actions:
      print(f"- {action.capitalize()}")
    print("\n")
    # Takes input choice
    choice = input("Select a following action: ").lower()
    print("\n")
    # If user input is quit then end game
    if choice == "quit":
      print("Exiting game!")
      break
    # If user input is explore then display current location of player
    # then run movement() function
    elif choice == "explore":
      print("\nSelect a following direction:\n")
      print(f"You're currently in {current_location.capitalize()}\n")
      movement()
    # If input is search then run find() function
    elif choice == "search":
      find()
    # If input is inventory then print out inventory list
    elif choice == "inventory":
      print("Inventory:")
      spacer()
      for inv in inventory:
        print(f"- {inv.capitalize()}")
      spacer()
    # If input is none of the above and is an action within the actions
    # list then pritn out bellow
    elif choice in database.actions:
      print(f"You are now {choice.capitalize()}ing!")
    # For invalid action
    else:
      print("Please select a valid action!")
except Exception as e:
  print("Something went wrong:", e)
