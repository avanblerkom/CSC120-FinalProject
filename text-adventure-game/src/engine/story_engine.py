import json
import os
import string
from typing import Dict, Optional

class StoryEngine:
    def __init__(self, combined_data):
        self.data = combined_data
        self.current_location = None

    def load_location(self, location_id):
        if location_id in self.data["locations"]:
            self.current_location = self.data["locations"][location_id]
        else:
            raise ValueError(f"Location ID '{location_id}' not found.")

    def get_story_text(self):
        if self.current_location and "story" in self.current_location:
            return self.current_location["story"].get("text", "No story available.")
        return "No story available."

    def get_choices(self):
        if self.current_location:
            return self.current_location.get("choices", [])
        return []