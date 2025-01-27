from sys import*
from os import getcwd
path.append(getcwd())
from tkinter import*
from UI.UI_setup import*



class QueenGame:
    def __init__(self, root, animation_speed, algorithm, *algorithm_args):
        self.root = root
        self.animation_speed = animation_speed
        self.algorithm = algorithm
        self.algorithm_args = algorithm_args
        self.etqueens = Eight_Queen()
        self.cell_size = 60  # Size of each chess cell
        self.board_size = 8  # 8x8 chess board
        
        # Game state
        self.board = self.etqueens.board_start  # Empty board
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main container
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(padx=20, pady=20)
        
        # Chess board canvas
        self.canvas = ctk.CTkCanvas(
            self.main_frame,
            width=self.board_size * self.cell_size,
            height=self.board_size * self.cell_size,
            bg="white"
        )
        self.canvas.pack(pady=20)
        
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
        
        # Draw initial board
        self.draw_board()
        
    def draw_board(self):
        self.canvas.delete("all")
        
        # Draw chess board pattern
        for row in range(self.board_size):
            for col in range(self.board_size):
                # Calculate position
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                
                # Alternate colors for chess pattern
                color = "#FFFFFF" if (row + col) % 2 == 0 else "#4A4A4A"
                
                # Draw cell
                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color,
                    outline=""
                )
                
                # Draw queen if present
                if self.board[row][col] == "Q":
                    self.canvas.create_text(
                        x1 + self.cell_size/2,
                        y1 + self.cell_size/2,
                        text="👑",
                        font=("TkDefaultFont", int(self.cell_size*0.7)),
                        tags="queen"
                    )
    
    def update_board(self, new_state):
        """Update the board with a new state"""
        self.board = new_state
        self.draw_board()
    
    def animate_move(self, states):
        """Animate a sequence of board states"""
        def animate_step(step):
            if step < len(states):
                board = get_board_string(states[step].value)
                self.update_board(board)
                self.root.after(self.animation_speed, animate_step, step + 1)
        
        animate_step(0)
    
    def solve(self):
        """Placeholder for solve command - to be connected externally"""
        path = self.algorithm(self.etqueens.root, self.etqueens.evaluation_function,[],*self.algorithm_args)
        if path:
            self.animate_move(path)
        else:
            messagebox.showerror('Solution not found')
    
    def reset(self):
        """Reset the board to initial state"""
        self.etqueens = Eight_Queen()
        self.board = self.etqueens.board_start
        self.draw_board()

def EightQueenGUI(algorithm, *args):
    root = Tk()
    root.title("Eight Queens Solver")
    QueenGame(root, 5,  algorithm, *args)
    root.mainloop()

if __name__ == "__main__":
    root = Tk()
    root.title("Eight Queens Solver")
    QueenGame(root, 0,  HillClimb.hill_climb)
    root.mainloop()

