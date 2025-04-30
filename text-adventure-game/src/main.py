# filepath: /text-adventure-game/text-adventure-game/src/main.py

import sys
import os
import json
from engine.game_state import GameState
from engine.story_engine import StoryEngine

# Fix typo in sys.path.append
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def load_combined_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "data", "combined_data.json")
    try:
        with open(data_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"❌ Error: {data_path} not found.")
        sys.exit(1)

def play_game():
    combined_data = load_combined_data()
    game_state = GameState()
    story_engine = StoryEngine(combined_data)
    current_location = "start"

    while True:
        # Load the current location
        story_engine.load_location(current_location)
        location_data = story_engine.data["locations"][current_location]
        print(f"\n{'='*40}\n{story_engine.get_story_text()}\n{'='*40}")

        # Special handling for the 'build_dam_start' location
        if current_location == "build_dam_start":
            required_sticks = 3
            if game_state.get_item_count("stick") >= required_sticks:
                print("\n🎉 You have enough sticks to build the dam! The dam is complete. You win!")
                current_location = "dam_complete"
                continue
            else:
                print(f"\n❌ You don't have enough sticks to build the dam. You currently have {game_state.get_item_count('stick')} stick(s).")
                current_location = "start"
                continue

        # Check for a puzzle at the current location
        if "puzzle" in location_data and not game_state.is_puzzle_completed(location_data["puzzle"]["id"]):
            puzzle = location_data["puzzle"]
            print(f"\nPuzzle: {puzzle['description']}")
            print(f"Hint: {puzzle['hint']}")
            while True:
                answer = input("\nYour answer: ").strip().lower()
                if answer in [solution.lower() for solution in puzzle["solution"]]:
                    print("\n✅ Correct! You solved the puzzle.")
                    game_state.mark_puzzle_completed(puzzle["id"])
                    if "item" in location_data and location_data["item"] == "stick":
                        game_state.update_inventory("stick")
                        print(f"\n🎉 You received a stick! You now have {game_state.get_item_count('stick')} stick(s).")
                    current_location = puzzle["next"]
                    break
                else:
                    print("\n❌ Incorrect. Try again or type 'skip' to skip the puzzle.")
                    if answer.lower() == "skip":
                        print("\nSkipping the puzzle...")
                        break

        # Special handling for the 'build_dam' location
        if current_location == "build_dam":
            required_sticks = 3
            if game_state.get_item_count("stick") < required_sticks:
                print(f"\n❌ You need at least {required_sticks} sticks to complete the dam. Keep exploring!")
                current_location = "gather_materials"
                continue

        # Display choices
        choices = story_engine.get_choices()
        if choices:
            print("\nWhat would you like to do?")
            for i, choice in enumerate(choices, start=1):
                print(f"  {i}. {choice['text']}")
            try:
                choice_index = int(input("\n> ")) - 1
                if 0 <= choice_index < len(choices):
                    next_location = choices[choice_index]["next_location"]
                    # Check if the choice requires items
                    if "required_item" in choices[choice_index]:
                        required_item = choices[choice_index]["required_item"]
                        if game_state.get_item_count(required_item) < required_sticks:
                            print(f"\n❌ You don't have enough {required_item}s to proceed.")
                            continue
                        game_state.remove_from_inventory(required_item, required_sticks)
                    current_location = next_location
                else:
                    print("\n❌ Invalid choice. Try again.")
            except ValueError:
                print("\n❌ Please enter a number.")
        else:
            print("\nThere are no paths forward. Exiting the game.")
            break

if __name__ == "__main__":
    play_game()