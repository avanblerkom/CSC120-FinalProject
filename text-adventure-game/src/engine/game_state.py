import json

class GameState:
    def __init__(self):
        self.inventory = {}  # Use a dictionary to track item counts
        self.progress = {}
        self.completed_puzzles = set()  # Track completed puzzles
        self.current_location = "start"  # Initial location

    def update_inventory(self, item):
        if item in self.inventory:
            self.inventory[item] += 1
        else:
            self.inventory[item] = 1
        print(f"DEBUG: Added '{item}' to inventory. You now have {self.inventory[item]} {item}(s).")

    def remove_from_inventory(self, item, count=1):
        if item in self.inventory:
            self.inventory[item] -= count
            if self.inventory[item] <= 0:
                del self.inventory[item]
        else:
            print(f"DEBUG: '{item}' not found in inventory.")

    def has_items(self, items):
        for item, count in items.items():
            if self.inventory.get(item, 0) < count:
                return False
        return True

    def get_item_count(self, item):
        return self.inventory.get(item, 0)

    def save_state(self, filename):
        with open(filename, 'w') as file:
            state_data = {
                'inventory': self.inventory,
                'progress': self.progress,
                'completed_puzzles': list(self.completed_puzzles)
            }
            json.dump(state_data, file)

    def load_state(self, filename):
        with open(filename, 'r') as file:
            state_data = json.load(file)
            self.inventory = state_data.get('inventory', {})
            self.progress = state_data.get('progress', {})
            self.completed_puzzles = set(state_data.get('completed_puzzles', []))

    def mark_puzzle_completed(self, puzzle_id):
        self.completed_puzzles.add(puzzle_id)
        print(f"DEBUG: Marked puzzle {puzzle_id} as completed.")  # Debugging line

    def is_puzzle_completed(self, puzzle_id):
        return puzzle_id in self.completed_puzzles

    def update_location(self, new_location):
        self.current_location = new_location
        print(f"DEBUG: Moved to location '{new_location}'.")

    def get_location(self):
        return self.current_location