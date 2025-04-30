This file will contain documentation for all commands available in your game.

Note:  It's a good idea to also make this list available inside the game, in response to a `HELP` command.


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

### Descriptions:
- **Start**: The starting point of your adventure.
- **Forest**: A dense forest with towering trees. Connects to the river and deep forest.
- **Deep Forest**: A quiet and mysterious part of the forest. Leads to the clearing and river.
- **River**: A rushing river with the sound of water filling the air. Connects to upstream, the forest, and the mountain path.
- **Upstream**: A small waterfall located upstream of the river. Connects to the mountain path and the clearing.
- **Mountain Path**: A rocky path leading to higher elevations. Connects to upstream, the clearing, the river, and the mountain peak.
- **Clearing**: A sunny clearing with scattered sticks on the ground. Contains a puzzle. Connects to the deep forest, mountain path, and upstream.
- **Mountain Peak**: The highest point in the game. Contains a pile of sticks left by a bird.

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

