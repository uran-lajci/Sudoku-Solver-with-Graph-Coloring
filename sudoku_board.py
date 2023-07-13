"""
This module defines a SudokuBoard class that represents a Sudoku puzzle. The SudokuBoard class 
contains methods to initialize the board, print the board, check if a cell is blank, check if a 
number can be placed at a certain position, and solve the Sudoku puzzle using graph coloring. 
The SudokuBoard class uses the SudokuConnections class, which is defined in a separate module, 
to represent the connections between cells in the Sudoku puzzle. The test function at the end of 
the module creates a SudokuBoard object and solves the Sudoku puzzle.
"""


from sudoku_connections import SudokuConnections


class SudokuBoard:

    def __init__(self):
        self.board = self.get_board()
        self.sudoku_graph = SudokuConnections()
        self.mapped_grid = self.get_mapped_matrix()

    def get_mapped_matrix(self):
        matrix = [[0 for cols in range(9)]
                  for rows in range(9)]

        count = 1
        for rows in range(9):
            for cols in range(9):
                matrix[rows][cols] = count
                count += 1
        return matrix

    def get_board(self):
        return [
            [0, 0, 0, 4, 0, 0, 0, 0, 0],
            [4, 0, 9, 0, 0, 6, 8, 7, 0],
            [0, 0, 0, 9, 0, 0, 1, 0, 0],
            [5, 0, 4, 0, 2, 0, 0, 0, 9],
            [0, 7, 0, 8, 0, 4, 0, 6, 0],
            [6, 0, 0, 0, 3, 0, 5, 0, 2],
            [0, 0, 1, 0, 0, 7, 0, 0, 0],
            [0, 4, 3, 2, 0, 0, 6, 0, 5],
            [0, 0, 0, 0, 0, 5, 0, 0, 0]
        ]

    def print_board(self):
        print("    1 2 3     4 5 6     7 8 9")
        for i in range(len(self.board)):
            if i % 3 == 0:  # and i != 0:
                print("  - - - - - - - - - - - - - - ")

            for j in range(len(self.board[i])):
                if j % 3 == 0:  # and j != 0 :
                    print(" |  ", end="")
                if j == 8:
                    print(self.board[i][j], " | ", i+1)
                else:
                    print(f"{ self.board[i][j] } ", end="")
        print("  - - - - - - - - - - - - - - ")

    def is_blank(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == 0:
                    return (row, col)
        return None

    def is_valid(self, num, pos):
        for col in range(len(self.board[0])):
            if self.board[pos[0]][col] == num and pos[0] != col:
                return False

        for row in range(len(self.board)):
            if self.board[row][pos[1]] == num and pos[1] != row:
                return False

        x = pos[1]//3
        y = pos[0]//3

        for row in range(y*3, y*3+3):
            for col in range(x*3, x*3+3):
                if self.board[row][col] == num and (row, col) != pos:
                    return False

        return True

    def graph_coloring_initialize_color(self):
        """
        fill the already given colors
        """
        color = [0] * (self.sudoku_graph.graph.total_V+1)
        given = []  # list of all the ids whos value is already given. Thus cannot be changed
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] != 0:
                    # first get the idx of the position
                    idx = self.mapped_grid[row][col]
                    # update the color
                    # this is the main imp part
                    color[idx] = self.board[row][col]
                    given.append(idx)
        return color, given

    def solve_graph_coloring(self, m=9):
        color, given = self.graph_coloring_initialize_color()
        if self.graph_color_utility(m=m, color=color, v=1, given=given) is None:
            return False
        
        count = 1
        for row in range(9):
            for col in range(9):
                self.board[row][col] = color[count]
                count += 1
        return color

    def graph_color_utility(self, m, color, v, given):
        if v == self.sudoku_graph.graph.total_V + 1:
            return True
        
        for c in range(1, m+1):
            if self.is_safe_to_color(v, color, c, given) == True:
                color[v] = c
                if self.graph_color_utility(m, color, v+1, given):
                    return True
                
            if v not in given:
                color[v] = 0

    def is_safe_to_color(self, v, color, c, given):
        if v in given and color[v] == c:
            return True
        elif v in given:
            return False

        for i in range(1, self.sudoku_graph.graph.total_V+1):
            if color[i] == c and self.sudoku_graph.graph.is_neighbour(v, i):
                return False
        return True