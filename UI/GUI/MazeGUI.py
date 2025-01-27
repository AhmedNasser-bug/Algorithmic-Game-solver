import tkinter as tk
from sys import *
from os import getcwd
path.append(getcwd())
from UI.UI_setup import *
from Algorithms import DLS, IDDFS, BestFirstSearch, HillClimb



class MazeGame:
    def __init__(self, root, rows, cols, complexity, animation_speed, algorithm, *algorithm_args):
        self.root = root
        self.cell_size = 15
        self.animation_speed = animation_speed
        
        # Game parameters
        self.rows = rows
        self.cols = cols
        self.complexity = complexity
        self.algorithm = algorithm
        self.algorithm_args = algorithm_args
        
        # Game state
        self.state = (0, 0)  # start position
        self.target = (rows-1, cols-1)  # bottom-right corner
        self.maze = self.generate_maze()
        self.path = []
        
        self.setup_ui()
    
    def setup_ui(self):
        # Create canvas
        self.canvas = ctk.CTkCanvas(
            self.root,
            width=self.cols * self.cell_size,
            height=self.rows * self.cell_size
        )
        self.canvas.pack()
        
        # Control buttons
        self.button_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.button_frame.pack(pady=20)
        
        self.solve_button = ctk.CTkButton(
            self.button_frame,
            text="Solve",
            command=self.solve,
            font=("Helvetica", 14),
            width=120
        )
        self.solve_button.pack(side="left", padx=10)
        
        self.regenerate_button = ctk.CTkButton(
            self.button_frame,
            text="Regenerate",
            command=self.regenerate_maze,
            font=("Helvetica", 14),
            width=120
        )
        self.regenerate_button.pack(side="left", padx=10)
        
        self.draw_maze()
    
    def generate_maze(self):
        # Create a new Maze instance (assuming you have a Maze class)
        self.main_maze = Maze(self.rows, self.cols, self.complexity)
        return self.main_maze.maze
    
    def draw_maze(self):
        self.canvas.delete("all")  # Clear canvas
        for i, row in enumerate(self.maze):
            for j, cell in enumerate(row):
                color = "white" if cell == 0 else "black"
                if (i,j) == self.state:
                    color = "cyan"
                elif (i,j) == self.target:
                    color = "red"
                    
                self.canvas.create_rectangle(
                    j * self.cell_size,
                    i * self.cell_size,
                    (j + 1) * self.cell_size,
                    (i + 1) * self.cell_size,
                    fill=color,
                    tags="maze"  # Add tag for maze cells
                )
    
    def draw_path(self, path):
    # Clear previous path
        self.canvas.delete("path")  # Only delete path elements

        def animate_path(index):
            if index < len(path):
                # Draw current step
                row, col = path[index].value
                self.canvas.create_rectangle(
                    col * self.cell_size,
                    row * self.cell_size,
                    (col + 1) * self.cell_size,
                    (row + 1) * self.cell_size,
                    fill="green",
                    tags="path"
                )

                # Schedule next step
                self.root.after(self.animation_speed, animate_path, index + 1)
            else:
                # Animation complete, ensure start and target are visible
                self.canvas.create_rectangle(
                    0, 0, 
                    self.cell_size, self.cell_size,
                    fill="cyan",
                    tags="path"
                )
                self.canvas.create_rectangle(
                    (self.cols-1) * self.cell_size,
                    (self.rows-1) * self.cell_size,
                    self.cols * self.cell_size,
                    self.rows * self.cell_size,
                    fill="red",
                    tags="path"
                )

        # Start animation
        animate_path(0)


    
    def solve(self):
        # Reset state to starting position
        self.state = (0, 0)
        
        # Clear previous path
        self.path = []
        self.draw_maze()  # Redraw maze to clear previous solution
        
        # Run algorithm
        try:
            self.path = self.algorithm(self.main_maze.root, self.main_maze.goal_condition,idx(self.main_maze.goal[0], self.main_maze.goal[1]), *self.algorithm_args)
            
            if self.path:
                self.draw_path(self.path)
            else:
                messagebox.showerror("Error", "No solution found!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def regenerate_maze(self):
        
        # Reset state
        self.state = (0, 0)
        self.path = []
        
        # Clear and redraw
        self.draw_maze()


                                                # DLS     # Limit
def get_maze_gui(rows, cols, complexity_of_maze, algorithm, *algorithm_args):
    '''
    Creates and Displays a MazeGUI instance with the given parameters.
    Do not include the root of the maze or the goal condition args 
    '''
    root = tk.Tk()
    gui = MazeGame(root, rows, cols, complexity_of_maze, algorithm, *algorithm_args)
    root.mainloop()

if __name__ == "__main__":
     get_maze_gui(10, 10, 35, 10, IDDFS.IterativeDS) # DLS with a limit of 30 steps_maze_gui(35, 35, 35, Bes, 30) # DLS with a limit of 30 steps
    