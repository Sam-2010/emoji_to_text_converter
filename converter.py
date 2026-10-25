import json
import os

class EmojiConverter:
    """Core engine responsible for loading emoji mappings and processing text."""

    def __init__(self, json_filepath="emojis.json"):
        self.json_filepath = json_filepath
        self.emoji_map = {}
        self.load_mappings()

    def load_mappings(self):
        """Loads emoji mappings from the external JSON file."""
        if not os.path.exists(self.json_filepath):
            raise FileNotFoundError(f"Configuration file '{self.json_filepath}' was not found.")

        try:
            with open(self.json_filepath, "r", encoding="utf-8") as file:
                self.emoji_map = json.load(file)
        except json.JSONDecodeError:
            raise ValueError(f"File '{self.json_filepath}' contains invalid JSON formatting.")

    def convert(self, text):
        """Replaces emojis in the input string with bracketed descriptions."""
        if not text:
            return ""

        processed_text = text
        for emoji_char, description in self.emoji_map.items():
            processed_text = processed_text.replace(emoji_char, f"[{description}]")
        
        return processed_text

    def get_count(self):
        """Returns the total number of loaded emoji mappings."""
        return len(self.emoji_map)