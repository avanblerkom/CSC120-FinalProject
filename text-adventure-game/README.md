# Text-Based Adventure Game

## Overview
This project is a text-based adventure game where players navigate through a story-driven world by making choices. Players take on the role of Justin the Beaver, exploring the wilderness, gathering resources, and overcoming challenges to build a thriving dam and lodge.

## Features
- **Branching Narratives**: Players' choices will lead to different story paths and outcomes.
- **Puzzles and Challenges**: Engage with various puzzles that test decision-making skills.
- **Character Interactions**: Meet and interact with various characters, each with unique traits and roles in the story.

## Project Structure
```
text-adventure-game
├── src
│   ├── main.py                # Entry point of the game
│   ├── engine
│   │   ├── story_engine.py     # Manages branching narratives
│   │   ├── text_parser.py      # Interprets player input
│   │   └── game_state.py       # Manages game state
│   ├── data
│   │   ├── characters.json      # Character data
│   │   ├── story_scripts.json    # Narrative scripts
│   │   └── puzzles.json         # Puzzle data
│   ├── ui
│   │   └── text_interface.py    # User interface management
│   └── utils
│       └── helpers.py          # Utility functions
├── tests
│   ├── test_story_engine.py     # Unit tests for StoryEngine
│   ├── test_text_parser.py      # Unit tests for TextParser
│   └── test_game_state.py       # Unit tests for GameState
├── requirements.txt             # Project dependencies
└── projectproposal.txt          # Initial project proposal
```

## Setup Instructions
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using:
   ```
   pip install -r requirements.txt
   ```
4. Run the game by executing:
   ```
   python src/main.py
   ```

## Gameplay
Players will navigate through the wilderness, making choices that affect the story's outcome. They will encounter various characters, solve puzzles, and manage resources to achieve their goal of building a dam and lodge.

## Contribution Guidelines
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code is well-documented and includes tests where applicable.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.