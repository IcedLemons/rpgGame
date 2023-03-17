# ---------------------------------------------
# Created By : Ben Chu
# Created Date : 15/03/23
# Version = '3.0'
# ---------------------------------------------

actions = ["heal", "attack", "defend", "explore", "quit"]

rooms = {
    "bathroom": {"north": "livingroom"},
    "kitchen": {"east": "livingroom"},
    "closet": {"south": "bedroom"},
    "basement": {"west": "livingroom"},
    "bedroom": {"north": "closet", "south": "livingroom"},
    "livingroom": {"north": "bedroom", "east": "basement", "south": "bathroom", "west": "kitchen"}
}

current_location = "livingroom"

while True:
    print("\n")
  
    for action in actions:
        print(f"- {action.capitalize()}")

    print("\n")
    choice = input("Pick a following action: ").lower()
    print("\n")

    if choice == "quit":
        print("Exiting game!")
        break
      
    elif choice == "explore":
        print("\nSelect a following direction:\n")
        print(f"\nYou're currently in {current_location.capitalize()}\n")    
        for direction in rooms[current_location]:
            print(f"- {direction.capitalize()}")
        print("\n")
        choice_dir = input("Select a direction: ").lower()
        print("\n")
      
        if choice_dir in rooms[current_location]:
            current_location = rooms[current_location][choice_dir]
            print(f"You are now in {current_location.capitalize()}")
        else:
            print("Invalid direction")
          
    elif choice in actions:
        print(f"You are now {choice.capitalize()}ing!")
    else:
        print("Please select a valid action")