import pygame
from Sudoku_UI import *

# check new value in row, column and grid
def isValid(grid, x, y, val):
    for i in range(9):
        if grid[x][i] == val: return False
        if grid[i][y] == val: return False
    
    start_row = x - x % 3
    start_col = y - y % 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == val:
                return False
    
    return True
        
def backtrack_solve(grid, row, col):
    if row == 8 and col == 9: 
        return True

    if col == 9: 
        col = 0
        row += 1

    if grid[row][col] > 0: return backtrack_solve(grid, row, col + 1)
    for i in range(1, 10):
        if isValid(grid, row, col, i):         
            grid[row][col] = i 
            draw_board(grid)
            pygame.display.update()
            pygame.time.delay(20)

            if backtrack_solve(grid, row, col + 1): return True
            grid[row][col] = 0

            draw_board()
            pygame.display.update()
            pygame.time.delay(50)
    return False

# grid = [[0] * 9 for _ in range(9)]

# grid[0][0] = 1
# grid[0][1] = 1
# backtrack_solve(grid, 0, 0)
# for i in range(9):
#     print(grid[i])
    
