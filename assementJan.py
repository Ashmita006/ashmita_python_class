import random
import time
import os

PET_FILE = "pet_status.txt"
LEADERBOARD_FILE = "pet_leaderboard.txt"

def save_to_file(filename, data, mode="a"):
    """Save data to file."""
    with open(filename, mode) as file:
        file.write(data + "\n")

def load_from_file(filename):
    """Load data from a file."""
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return [line.strip() for line in file]

def initialize_pet():
    """Initialize the pet's attributes."""
    print("Welcome to the Virtual Pet Game!")
    pet_name = input("What would you like to name your pet? ").strip()

    if os.path.exists(PET_FILE):
        print("\nResuming your pet's progress...")
        with open(PET_FILE, "r") as file:
            data = file.read().strip().split(',')
            return pet_name, {"hunger": int(data[0]), "happiness": int(data[1]), "energy": int(data[2])}
    else:
        print("\nStarting a new pet adventure...")
        attributes = {"hunger": 50, "happiness": 50, "energy": 50}
        save_pet_status(attributes)
        return pet_name, attributes

def save_pet_status(attributes):
    """Save the pet's attributes to a file."""
    with open(PET_FILE, "w") as file:
        file.write(f"{attributes['hunger']},{attributes['happiness']},{attributes['energy']}")

def display_status(pet_name, attributes):
    """Display the current status of the pet."""
    print(f"\n{pet_name}'s Current Status:")
    for attribute, value in attributes.items():
        print(f"{attribute.capitalize()}: {value}")
    print("")

def feed_pet(attributes):
    """Feed the pet to increase hunger."""
    attributes["hunger"] = min(100, attributes["hunger"] + 10)
    print("You fed your pet. Hunger increased.")

def play_with_pet(attributes):
    """Play with the pet to increase happiness and decrease energy."""
    attributes["happiness"] = min(100, attributes["happiness"] + 10)
    attributes["energy"] = max(0, attributes["energy"] - 10)
    print("You played with your pet. Happiness increased, but energy decreased.")

def rest_pet(attributes):
    """Let the pet rest to increase energy and slightly decrease hunger."""
    attributes["energy"] = min(100, attributes["energy"] + 10)
    attributes["hunger"] = max(0, attributes["hunger"] - 5)
    print("Your pet rested. Energy increased, but hunger decreased slightly.")

def random_event(attributes):
    """Trigger a random event that affects the pet."""
    events = [
        ("Your pet found a toy!", "happiness", 10),
        ("Your pet found some snacks!", "hunger", 10),
        ("Your pet had a bad dream...", "happiness", -10),
        ("Your pet tripped while playing...", "energy", -10)
    ]
    event = random.choice(events)
    print(f"Random Event: {event[0]}")
    attributes[event[1]] = min(100, max(0, attributes[event[1]] + event[2]))

def check_win_condition(attributes, consecutive_turns):
    """Check if the pet meets the win condition."""
    if all(value > 80 for value in attributes.values()):
        consecutive_turns += 1
        if consecutive_turns == 3:
            return True, consecutive_turns
    else:
        consecutive_turns = 0
    return False, consecutive_turns

def check_loss_condition(attributes):
    """Check if the pet meets the loss condition."""
    return any(value == 0 for value in attributes.values())

def update_leaderboard(player_name, score):
    """Update the leaderboard with the player's score."""
    save_to_file(LEADERBOARD_FILE, f"{player_name}: {score}")

def display_leaderboard():
    """Display the leaderboard."""
    leaderboard = load_from_file(LEADERBOARD_FILE)
    if leaderboard:
        print("\nLeaderboard:")
        for entry in leaderboard:
            print(entry)
    else:
        print("\nNo entries in the leaderboard yet.")

def pet_game():
    """Main game function."""
    pet_name, attributes = initialize_pet()
    consecutive_turns = 0
    score = 0

    while True:
        display_status(pet_name, attributes)

        # Check win condition
        won, consecutive_turns = check_win_condition(attributes, consecutive_turns)
        if won:
            print(f"Congratulations! {pet_name} is super happy and energetic. You win!")
            update_leaderboard(pet_name, score)
            break

        # Check loss condition
        if check_loss_condition(attributes):
            print(f"Oh no! {pet_name} got sick. Game over.")
            break

        print("\nWhat would you like to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Rest")
        print("4. Save and Exit")
        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == "1":
            feed_pet(attributes)
            score += 1
        elif choice == "2":
            play_with_pet(attributes)
            score += 1
        elif choice == "3":
            rest_pet(attributes)
            score += 1
        elif choice == "4":
            save_pet_status(attributes)
            print(f"\nThanks for playing! Your progress has been saved.")
            update_leaderboard(pet_name, score)
            break
        else:
            print("Invalid choice. Please try again.")

        # Trigger a random event occasionally
        if random.random() < 0.3:
            random_event(attributes)

def main():
    """Main menu function."""
    while True:
        print("\n== Virtual Pet Game Menu ==")
        print("1. Start/Resume Game")
        print("2. View Leaderboard")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            pet_game()
        elif choice == "2":
            display_leaderboard()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()