# Summary
Python-based system using reusable pathfinding algorithms to solve multiple games via a common Graph 
interface. Easily extensible for new games.
# Role
1. Implemented pathfinding algorithms (DLS, BFS, IDDFS, HillClimb).
2. Initialized and implemented the idea of unified graph solver algorithms.
3. Implemented sudoku game graph by assigning each empty box to its all possible number, and the goal is the box with exactly one possible choice.
4. Implemented 8 queens game graph by generating each possible position for all 8 queens inside the 8x8 board, and the goal is a valid 8 queens board.
5. Implemented Maze game graph by generating a new random maze then turning all possible moves from the start to the goal into a graph. 
7. Built both CLI/GUI testing environments with unified interfaces.
# Technologies
1. python
2. tkinter
3. customkinter
4. GitHub for version control
5. Claude 3.5 Sonnet for building most GUI blocks.
# How to run
In order to run the project run the "Main Screen.py" file found in the UI Folder , Thats it!

## Application UI
![Screenshot 2025-02-13 162610](https://github.com/user-attachments/assets/8c035a61-9ae3-4dae-a8e3-1c0f7fd3c215) ![Screenshot 2025-02-13 162622](https://github.com/user-attachments/assets/38521a1d-5bb0-4430-ac3b-8ce68989af46)
## Sudoku after using Best First Search on Sudoku Graph
![Screenshot 2025-02-13 162653](https://github.com/user-attachments/assets/69680a9a-ab0b-42ae-9743-e5b7824c119a) Sudoku
## Best First Search in the middle of searching for maze Goal [Red Box]
![Screenshot 2025-02-13 162712](https://github.com/user-attachments/assets/d41c04cf-8378-4d94-8e64-fa7574f49f51) Maze
## Best First Search after Searching for a Valid 8 queens board inside the Graph of all possible 8 queens positions
![Screenshot 2025-02-13 162734](https://github.com/user-attachments/assets/801c7e99-468a-49bf-9352-a3eebc741483) 8 Queens
