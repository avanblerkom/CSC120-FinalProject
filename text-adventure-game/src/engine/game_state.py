import json

class GameState:
    """
    Manages the state of the game, including inventory, progress, and location.
    """

    def __init__(self):
        """
        Initialize the game state with default values.
        """
        self.inventory = {}  # Dictionary to track item counts
        self.progress = {}
        self.completed_puzzles = set()  # Set to track completed puzzles
        self.current_location = "start"  # Initial location
        self.acornelius_helped = False  # Track if Acornelius has helped the player

    def update_inventory(self, item_name):
        """
        Add an item to the inventory or increment its count.

        Args:
            item_name (str): The name of the item to add.
        """
        if item_name in self.inventory:
            self.inventory[item_name] += 1
        else:
            self.inventory[item_name] = 1

    def remove_from_inventory(self, item_name, count=1):
        """
        Remove a specified quantity of an item from the inventory.

        Args:
            item_name (str): The name of the item to remove.
            count (int): The quantity to remove (default is 1).
        """
        if item_name in self.inventory:
            self.inventory[item_name] -= count
            if self.inventory[item_name] <= 0:
                del self.inventory[item_name]

    def has_items(self, required_items):
        """
        Check if the inventory contains the required items in the specified quantities.

        Args:
            required_items (dict): A dictionary of item names and required quantities.

        Returns:
            bool: True if all required items are present, False otherwise.
        """
        for item, count in required_items.items():
            if self.inventory.get(item, 0) < count:
                return False
        return True

    def get_item_count(self, item_name):
        """
        Get the count of a specific item in the inventory.

        Args:
            item_name (str): The name of the item.

        Returns:
            int: The count of the item (0 if not present).
        """
        return self.inventory.get(item_name, 0)

    def save_state(self, filename="game_state.json"):
        """
        Save the current game state to a file.

        Args:
            filename (str): The name of the file to save the state to (default is 'game_state.json').
        """
        with open(filename, 'w') as file:
            state_data = {
                'inventory': self.inventory,
                'progress': self.progress,
                'completed_puzzles': list(self.completed_puzzles),
                'current_location': self.current_location
            }
            json.dump(state_data, file)

    def load_state(self, filename="game_state.json"):
        """
        Load the game state from a file.

        Args:
            filename (str): The name of the file to load the state from (default is 'game_state.json').
        """
        try:
            with open(filename, 'r') as file:
                state_data = json.load(file)
                self.inventory = state_data.get('inventory', {})
                self.progress = state_data.get('progress', {})
                self.completed_puzzles = set(state_data.get('completed_puzzles', []))
                self.current_location = state_data.get('current_location', "start")
        except FileNotFoundError:
            print(f"❌ Error: {filename} not found. Starting a new game.")

    def mark_puzzle_completed(self, puzzle_id):
        """
        Mark a puzzle as completed.

        Args:
            puzzle_id (int): The ID of the puzzle to mark as completed.
        """
        self.completed_puzzles.add(puzzle_id)

    def is_puzzle_completed(self, puzzle_id):
        """
        Check if a puzzle has been completed.

        Args:
            puzzle_id (int): The ID of the puzzle.

        Returns:
            bool: True if the puzzle is completed, False otherwise.
        """
        return puzzle_id in self.completed_puzzles

    def update_location(self, new_location):
        """
        Update the current location of the player.

        Args:
            new_location (str): The new location ID.
        """
        self.current_location = new_location

    def get_location(self):
        """
        Get the current location of the player.

        Returns:
            str: The current location ID.
        """
        return self.current_location

    def mark_acornelius_helped(self):
        """
        Mark that Acornelius has helped the player.
        """
        self.acornelius_helped = True

    def has_acornelius_helped(self):
        """
        Check if Acornelius has helped the player.

        Returns:
            bool: True if Acornelius has helped, False otherwise.
        """
        return self.acornelius_helped