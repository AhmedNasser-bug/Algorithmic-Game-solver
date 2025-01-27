from sys import *
from os import getcwd
path.append(getcwd())
from Sudoku_Solver.Sudoku import *
from tkinter import *
from Algorithms.IDDFS import *
from UI.UI_setup import *




class SudokuGame:
    def __init__(self, root, algorithm, *algorithm_args):
        self.root = root
        self.algorithm = algorithm
        self.algorithm_args = algorithm_args
        self.cell_size = 50
        self.board_size = 9
        
        self.game = Sudoku()
        # Hardcoded initial Sudoku board (0 represents empty cells)
        self.initial_board = self.game.board
        
        # Current board state
        self.board = [row[:] for row in self.initial_board]
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main container
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(padx=20, pady=20)
        
        # Sudoku board canvas
        self.canvas = ctk.CTkCanvas(
            self.main_frame,
            width=self.board_size * self.cell_size,
            height=self.board_size * self.cell_size,
            bg="white"
        )
        self.canvas.pack(pady=20)
        
        # Create labels for each cell
        self.cells = []
        for i in range(9):
            row = []
            for j in range(9):
                label = tk.Label(
                    self.canvas,
                    font=('Arial', 18, 'bold'),
                    justify='center',
                    width=2,
                    bg='white'
                )
                # Place label widget on canvas
                self.canvas.create_window(
                    j * self.cell_size + self.cell_size/2,
                    i * self.cell_size + self.cell_size/2,
                    window=label
                )
                row.append(label)
            self.cells.append(row)
        
        # Draw grid lines
        self.draw_grid()
        
        # Control buttons frame
        self.button_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.button_frame.pack(pady=10)
        
        # Solve button
        self.solve_button = ctk.CTkButton(
            self.button_frame,
            text="Solve",
            command=self.solve,
            font=("Helvetica", 14),
            width=120
        )
        self.solve_button.pack(side="left", padx=10)
        
        # Reset button
        self.reset_button = ctk.CTkButton(
            self.button_frame,
            text="Reset",
            command=self.reset,
            font=("Helvetica", 14),
            width=120
        )
        self.reset_button.pack(side="left", padx=10)
        
        # Display initial board
        self.display_board()
    
    def draw_grid(self):
        # Draw the Sudoku grid lines
        for i in range(10):
            # Determine line width (thicker for 3x3 box borders)
            line_width = 2 if i % 3 == 0 else 1
            
            # Draw vertical lines
            self.canvas.create_line(
                i * self.cell_size, 0,
                i * self.cell_size, self.board_size * self.cell_size,
                width=line_width
            )
            
            # Draw horizontal lines
            self.canvas.create_line(
                0, i * self.cell_size,
                self.board_size * self.cell_size, i * self.cell_size,
                width=line_width
            )
    
    def display_board(self):
        """Display the current board state"""
        for i in range(9):
            for j in range(9):
                value = self.board[i][j]
                if value != 0:
                    self.cells[i][j].config(
                        text=str(value),
                        fg='black' if self.initial_board[i][j] != 0 else 'blue'
                    )
                else:
                    self.cells[i][j].config(text='')
    
    def update_cell(self, position, value):
        """Update a single cell with new value"""
        i, j = position
        self.board[i][j] = value
        self.cells[i][j].config(
            text=str(value) if value != 0 else '',
            fg='blue',
            bg='lightgreen'
        )
        self.root.update()
    
    def animate_solution(self, solution_steps):
        """Animate the solution steps"""
        def animate_step(step):
            if step < len(solution_steps):
                
                i,j, value = solution_steps[step]
                self.update_cell((i,j), value[0])
                # Reset previous cell color
                if step > 0:
                    i,j, _ = solution_steps[step-1]
                    self.cells[i][j].config(bg='white')
                self.root.after(100, animate_step, step + 1)
            else:
                # Reset all cell colors
                for i in range(9):
                    for j in range(9):
                        self.cells[i][j].config(bg='white')
        
        animate_step(0)
    
    def solve(self):
        """Placeholder for solve command"""
        path = [node.value for node in self.game.sudoku_tester(self.algorithm, *self.algorithm_args)]
        self.animate_solution(path)
    
    def reset(self):
        """Reset to initial board state"""
        self.board = [row[:] for row in self.initial_board]
        for i in range(9):
            for j in range(9):
                self.cells[i][j].config(bg='white')
        self.display_board()

if __name__ ==  "__main__":
    root = Tk()
    root.title("Sudoku Solver")
    root.geometry("700x600")

    SudokuGame(root, IterativeDS)
    root.mainloop()