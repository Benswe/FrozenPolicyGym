import random

class GridWorldEnv:
    def __init__(self, grid=None, start_state=0, gamma=0.99, is_slippery=True):
        if grid is None:
            grid = [
                "SFFF",
                "FHFH",
                "FFFH",
                "HFFG"
            ]
        self.grid = grid 
        self.n_rows = len(grid)
        self.n_cols = len(grid[0])

        self.states = list(range(self.n_rows * self.n_cols))
        self.actions = ["LEFT", "RIGHT", "UP", "DOWN"]

        self.start_state = start_state
        self.state = start_state
        self.gamma = gamma
        self.is_slippery = is_slippery

        self.terminal_states = self.get_terminal_states()
    def state_to_pos(self, state):
        """
        Convert integer state into (row, col)
        """
        row = state // self.n_cols
        col = state % self.n_cols
        return row, col
    
    def pos_to_state(self, row, col):
        """
        Convert (row, col) back into integer state.
        
        """
        state = (row * self.n_cols) + col 
        return state

    def get_tile(self, state):
        """
        Return the character at a given state

        Example:
        "S", "F", "H", or "G"
        """
        row, col = self.state_to_pos(state)
        return self.grid[row][col]

    def find_start_state(self):
        """
        Find where the "S" tile i.
        
        """
        for s in self.states:
            tile = self.get_tile(s)
            if tile == "S":
                return s
            
        raise ValueError("No start state S found!")
    
    def get_terminal_states(self):
        """
        Returns a list of all terminal states.

        Terminal states are:
        - holes: "H"
        - goal: "G""

        """
        terminal_states = []
        for s in self.states:
            tile = self.get_tile(s)
            if tile in ["H", "G"]:
                terminal_states.append(s)
        return terminal_states
                
            
            
