# ---------------------------------------------
# Title: Castle Dungeon Explorer
# Assignment: RPG Modules
# Class: CS 30
# Date : 21/03/23
# Coders Name:  Ben Chu
# Version:'3.0'
# ---------------------------------------------
'''
Current Assignment: RPG Inventory

This is a simple text based game that contains a small databse of actions 
and rooms that the player can access, 
it has been updated to house a user inventory.
'''
# =============================================================================
# Lists and Dictionaries
# Actions list containing possible actions input by player
actions = ["explore", "search", "inventory", "quit"]
# Items dictionary with the room item can be found in and its description
items = {
  "Courtyard": {
    "item": ["sword"],
    "description": [
      "A gleaming sword you pulled out of stone left untouched" +
      " and exposed to elements for centuries but still razor sharp"
    ],
  },
  "Jail Cells": {
    "item": ["set of shackles"],
    "description": [
      """A set of shackles with not one spot of rust, 
the material is unknown"""
    ],
  },
  "Throne Room": {
    "item": ["crown"],
    "description": [
      """A golden crown found sitting on the throne, 
the crown is studded with gems, the large glowing purple gem 
on the front of the crown catches your attention"""
    ],
  },
  "Lower Dungeons": {
    "item": ["key"],
    "description": [
      """You found a mysterious bronze skeleton key hanging from a wall, 
which door is this for?"""
    ],
  },
  "Guard Hall": {
    "item": ["shield"],
    "description": [
      """This sturdy shield may be useful later on, 
it is lined with the same unbreakable material as the shackles 
and the main body out of a wood as hard as iron"""
    ],
  },
  "Main Hall": {
    "item": ["map"],
    "description": [
      """This map displayed several mysterious caves 
and cliffs with some shadowed area, 
the castle is located in the middle of the map"""
    ],
  },
}
# Rooms list containing possible rooms and directions user can go in
# once in said room
rooms = [
  ["Courtyard", {
    "north": "Main Hall"
  }],
  ["Jail Cells", {
    "east": "Main Hall"
  }],
  ["Throne Room", {
    "south": "Guard Hall",
  }],
  ["Lower Dungeons", {
    "west": "Main Hall"
  }],
  ["Guard Hall", {
    "north": "Throne Room",
    "south": "Main Hall"
  }],
  [
    "Main Hall",
    {
      "north": "Guard Hall",
      "east": "Lower Dungeons",
      "south": "Courtyard",
      "west": "Jail Cells",
    },
  ],
]
# Global variable containging players current location
current_location = "Main Hall"
# Empty list to be filled with items player discover
inventory = []
# =============================================================================
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
  current_room = next((room for room in rooms if room[0] == current_location),
                      None)
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
  Locates items that are under the room name of the current location 
  and adds them to inventory list while 
  also removing them from items dictionary.
  Also prints out item name and description when found
  '''
  global current_location
  global inventory
  if current_location in items:
    found_items = items[current_location]["item"]
    for item in found_items:
      inventory.append(item)
      item_description = items[current_location]["description"][0]
      spacer()
      print(
        f"You've found a {item} within the {current_location.capitalize()}"
      )
      print("-------------------------------")
      print(f"DESCRIPTION: {item_description}")
      spacer()
      print(f"\nThe {item} has been added to your inventory!")
      items.pop(current_location)
  else:
    print("No items found.")
# Loops the game for continuous gameplay
while True:
  print("\n")
  # Displays actions possible by user
  for action in actions:
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
  elif choice in actions:
    print(f"You are now {choice.capitalize()}ing!")
  # For invalid action
  else:
    print("Please select a valid action!")