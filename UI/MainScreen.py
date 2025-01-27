from sys import*
from os import getcwd
path.append(getcwd())
from UI.GUI.SudokuGUI import*
from UI.GUI.EightQueenGUI import *
from UI.GUI.MazeGUI import *
from UI.UI_setup import*
from Algorithms import* 


class ModernAlgorithmGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Algorithm Selection")
   
        # Add this color scheme dictionary
        self.colors = {
            'primary': "#651fff",        # Main purple
            'primary_dark': "#4615b2",   # Darker purple
            'header': "#1a237e",         # Deep indigo
            'text_primary': "#263238",   # Dark blue grey
            'text_light': "#ffffff",     # White
            'success': "#00c853",        # Bright green
            'success_dark': "#00b248",   # Darker green
            'back': "#546e7a",           # Blue grey
            'back_dark': "#455a64",      # Darker blue grey
            'problem_1': "#00bcd4",      # Cyan
            'problem_2': "#7c4dff",      # Deep purple
            'problem_3': "#ff4081",      # Pink accent
            'background': "#f5f5f5",     # Light grey background
            'card': "#ffffff",           # White card background
             }
        
        # Fixed window size with smartphone ratio (9:16)
        window_width = 500
        window_height = 889  # Approximately 16:9 ratio
        self.root.geometry(f"{window_width}x{window_height}")
        self.root.resizable(False, False)
        
        # Set theme
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        self.depth_limit = 0
        self.selected_algorithm = ""
        
        # Create main container
        self.main_frame = ctk.CTkFrame(
            self.root,
            corner_radius=0,
            fg_color="#ffffff"
        )
        self.main_frame.pack(fill="both", expand=True)
        
        # Create header frame with gradient background
        self.header_frame = ctk.CTkFrame(
            self.main_frame,
            height=120,
            corner_radius=0,
            fg_color = self.colors["header"]
        )
        self.header_frame.pack(fill="x", pady=0, padx=0)
        self.header_frame.pack_propagate(False)
        
        # Create logo (you'll need to replace 'logo.png' with your actual logo file)
        try:
            logo_img = Image.open("logo.png")
            logo_img = logo_img.resize((60, 60))
            self.logo = ImageTk.PhotoImage(logo_img)
            self.logo_label = tk.Label(
                self.header_frame,
                image=self.logo,
                bg="#2c3e50"
            )
            self.logo_label.pack(side="left", padx=20)
        except:
            # Fallback if no logo image is found
            self.logo_label = ctk.CTkLabel(
                self.header_frame,
                text="🤖",  # Fallback emoji logo
                font=("Helvetica", 40),
                text_color="#ffffff"
            )
            self.logo_label.pack(side="left", padx=20)
        
        # Title in header
        self.title_label = ctk.CTkLabel(
            self.header_frame,
            text="Algorithm\nSelection",
            font=("Helvetica", 24, "bold"),
            text_color="#ffffff"
        )
        self.title_label.pack(side="left", padx=10)
        
        # Content frame
        self.content_frame = ctk.CTkFrame(
            self.main_frame,
            corner_radius=0,
            fg_color="#f0f0f0"
        )
        self.content_frame.pack(fill="both", expand=True)
        
        self.create_main_buttons()
        
    def create_main_buttons(self):
        # Clear existing widgets in content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()
            
        # Create buttons container
        buttons_frame = ctk.CTkFrame(
            self.content_frame,
            corner_radius=15,
            fg_color="transparent"
        )
        buttons_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        algorithms = [
            "Best First Search",
            "Depth Limited Search",
            "Iterative Deepening DFS",
            "Simple Hill Climb",
            "Breadth First Search"
        ]
        
        for algo in algorithms:
            btn = ctk.CTkButton(
                buttons_frame,
                text=algo,
                font=("Helvetica", 16),
                height=60,
                corner_radius=10,
                command=lambda a=algo: self.algorithm_selected(a),
                fg_color=self.colors["primary"],
                hover_color= self.colors["primary_dark"]
            )
            btn.pack(pady=10, padx=20, fill="x")
            
    def create_problem_buttons(self):
        # Clear existing widgets in content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()
            
        # Create container
        problems_frame = ctk.CTkFrame(
            self.content_frame,
            corner_radius=15,
            fg_color="transparent"
        )
        problems_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Algorithm info
        algo_info = ctk.CTkLabel(
            problems_frame,
            text=f"Selected Algorithm:",
            font=("Helvetica", 16, "bold"),
            text_color="#2c3e50"
        )
        algo_info.pack(pady=(0, 5))
        
        algo_name = ctk.CTkLabel(
            problems_frame,
            text=self.selected_algorithm,
            font=("Helvetica", 14),
            text_color="#2c3e50"
        )
        algo_name.pack(pady=(0, 10))
    
        # Check if it's a non-pathfinding algorithm

        self.create_standard_problem_buttons(problems_frame)


    def algorithm_selected(self, algorithm):
        self.selected_algorithm = algorithm
        
        if algorithm == "Depth Limited Search":
            try:
                dialog = DepthLimitDialog(self.root)
                self.depth_limit = dialog.result
                
                if self.depth_limit is not None:
                    self.create_problem_buttons()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid integer!")
                return
        else:
            self.depth_limit = 0
            self.create_problem_buttons()
            
    def problem_selected(self, problem):
        # Store the current algorithm settings
        settings = {
            'algorithm': self.selected_algorithm,
            'depth_limit': getattr(self, 'depth_limit', None)  # For DLS algorithm
        }

        # Create new window for the game
        game_window = ctk.CTkToplevel(self.root)
        game_window.title(problem)
        game_window.geometry("1000x800")
        game_window.resizable(True, True)

        func_algorithm = self.get_chosen_algorithm(self.selected_algorithm)
        # Initialize appropriate game class based on selection
        if self.depth_limit  != 0:
            if problem == "Sudoku Solver":
                SudokuGame(game_window, func_algorithm, self.depth_limit)
            elif problem == "Maze Solver":
                MazeGame(game_window, 50, 50, 60, 1, func_algorithm, self.depth_limit)
            elif problem == "8-Queen Solver":
                QueenGame(game_window, 2, func_algorithm, self.depth_limit)
        else:
            if problem == "Sudoku Solver":
                SudokuGame(game_window, func_algorithm)
            elif problem == "Maze Solver":
                MazeGame(game_window, 50, 50, 60, 30, func_algorithm)
            elif problem == "8-Queen Solver":
                QueenGame(game_window, 1, func_algorithm)
            

    def get_chosen_algorithm(self, algorithm):
        algorithms = [
            "Best First Search",
            "Depth Limited Search",
            "Iterative Deepening DFS",
            "Simple Hill Climb",
            "Breadth First Search"
        ]
        func_algorithms = [BestFirstSearch.bestfirstsearch, DLS.get_dls_path, IDDFS.IterativeDS, HillClimb.hill_climb, BFS.bfs]
        for algorithm in algorithms:
            if self.selected_algorithm == algorithm:
                return func_algorithms[algorithms.index(algorithm)]
            
    def create_standard_problem_buttons(self, parent_frame):
        problems = [
            ("Sudoku Solver", self.colors["problem_1"]),
            ("Maze Solver", self.colors["problem_2"]),
            ("8-Queen Solver", self.colors["problem_3"])
        ]

        for problem, color in problems:
            btn = ctk.CTkButton(
                parent_frame,
                text=problem,
                font=("Helvetica", 18),
                height=70,
                corner_radius=10,
                command=lambda p=problem: self.problem_selected(p),
                fg_color=color,
                hover_color=color
            )
            btn.pack(pady=15, padx=20, fill="x")

        # Back button
        back_btn = ctk.CTkButton(
            parent_frame,
            text="Back",
            font=("Helvetica", 14),
            height=50,
            corner_radius=10,
            command=self.create_main_buttons,
            fg_color="#95a5a6",
            hover_color="#7f8c8d"
        )
        back_btn.pack(pady=20, padx=20, fill="x")

    def on_hover_enter(self, event):
        event.widget.configure(fg_color=self.colors['primary_dark'])

    def on_hover_leave(self, event):
        event.widget.configure(fg_color=self.colors['primary'])

class DepthLimitDialog(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Enter Depth Limit")
        self.geometry("300x200")
        
        self.result = None
        
        ctk.CTkLabel(
            self,
            text="Enter Depth Limit:",
            font=("Helvetica", 16)
        ).pack(pady=20)
        
        self.entry = ctk.CTkEntry(
            self,
            font=("Helvetica", 14),
            width=200
        )
        self.entry.pack(pady=10)
        
        ctk.CTkButton(
            self,
            text="Confirm",
            command=self.confirm,
            font=("Helvetica", 14)
        ).pack(pady=20)
        
        self.transient(parent)
        self.grab_set()
        parent.wait_window(self)
        
    def confirm(self):
        try:
            self.result = int(self.entry.get())
            self.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernAlgorithmGUI(root)
    root.mainloop()