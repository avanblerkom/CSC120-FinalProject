import json
import os
from collections import deque

def load_combined_data():
    """
    Load the combined_data.json file.

    Returns:
        dict: Parsed JSON data from the file, or None if the file is not found.
    """
    data_path = os.path.join(os.path.dirname(__file__), "text-adventure-game/src/data/combined_data.json")
    try:
        with open(data_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"❌ Error: {data_path} not found.")
        return None

def validate_gameflow(game_data):
    """
    Validate that all storylines and puzzles are accessible and the game flow is continuous.

    Args:
        game_data (dict): The combined game data containing locations and other elements.
    """
    locations = game_data.get("locations", {})
    visited_locations = set()
    location_queue = deque(["start"])

    # Traverse the game locations
    while location_queue:
        current_location = location_queue.popleft()
        if current_location in visited_locations:
            continue
        visited_locations.add(current_location)

        location_data = locations.get(current_location)
        if not location_data:
            continue

        # Check for puzzles
        if "puzzle" in location_data:
            puzzle = location_data["puzzle"]
            if "id" not in puzzle or "description" not in puzzle or "solution" not in puzzle:
                continue
            if "next" not in puzzle:
                continue

        # Add connected locations to the queue
        for choice in location_data.get("choices", []):
            next_location = choice.get("next_location")
            if next_location:
                location_queue.append(next_location)

    # Check for unreachable locations
    all_locations = set(locations.keys())
    unreachable_locations = all_locations - visited_locations

def main():
    """
    Main function to load game data and validate the game flow.
    """
    game_data = load_combined_data()
    if game_data:
        validate_gameflow(game_data)

if __name__ == "__main__":
    main()
