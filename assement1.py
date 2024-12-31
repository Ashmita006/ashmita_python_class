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



  
                
    
      
    
