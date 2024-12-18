#fun game
def setup_mission():
    print("setting up for the mission....")
    available_food =[
"apple",
"Cherry",
"banana",
"watermelon",
"chocolate",
"berries",
"pizza",
"water",
]
    available_crews = int(input("Enter available crews"))
    print("Setup Completed......")
    return available_crews, available_food

def  alien_attack_game():
    print("Welcome to Alien Attack Game")
    print("Starting mission.......")

crews_number, foods = setup_mission()
print(f"You have {crews_number} astronuts aand food avaliable = {foods} ")

setup_mission()
print("WELCOME TO THE MARS!!!!!!")
print("Your battery is dead please change the battery")



print("Mission Completed")
    
alien_attack_game()


    
    
    
    

