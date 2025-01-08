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

#
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print("1 D array", arr)
print(type(arr))
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#Orderedlist
from collections import OrderedDict
class GroceryList:
    def __init__(self):
        self.grocery_list = OrderedDict()

    def add_item(self, item, quantity=1):
        """Add an item to the list with a specified quantity."""
        if item in self.grocery_list:
            self.grocery_list[item] += quantity
        else:
            self.grocery_list[item] = quantity

    def remove_item(self, item):
        """Remove an item from the list."""
        if item in self.grocery_list:
            del self.grocery_list[item]
        else:
            print(f"Item '{item}' not found in the list.")

    def update_quantity(self, item, quantity):
        """Update the quantity of an item."""
        if item in self.grocery_list:
            self.grocery_list[item] = quantity
        else:
            print(f"Item '{item}' not found in the list.")

    def show_list(self):
        """Display the grocery list."""
        print("\nGrocery List:")
        for item, quantity in self.grocery_list.items():
            print(f" - {item}: {quantity}")

    def clear_list(self):
        """Clear the entire list."""
        self.grocery_list.clear()
        print("Grocery list cleared.")

if __name__ == "__main__":
    gl = GroceryList()
    gl.add_item("Apples", 4)
    gl.add_item("Bread", 2)
    gl.add_item("Milk", 1)
    gl.add_item("Apples", 2) 
    gl.show_list()

    gl.update_quantity("Bread", 1)
    gl.remove_item("Milk")
    gl.show_list()
    gl.clear_list()

    #1
import csv
# File path for the sales tracker
file_path = "sales_tracker.csv"
# Create a new CSV file with headers
def create_csv():
    headers = ["Date", "Product", "Quantity", "Price per unit", "Total"]
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
    print("Sales tracker created.")

# Add a new sale record to the CSV file
def add_sale(date, product, quantity, price_per_unit):
    total = quantity * price_per_unit
    with open(file_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, product, quantity, price_per_unit, total])
    print("Sale record added.")

# Calculate total sales from the CSV file
def calculate_total_sales():
    total_sales = 0
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_sales += float(row["Total"])
    print(f"Total Sales: ${total_sales:.2f}")

# Example usage
create_csv()
add_sale("2025-01-08", "Laptop", 2, 1200.50)
add_sale("2025-01-09", "Mouse", 5, 25.99)
calculate_total_sales()

#2
import csv
import numpy as np
# File path for input CSV
file_path = "sales_tracker.csv"
# Load data into a structured NumPy array
def load_data(file_path):
    data = []
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            product = row["Product"]
            revenue = float(row["Total"])
            region = row.get("Region", "Unknown")  
            data.append((product, revenue, region))
    return np.array(data, dtype=[("Product", "U50"), ("Revenue", "f8"), ("Region", "U50")])
# Calculate metrics using NumPy
def calculate_metrics(data):
    # Average revenue for all products
    avg_revenue = np.mean(data["Revenue"])
    # Find the product with the highest revenue
    max_revenue_index = np.argmax(data["Revenue"])
    highest_revenue_product = data[max_revenue_index]
    # Total revenue by region
    unique_regions = np.unique(data["Region"])
    revenue_by_region = {region: np.sum(data["Revenue"][data["Region"] == region]) for region in unique_regions}
    return avg_revenue, highest_revenue_product, revenue_by_region
# Main function to load data, calculate metrics, and display results
def main():
    try:
        # Load data
        data = load_data(file_path)
        # Calculate metrics
        avg_revenue, highest_revenue_product, revenue_by_region = calculate_metrics(data)
        # Display results
        print(f"Average Revenue for All Products: ${avg_revenue:.2f}")
        print(f"Product with Highest Revenue: {highest_revenue_product['Product']} (${highest_revenue_product['Revenue']:.2f})")
        print("Total Revenue by Region:")
        for region, revenue in revenue_by_region.items():
            print(f"  {region}: ${revenue:.2f}")
    except FileNotFoundError:
        print("Error: The input CSV file was not found.")
    except KeyError as e:
        print(f"Error: Missing expected column: {e}")
if __name__ == "__main__":
    main()

#3
import csv
import numpy as np

# File paths
input_file_path = "sales_tracker.csv"
output_file_path = "sales_summary.csv"

# Function to calculate metrics and write results to a new CSV file
def calculate_and_write_summary():
    try:
        # Load data from the CSV file
        data = []
        with open(input_file_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                product = row["Product"]
                region = row.get("Region", "Unknown")  # Default region if not present
                revenue = float(row["Total"])
                data.append((product, revenue, region))
        
        # Convert data to a structured NumPy array
        structured_data = np.array(data, dtype=[("Product", "U50"), ("Revenue", "f8"), ("Region", "U50")])
        
        # Calculate total revenue for each product
        unique_products = np.unique(structured_data["Product"])
        product_revenue = {product: np.sum(structured_data["Revenue"][structured_data["Product"] == product]) for product in unique_products}
        
        # Calculate the product with the highest revenue
        max_revenue_index = np.argmax(structured_data["Revenue"])
        highest_revenue_product = structured_data[max_revenue_index]
        
        # Calculate total revenue by region
        unique_regions = np.unique(structured_data["Region"])
        revenue_by_region = {region: np.sum(structured_data["Revenue"][structured_data["Region"] == region]) for region in unique_regions}
        
        # Write results to a new CSV file
        with open(output_file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Product", "Total Revenue", "Region"])
            for product, revenue in product_revenue.items():
                for region in unique_regions:
                    region_revenue = np.sum(
                        structured_data["Revenue"][
                            (structured_data["Product"] == product) & (structured_data["Region"] == region)
                        ]
                    )
                    if region_revenue > 0:  # Include only if revenue exists for this region
                        writer.writerow([product, region_revenue, region])
        
        print("Summary written to", output_file_path)
        print(f"Product with the Highest Revenue: {highest_revenue_product['Product']} (${highest_revenue_product['Revenue']:.2f})")
        print("Revenue by Region:", revenue_by_region)
    
    except FileNotFoundError:
        print("Error: Input file not found.")
    except KeyError as e:
        print(f"Error: Missing expected column in input file - {e}")
# Example Usage
if __name__ == "__main__":
    calculate_and_write_summary()


  
                
    
      
    
