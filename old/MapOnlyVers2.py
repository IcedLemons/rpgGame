# ---------------------------------------------
# Title: RPG map                                                              
# Class: CS 30                                                              
# Date : 21/03/23                                                                 
# Coders Name:  Ben Chu                                                       
# Version:'2.0'
# ---------------------------------------------
'''
Current Assignment: RPG Map

This is a simple text based game that contains a small databse of actions and rooms that the player can access
'''
# Actions List, contains all possible actions by users
actions = ["heal", "attack", "defend", "explore", "quit"]
# Rooms list, contains all rooms accessible
# Also contains the possible directions users can go once in said room
rooms = [
    ["courtyard", {"north": "Main Hall"}],
    ["jail cells", {"east": "Main Hall"}],
    ["throne room", {"south": "guard Hall"}],
    ["lower Dungeons", {"west": "Main Hall"}],
    ["guard Hall", {"north": "throne room", "south": "Main Hall"}],
    [
        "Main Hall",
        {
            "north": "guard Hall",
            "east": "lower Dungeons",
            "south": "courtyard",
            "west": "jail cells",
        },
    ],
]
# Sets the starting location for player
current_location = "Main Hall"
# Movement Function
def movement():
  global current_location
  current_room = next(
  (room for room in rooms if room[0] == current_location), None)
  if current_room is not None:
      # Prints out list of possible directions within the current room player is in
      for direction in current_room[1]:
          print(f"- {direction.capitalize()}")
  else:
      print("Invalid room")
  # Checks user input within all possible directions (current_room)...? in lowercase
  print("\n")
  choice_direc = input("Select a direction: ").lower()
  print("\n")
  # If a valid direction is chosen then it runs the following
  # The users direction is checked with a corresponding room within the rooms list
  # possible within their current room
  input_direction = next(
      (direction for direction in current_room[1] if direction == choice_direc),
      None,
  )
  if input_direction is not None:
      # Prints out the players location after they select a direction to go in
      current_location = current_room[1][input_direction]
      print(f"You are now in {current_location.capitalize()}")


while True:
    print("\n")
    # Prints out the actions list
    for action in actions:
        print(f"- {action.capitalize()}")
    # Checks user inout all in lowercase
    print("\n")
    choice = input("Select a following action: ").lower()
    print("\n")
    # If user input is quit then it exits the game
    if choice == "quit":
        print("Exiting game!")
        break
    # If not quit and is explored then prints out directions list within the rooms list
    elif choice == "explore":
        print("\nSelect a following direction:\n")
        # Prints out current location of player
        print(f"\nYou're currently in {current_location.capitalize()}\n")
        
        movement()
    # If player input is neither quit nor explore and is a valid action
    # then prints out user enacting the action
    elif choice in actions:
        print(f"You are now {choice.capitalize()}ing!")
    # Error message if user input isn't in actions list
    else:
        print("Please select a valid action!")