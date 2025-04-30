This file will contain documentation for all commands available in your game.

Note: It's a good idea to also make this list available inside the game, in response to a `HELP` command.

# Cheatsheet

## Available Commands
- **go [direction]**: Move to a different location (e.g., `go north`, `go east`).
- **take [item]**: Pick up an item (e.g., `take stick`).
- **use [item]**: Use an item from your inventory (e.g., `use stick`).
- **inventory**: Check your current inventory.
- **help**: Display this cheatsheet.
- **quit**: Exit the game.

## Game World Layout
Below is a map of the game's physical layout:

```
          [Upstream] (climb_tree)
              |
              v
           [River] (gather_materials) <--> [Mountain Path] (mountain_path) <--> [Mountain Peak] (mountain_peak)
              |                              ^
              v                              |
[Start] (intro) <--> [Forest] (forest_exploration) <--> [Deep Forest] (deeper_forest) <--> [Clearing] (clearing)
              ^                              |
              |                              v
          [Upstream] <-----------------------+
```

### Navigation Notes:
- **Start**: The starting point of your adventure. You can reach it directly from the forest or the river.
- **Forest**: A dense forest with towering trees. Connects to the start, river, and deep forest.
- **Deep Forest**: A quiet and mysterious part of the forest. Leads to the clearing, river, and forest.
- **River**: A rushing river with the sound of water filling the air. Connects to the start, forest, upstream, and mountain path.
- **Upstream**: A small waterfall located upstream of the river. Connects to the river, clearing, and mountain path.
- **Mountain Path**: A rocky path leading to higher elevations. Connects to upstream, clearing, river, and mountain peak.
- **Mountain Peak**: The highest point in the game. You can descend back to the mountain path.
- **Clearing**: A sunny clearing with scattered sticks on the ground. Contains a puzzle. Connects to the deep forest, mountain path, and upstream.

### Story Script Associations
The following table shows which story scripts are associated with each physical location:
| Location         | Story Script ID       |
|------------------|-----------------------|
| Start            | `intro`              |
| Forest           | `forest_exploration` |
| Deep Forest      | `deeper_forest`      |
| River            | `gather_materials`   |
| Upstream         | `climb_tree`         |
| Mountain Path    | `mountain_path`      |
| Mountain Peak    | `mountain_peak`      |
| Clearing         | `clearing`           |

