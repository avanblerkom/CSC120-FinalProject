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
          [Upstream] (upstream)
              |
              v
           [River] (gather_materials) <--> [Mountain Path] (mountain_path) <--> [Mountain Peak] (mountain_peak)
              |                              ^
              v                              |
[Pond] (intro) <--> [Forest] (forest_exploration) <--> [Deep Forest] (deeper_forest) <--> [Clearing] (clearing)
              ^                              |
              |                              v
          [Collect Sticks] (collect_sticks) <--> [Build Dam] (build_dam)
```

### Navigation Notes:
- **Pond**: The starting point of your adventure. You can explore the forest, gather materials at the river, or attempt to build the dam here.
- **Forest**: A dense forest with towering trees. Connects to the pond, river, and deep forest.
- **Deep Forest**: A quiet and mysterious part of the forest. Leads to the clearing and forest.
- **River**: A rushing river with the sound of water filling the air. Connects to the pond, forest, upstream, and mountain path.
- **Upstream**: A small waterfall located upstream of the river. Connects to the river and mountain path.
- **Mountain Path**: A rocky path leading to higher elevations. Connects to upstream, clearing, and mountain peak.
- **Mountain Peak**: The highest point in the game. You can descend back to the mountain path or go to the clearing.
- **Clearing**: A sunny clearing with scattered sticks on the ground. Contains a puzzle. Connects to the deep forest, mountain path, and upstream.
- **Collect Sticks**: A location where you gather sticks for building the dam. Connects to the clearing and build dam location.
- **Build Dam**: The final location where you use collected sticks to complete the dam and win the game.

### Story Script Associations
The following table shows which story scripts are associated with each physical location:
| Location         | Story Script ID       |
|------------------|-----------------------|
| Pond             | `intro`              |
| Forest           | `forest_exploration` |
| Deep Forest      | `deeper_forest`      |
| River            | `gather_materials`   |
| Upstream         | `upstream`           |
| Mountain Path    | `mountain_path`      |
| Mountain Peak    | `mountain_peak`      |
| Clearing         | `clearing`           |
| Collect Sticks   | `collect_sticks`     |
| Build Dam        | `build_dam`          |

### Updated Notes:
- The starting location is now referred to as the **Pond**.
- The `upstream` location has been updated to reflect its correct story script ID.
- The option to build the dam at the pond is now included in the navigation notes.

