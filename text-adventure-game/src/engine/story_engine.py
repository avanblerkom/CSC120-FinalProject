import json
import os
import string
from typing import List, Dict, Optional

class StoryEngine:
    def __init__(self, story_data: Dict[str, Dict], map_data: Dict[str, Dict]):
        """
        Initialize the StoryEngine with story data, map data, and load puzzles.
        """
        self.story_data = story_data
        self.map_data = map_data
        self.current_story: Optional[Dict] = None
        self.puzzles = self.load_puzzles()

    def load_story(self, story_id: str) -> None:
        """
        Load a story point by its ID.
        """
        if story_id in self.story_data:
            self.current_story = self.story_data[story_id]
            print(f"DEBUG: Loaded story '{story_id}' with text: {self.current_story.get('text', '')}")  # Debugging line
        else:
            raise ValueError(f"Story ID '{story_id}' not found.")

    def get_choices(self) -> List[Dict]:
        """
        Get the list of choices for the current story point.
        """
        if self.current_story:
            return self.current_story.get('choices', [])
        return []

    def make_choice(self, user_input: str, game_state) -> None:
        """
        Make a choice based on the user input and load the next story point.
        """
        # Validate user input and handle choices
        choices = self.get_choices()
        try:
            choice_index = int(user_input) - 1
            if 0 <= choice_index < len(choices):
                choice = choices[choice_index]
                if "required_item" in choice and choice["required_item"] not in game_state.inventory:
                    print(f"You need {choice['required_item']} to proceed.")
                    return
                if "reward_item" in choice:
                    game_state.update_inventory(choice["reward_item"])
                if game_state.get_item_count("stick") < 3:
                    print("You need at least 3 sticks to complete the dam!")
                    return
                self.load_story(choice["next"])
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    def load_puzzles(self) -> Dict[int, Dict]:
        """
        Load puzzles from the puzzles.json file.
        """
        try:
            # Dynamically construct the absolute path to puzzles.json
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            puzzles_path = os.path.join(base_dir, "data", "puzzles.json")
            with open(puzzles_path, "r") as file:
                return {puzzle["id"]: puzzle for puzzle in json.load(file)["puzzles"]}
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: puzzles.json file not found at {puzzles_path}")
        except json.JSONDecodeError:
            raise ValueError("Error: Failed to parse puzzles.json.")

    def solve_puzzle(self, puzzle_id: int, user_solution: str) -> bool:
        """
        Check if the user's solution matches any of the puzzle's valid solutions.
        """
        # Simplify puzzle solution logic
        puzzle = self.puzzles.get(puzzle_id)
        if not puzzle:
            raise ValueError(f"Puzzle ID '{puzzle_id}' not found.")
        
        # Normalize user solution and valid solutions for comparison
        normalized_user_solution = user_solution.strip().lower().translate(str.maketrans('', '', string.punctuation))
        valid_solutions = [
            sol.strip().lower().translate(str.maketrans('', '', string.punctuation))
            for sol in puzzle["solution"]
        ]
        return normalized_user_solution in valid_solutions

    def get_location_story(self, location: str) -> Dict:
        """
        Retrieve the story associated with the given location.
        """
        location_data = self.map_data.get(location, {})
        story_id = location_data.get("story", {}).get("id")
        if story_id and story_id in self.story_data:
            return self.story_data[story_id]
        return location_data.get("story", {})

    def get_location_choices(self, location: str) -> List[Dict]:
        """
        Retrieve the choices available at the given location.
        """
        return self.map_data.get(location, {}).get("choices", [])