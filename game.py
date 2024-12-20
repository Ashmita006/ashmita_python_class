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

#check battries over hundred
def get_charged_batteries():
    batteries = [50, 30, 4, 45, 12, 18, 30] ##battery basket
    minimum_battery_power = 20  #battery 
    usable_battery_power = 0
    usable_battery_count = 0
    for battery in batteries:
       if battery > minimum_battery_power:
           usable_battery_power += battery
           usable_battery_count = usable_battery_count + 1
           if usable_battery_power >= 100:
               return usable_battery_power, usable_battery_count
           
def decrypt_alien_message(alien_message):
    human_mesage = alien_message[::-1] #reserve string
    return human_mesage

def food_dived_equally(foods, crew_member):
    equally_food =  len(foods)// crew_member
    remaining_foods = len(foods) %crew_member
    return equally_food, remaining_foods
    
        
def  alien_attack_game():
    print("Welcome to Alien Attack Game")
    print("Starting mission.......")
    
crews_number, foods = setup_mission()
print(f"You have {crews_number} astronuts aand food avaliable = {foods} ")


print("WELCOME TO THE MARS!!!!!!")
print("Your battery is dead please change the battery")
battery_power, battery_count = get_charged_batteries()

print("Hurray!!!! You battery is charged.")

print("Oops....Alien has arrived saying:")
print("rednerrus")

decrypted_text  = decrypt_alien_message("rednerrus")
print(f"Alien is saying: {decrypted_text}")
print("Alien has captured all astronauts")
print("if astronaut wants to escape they have divide each food and give remaining foods")

equally_divide, remaining_food = food_dived_equally(foods, crews_number)
print(f"You have {equally_divide} foods divided equally and remaning = {remaining_food}")
print("Okay.....Now you can go to Earth")

    
print("Mission Completed")
    
alien_attack_game()


    
    
    
    

