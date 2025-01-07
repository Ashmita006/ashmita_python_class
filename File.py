# To do list using python class and object
INVENTORY_FILE = "inventory.txt"
LEADERBOARD_FILE = "leaderboard.txt"
def save_to_file(filename, data, mode="a"):
    """Save data to a file."""
    with open(filename, mode) as file:
             file.write(data + "\n")

class TodoList:
    def __init__(self):
      self.tasks = []
      
    def add_task(self, task): #create
        self.tasks.append(task)
        print(f"Task '{task}' removed from the list. ")
        
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"task ' {task}' added to the list.")       
        else:
          print(f"Task '{task}' not found in the list.")
    
    def update_task(self, old_task, new_task): 
        if old_task in self.tasks:
            index = self.tasks.index(old_task)
            self.tasks[index] = new_task
            print(f"Task update to '{new_task}'.")
        else:
            print(f"Task '{old_task}' not found in the list.")
            
    def show_tasks(self):
        if self.tasks:
            print("Your Todo List:")
            for index, task in enumerate(self.tasks):
                print("Your Todo List is empty.")
        
todo_list = TodoList()                  
todo_list.add_task("Buy groceries")
todo_list.add_task("Finish the report")
todo_list.add_task("Call mom")

todo_list.show_tasks()
todo_list.remove_task("Finish the report")
todo_list.update_task("Buy groceries", "Go for a walk")
todo_list.show_tasks()

#
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
    
    #
def natural_numbers():
    n = 0
    while True:
        yield n 
        n += 1
gen = natural_numbers() 
for _ in range(10): #Print the first 10 natural numbers
    print(next(gen))

treasures = ["Gold","Silver", "Gem", "Gold"]
upper_treasure = []
for treasure in treasures:
    upper_treasure.append(treasure.upper())
#use a list comprehension   yo capitalize all treasures
capitalized_treasures = [treasure.upper() for treasure in treasures]
print(capitalized_treasures)

#
from collections import Counter
#Sample text
text = """
Python is an amazing programming language. Python is fun to learn and powerful to use.
"""
#Split text into words and count frequency
words = text.lower().split()
word_count = Counter(words)
#Display word frequencies
print("Woed Frequencies:")
for word, count in word_count.items():
    print(f"{word}:{count}")
    
    #
    from queue import Queue
#Create a task queue
task_queue = Queue()
#Add tasks to the queue
tasks = ["Task 1: Clean the room", "Task 2: Write Python code","Task 3: Read a book"]
for task in tasks:
      task_queue.put(task)
#Process tasks
print("Processing Tasks:")
while not task_queue.empty():
    print(task_queue.get())
    
    #
from collections import deque
import random
#Initialize deck of c ards
deck = deque([f"{value} of {suit}" for value in
             ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
             for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]])
#Shuffle the deck
random.shuffle(deck)
#Players and their hands
player1 = []
player2 = []             
#Draw 3 cards for each player
for _ in range(3):
    player1.append(deck.popleft())
    player2.append(deck.popleft())
#Display players' hands
print("Player 1's Hand:")
print(player1)
print("\nPlayer 2's Hand:")
print(player2)

  
                
    
      
    
