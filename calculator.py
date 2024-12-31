first_number   = int (input("Enter your first number:"))
second_number = int (input("Enter your second number:"))
       # first_number = int(first_number)
user_choice = input(""")
                           Please choose you option
                           + for Addition 
                           - for Substraction
                           * for Multiply
                           / for Dividez
                           """)
if user_choice == "+":
              print("Addition = ", first_number + second_number)
elif user_choice == "-":
              print("Substraction = ", first_number - second_number)
else:
       print("Invalid option")

first_number = float(input("Enter the first number:"))
second_number = float(input("Enter the second number:"))
print("Substraction =", first_number - second_number)

first_number = float(input("Enter the first number:"))
second_number = float(input("Enter the second number:"))
print("Multiply =", first_number * second_number)

first_number = float(input("Enter the first number:"))
second_number = float(input("Enter the second number:"))
print("Divide =", first_number / second_number)

import random
import os
import time

INVENTORY_FILE = "inventory.txt"
LEADERBOARD_FILE = "leaderboard.txt"

def save_to_file(filename, data, mode="a"):
    """Save data to a file."""
    with open(filename, mode) as file:
             file.write(data + "\n")
             
def explore_location():
    """Explore a random location and find treasures."""
    location = ["Mysterious Cane", "Haunted Forest", "Deserted Beach", "Ancient Rusins"]
    treasures = ["Golden Crown", "Sliver Sword", "Diamond Necklace", "Ancient Artifact"]
    
    location = random.choice(location)
    treasures = random.choice(treasures)
    
    print(f"\nExploring {location}....")
    time.sleep(2)
    print(f"You found a {treasures}!")
    
    save_to_file(INVENTORY_FILE, treasures)
    return treasures

def load_from_file(filename):
    """Load data from a file."""
    if not os.path.exist(filename):
        return[]
    with open(filename, "r") as file:
            return[line.strip() for line in file]   
        
def display_inventory():
    """Display the leaderboard."""
    leaderboard = load_from_file(LEADERBOARD_FILE)
    if leaderboard:
        print("\nLeaderboard:")
        for entry in leaderboard:
            print(entry)
    else:
        print("\nNo entries in the leaderboard yet.")
        
def update_leaderboard(player_name, score):
    """Updata the leaderboard."""
    save_to_file(LEADERBOARD_FILE, f"{player_name}: {score}")
    
def treasure_hunt():
       print("Welcome to Treasure Humt!")
       player_mame = input("Enter your name: ").strip
       
        #Load inventory if it exists
       if os.path.exists(INVENTORY_FILE):
           print("\nREsuming your adventure...")
       else:
           print("\n starting a new adventure...")
           open(INVENTORY_FILE, "w").close() #create an empty inventory file
           
       score = 0   
       
       while True:
           print("\nWhat would you like to do?")
           print("1. Explore a new location")
           print("2. View Leaderboard")
           print("3. Quit and save progress")
           choice = input("Enter your choice (1/2/3): ").strip()
           
           if choice == "1":
               treasure = explore_location()
               score += 1
               print(f"You added {treasure} to your inventory!")
           elif choice == "2":
               display_inventory()
def dispaly_leaderboard():
    """Display the leaderboard."""
    leaaderboard = load_from_file(LEADERBOARD_FILE)
    if leaaderboard:
        print("\nLeaderboard:")
        for entry in leaaderboard:
            print(entry)
    else:
        print("\nNo entries in the ledaerboard yet:")
                
def view_leaderboard():
      print("\n== Leaderboard ==")
      dispaly_leaderboard()
      
def main():
     while True:
         print("\n== Treasure Hunt Menu == ")
         print("1. Start/Resume Game")
         print("2. View Leaderboard")
         print("3. Exit")
         choice = input("Enter your choice (1/2/3): ").strip()
         
         if choice == "1":
             treasure_hunt()       
         elif choice == "2":
             view_leaderboard()
         elif choice == "3":
               print("Goodbye!")
         else:
             print("Invalid Choice.Please try again. ")
           
if  __name__ =="__main__":
    main()
    
