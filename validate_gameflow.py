import json
import os
from collections import deque

def load_combined_data():
    """Load the combined_data.json file."""
    data_path = os.path.join(os.path.dirname(__file__), "text-adventure-game/src/data/combined_data.json")
    try:
        with open(data_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"❌ Error: {data_path} not found.")
        return None

def validate_gameflow(data):
    """Validate that all storylines and puzzles are accessible and the game flow is continuous."""
    locations = data.get("locations", {})
    visited = set()
    queue = deque(["start"])

    # Traverse the game locations
    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)

        location = locations.get(current)
        if not location:
            print(f"❌ Error: Location '{current}' is missing in the data.")
            continue

        # Check for puzzles
        if "puzzle" in location:
            puzzle = location["puzzle"]
            if "id" not in puzzle or "description" not in puzzle or "solution" not in puzzle:
                print(f"❌ Error: Puzzle in location '{current}' is incomplete.")
            if "next" not in puzzle:
                print(f"❌ Error: Puzzle in location '{current}' does not specify the next location.")

        # Add connected locations to the queue
        for choice in location.get("choices", []):
            next_location = choice.get("next_location")
            if next_location:
                queue.append(next_location)
            else:
                print(f"❌ Error: Choice in location '{current}' is missing a 'next_location'.")

    # Check for unreachable locations
    all_locations = set(locations.keys())
    unreachable = all_locations - visited
    if unreachable:
        print(f"❌ Error: The following locations are unreachable: {', '.join(unreachable)}")
    else:
        print("✅ All locations are reachable.")

    # Check for dead ends
    for loc_id, loc_data in locations.items():
        if not loc_data.get("choices") and loc_id != "dam_complete":
            print(f"⚠️ Warning: Location '{loc_id}' is a dead end.")

def main():
    data = load_combined_data()
    if data:
        validate_gameflow(data)

if __name__ == "__main__":
    main()
