# ---------------------------------------------
# Created By : Ben Chu
# Created Date : 09/03/23
# Version = '1.0'
# ---------------------------------------------

# All actions possible for user input
actions = ["heal", "attack", "defend", "quit"]
directions = ["north", "west", "south", "east"]

while True:
    # List out actions in both actions and directions
    print("\n Please choose a following action:\n")
    for action in actions:
        print(f" - {action.capitalize()}")
    print("\n" "Or select a following direction:\n")
    for direc in directions:
        print(f" - {direc.capitalize()}")
    # Check for user input all in lowercase
    choice = input("\n Select an action: ").lower()
    # Checking user input within actions list
    if choice in actions:
        # If input is quit then exit game
        if choice == "quit":
            print("Exiting game")
            break
        # If not and is valid action input then reply with user doing action
        else:
            print("\n" f"You are {choice.capitalize()}ing!")
    # If input isn't in actions list then check for in directions list
    else:
        # If input found in directions then reply with user going in direction
        if choice in directions:
            print("\n" f"Going {choice.capitalize()}!")
        # If input isn't in directions either then reply with invalid
        else:
            print("Invalid action chosen")