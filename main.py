from sudoku_board import SudokuBoard

sudoku_board = SudokuBoard()

print("\n\nBEFORE SOLVING ...")
print("\n\n")
sudoku_board.print_board()

print("\n\n\nAFTER SOLVING ...")
print("\n\n")

sudoku_board.solve_graph_coloring(m=9)
sudoku_board.print_board()