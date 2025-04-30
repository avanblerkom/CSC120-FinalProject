# filepath: /text-adventure-game/text-adventure-game/src/main.py

import json
import sys
import os
import string  # Add this import for punctuation removal

# Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.engine.game_state import GameState
from src.engine.story_engine import StoryEngine

def load_map():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    map_path = os.path.join(base_dir, "data", "map.json")
    with open(map_path, "r") as file:
        return json.load(file)

def load_story_scripts():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    story_path = os.path.join(base_dir, "data", "story_scripts.json")
    with open(story_path, "r") as file:
        return {script["id"]: script for script in json.load(file)["scripts"]}

def play_game():
    game_map = load_map()
    story_scripts = load_story_scripts()
    game_state = GameState()
    story_engine = StoryEngine(story_scripts, game_map)  # Initialize StoryEngine
    current_story_id = "intro"  # Start with the intro story

    while True:
        # Get the current story data
        story = story_scripts.get(current_story_id, {})
        if not story:
            print(f"DEBUG: Story ID '{current_story_id}' not found. Returning to the previous story.")
            continue  # Loop back to the current story

        print(story.get("text", "No story available for this location."))

        # Handle item rewards
        if "item" in story:
            game_state.update_inventory(story["item"])
            if story["item"] == "stick":
                print(f"You now have {game_state.get_item_count('stick')} stick(s).")

        # Handle puzzles
        if "puzzle_id" in story:
            puzzle_id = story["puzzle_id"]
            if game_state.is_puzzle_completed(puzzle_id):
                print("You have already solved this puzzle. Moving on...")
                current_story_id = story.get("next", current_story_id)
                continue

            puzzle = story_engine.puzzles.get(puzzle_id)
            if not puzzle:
                print(f"DEBUG: Puzzle ID '{puzzle_id}' not found. Skipping puzzle.")
                current_story_id = story.get("next", current_story_id)
                continue

            print(puzzle["description"])
            while True:
                user_solution = input("Your answer: ").strip().lower().translate(str.maketrans('', '', string.punctuation))
                if story_engine.solve_puzzle(puzzle_id, user_solution):
                    print("Correct! You may proceed.")
                    game_state.update_inventory("stick")
                    print("A magical stick has appeared!")
                    print(f"You now have {game_state.get_item_count('stick')} sticks.")
                    game_state.mark_puzzle_completed(puzzle_id)
                    current_story_id = puzzle["next"]  # Transition to the next story point
                    break
                else:
                    print("Incorrect. Try again or type 'hint' for help.")
                    if user_solution.lower() == "hint":
                        print(puzzle.get("hint", "No hints available."))
            continue

        # Display choices if available
        if "choices" in story and story["choices"]:
            print("What would you like to do?")
            for i, choice in enumerate(story["choices"], start=1):
                # Skip the option to get help from Acornelius if he has already helped
                if choice["next"] == "gather_with_acornelius" and game_state.has_acornelius_helped():
                    continue
                print(f"{i}. {choice['text']}")
            print(f"{len(story['choices']) + 1}. Exit the game")  # Add an exit option

            try:
                choice_index = int(input("> ")) - 1
                if 0 <= choice_index < len(story["choices"]):
                    next_story_id = story["choices"][choice_index]["next"]
                    # Mark Acornelius as having helped if the player chooses that option
                    if next_story_id == "gather_with_acornelius":
                        game_state.mark_acornelius_helped()
                    # Check if the player has enough sticks to complete the dam
                    if next_story_id == "dam_complete":
                        stick_count = game_state.get_item_count("stick")
                        if stick_count < 3:
                            print(f"You need at least 3 sticks to complete the dam! You currently have {stick_count} stick(s).")
                            continue  # Stay in the current story
                    current_story_id = next_story_id
                elif choice_index == len(story["choices"]):  # Exit option
                    print("Thank you for playing! Goodbye.")
                    break
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a number.")
        else:
            print("There are no paths forward from here. Type 'exit' to quit or 'restart' to return to the beginning.")
            user_input = input("> ").strip().lower()
            if user_input == "exit":
                print("Thank you for playing! Goodbye.")
                break
            elif user_input == "restart":
                current_story_id = "intro"  # Restart the game
            else:
                print("Invalid input. Returning to the current story.")

if __name__ == "__main__":
    play_game()