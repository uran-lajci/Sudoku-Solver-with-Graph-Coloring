"""
This Python code implements a SudokuConnections class that generates a graph representation 
of a Sudoku puzzle. The class utilizes a Graph object from the 'graph' module to create nodes 
and establish connections based on the constraints of the Sudoku game. The graph represents 
the relationships between cells in the puzzle grid. The SudokuConnections class initializes a 
graph and creates nodes corresponding to each cell in a 9x9 Sudoku grid. It then connects the 
nodes according to Sudoku rules, such as ensuring that each row, column, and 3x3 block contains 
unique values from 1 to 9. The class provides methods for accessing and manipulating the graph.
The 'test_connections' function demonstrates the usage of the SudokuConnections class by creating 
an instance and performing various operations on the graph, such as printing all node IDs, performing 
depth-first search (DFS) and breadth-first search (BFS), and displaying the connections of each node.
This code serves as a foundation for building Sudoku-solving algorithms that can utilize graph traversal 
and constraint propagation techniques.
"""


from graph import Graph


class SudokuConnections:

    def __init__(self):  # constructor
        self.graph = Graph()  # Graph Object
        self.rows, self.cols = 9, 9
        self.total_blocks = self.rows*self.cols  # 81
        self.generate_graph()  # Generates all the nodes
        self.connect_edges()  # connects all the nodes acc to sudoku constraints
        self.all_ids = self.graph.get_all_nodes_ids()  # storing all the ids in a list

    def generate_graph(self):
        for idx in range(1, self.total_blocks+1):
            _ = self.graph.add_node(idx)

    def connect_edges(self):
        matrix = self.get_grid_matrix()
        for row in range(9):
            for col in range(9):
                head = matrix[row][col]  # id of the node
                connections = self.get_connections(matrix, row, col)
                self.connect_nodes(head, connections)

    def connect_nodes(self, head, connections):
        for connection_type in connections:
            for node in connections[connection_type]:
                self.graph.add_edge(src=head, dst=node)

    def get_connections(self, matrix, rows, cols):
        return {
            'rows': [matrix[rows][c] for c in range(cols + 1, 9)],
            'cols': [matrix[r][cols] for r in range(rows + 1, 9)],
            'blocks': [matrix[rows // 3 * 3 + r][cols // 3 * 3 + c] for r in [0, 1, 2] for c in [0, 1, 2] if r != rows % 3 or c != cols % 3]
        }

    def get_grid_matrix(self):
        matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for rows in range(9):
            for cols in range(9):
                matrix[rows][cols] = rows*9 + cols + 1
        return matrix
