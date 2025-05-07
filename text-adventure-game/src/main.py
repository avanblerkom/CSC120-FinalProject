# filepath: /text-adventure-game/text-adventure-game/src/main.py

import sys
import os
import json
from engine.game_state import GameState
from engine.story_engine import StoryEngine

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def load_combined_data():
    """
    Load the combined_data.json file.

    Returns:
        dict: Parsed JSON data from the file, or exits the program if the file is not found.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "data", "combined_data.json")
    try:
        with open(data_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"❌ Error: {data_path} not found.")
        sys.exit(1)

def display_help():
    """
    Display relevant content from the cheatsheet to the user.
    """
    help_text = """
    === Help Menu ===
    How to Play:
    - Navigate through the game by typing the number corresponding to your choice.
    - Solve puzzles by typing your answer.
    - Type 'inventory' to check your inventory.
    - Type 'help' to display this menu.
    - Type 'quit' to exit the game.
    """
    print(help_text)

def display_inventory(game_state):
    """
    Display the player's current inventory.

    Args:
        game_state (GameState): The current game state object.
    """
    inventory = game_state.inventory
    if inventory:
        print("\n=== Inventory ===")
        for item, count in inventory.items():
            print(f"- {item}: {count}")
    else:
        print("\nYour inventory is empty.")

def play_game():
    """
    Main game loop that handles the flow of the game, including loading locations,
    solving puzzles, and managing inventory.
    """
    combined_data = load_combined_data()
    game_state = GameState()
    story_engine = StoryEngine(combined_data)
    current_location = "start"

    while True:
        # Load the current location
        story_engine.load_location(current_location)
        location_data = story_engine.data["locations"][current_location]
        print(f"\n{'='*40}\n{story_engine.get_story_text()}\n{'='*40}")

        # Check if the user has collected 3 sticks and display the message
        if game_state.get_item_count("stick") == 3:
            print("\nYou start to wonder why, given that you are a beaver, you need to solve riddles to get sticks instead of simply chewing and gnawing like everybody else... hmph. You are too sentient for a beaver. Anyways,")

        # Check for a puzzle at the current location
        if "puzzle" in location_data and not game_state.is_puzzle_completed(location_data["puzzle"]["id"]):
            puzzle = location_data["puzzle"]
            print(f"\nPuzzle: {puzzle['description']}")
            while True:
                answer = input("\nYour answer: ").strip().lower()
                if answer in [solution.lower() for solution in puzzle["solution"]]:
                    if puzzle["id"] == 4:  # Special handling for puzzle 4
                        print(f"\n✅ Correct! The answer is {puzzle['solution'][0]}... duh!")
                    else:
                        print("\n✅ Correct! You solved the riddle.")
                    game_state.mark_puzzle_completed(puzzle["id"])
                    if "item" in location_data and location_data["item"] == "stick":
                        game_state.update_inventory("stick")
                        print(f"\n🎉 You received a stick! You now have {game_state.get_item_count('stick')} sticks.")
                    current_location = puzzle["next"]
                    break
                elif answer == "hint":
                    print(f"\nHint: {puzzle['hint']}")
                else:
                    print("\n❌ Incorrect. Try again or type 'hint' to get a hint.")

        # Check for an item at the current location
        if "item" in location_data:
            item = location_data["item"]
            if item == "golden key" and game_state.get_item_count("golden key") == 0:
                game_state.update_inventory("golden key")
                print("\n🎉 You found a golden key and added it to your inventory!")

        # Special handling for the 'build_dam' location
        if current_location == "build_dam":
            required_sticks = 4
            current_sticks = game_state.get_item_count("stick")
            if current_sticks >= required_sticks:
                print("\n🎉 You have enough sticks to build the dam! The dam is complete. You win!")
                current_location = "dam_complete"
            else:
                print(f"\n❌ You need {required_sticks} sticks to complete the dam. You currently have {current_sticks}. Keep exploring!")
                current_location = "start"
            continue

        # Check for special conditions at the current location
        if current_location == "open_chest":
            if game_state.get_item_count("golden key") > 0:
                print("\n🔓 You use the golden key to unlock the chest. Inside, you find a GOLDEN STICK!")
                game_state.update_inventory("golden_stick")
                print("\n🎉 You received a GOLDEN STICK! It has been added to your inventory.")
                current_location = "mountain_peak"
            else:
                print("\n❌ The chest is locked. You need a key to open it.")
                current_location = "mountain_peak"
            continue

        if current_location == "gather_with_sprayoncé":
            print("\n🎉 Sprayoncé helps you gather materials. You receive 1 stick!")
            game_state.update_inventory("stick")
            print(f"\nYou now have {game_state.get_item_count('stick')} sticks.")
            current_location = "build_dam"  # Redirect to build dam location
            continue

        # Display choices
        choices = story_engine.get_choices()
        if choices:
            print("\nWhat would you like to do?")
            for i, choice in enumerate(choices, start=1):
                print(f"  {i}. {choice['text']}")
            user_input = input("\n> ").strip().lower()
            if user_input == "help":
                display_help()
                continue
            elif user_input == "inventory":
                display_inventory(game_state)
                continue
            elif user_input == "quit":
                print("\n👋 Thanks for playing! Goodbye!")
                break
            try:
                choice_index = int(user_input) - 1
                if 0 <= choice_index < len(choices):
                    next_location = choices[choice_index]["next_location"]
                    current_location = next_location  # Update only if valid
                else:
                    print("\nInvalid choice. Please type a number or type 'hint' for other valid commands.")
            except ValueError:
                print("\nInvalid choice. Please type a number or type 'hint' for other valid commands.")
        else:
            print("\nThere are no paths forward. Exiting the game.")
            break

if __name__ == "__main__":
    """
    Entry point for the game. Starts the game loop.
    """
    play_game()