import pygame
import Backtrack_solve
import Genetic_solve
import random

pygame.font.init()
random.seed()
screen = pygame.display.set_mode((700, 700))

square_len = 500/9

## some global var for color and position
# box's coordinate , x = pos[0], y = pos[1]
pos = (0,0)
x = 0
y = 0

# color
screen.fill((62, 168, 247))
BGCOLOR = (62, 168, 247)
TEXT_BG_COLOR = (88,210,53)
TEXT_COLOR = (255,255,255)

global BT_SOLVE_SURF, BT_SOLVE_RECT, GA_SOLVE_SURF, GA_SOLVE_RECT, NEW_GEN_SURF, NEW_GEN_RECT



# flag to check when to redraw board
border_flag = 0 # border a box
value_flag = 0  # value on box
solve_flag = 0  # solve sudoku


# initialize a temp sudoku board
grid = [[0] * 9 for _ in range(9)]

print(grid)

#font
text_font = pygame.font.SysFont("arial", 20)

def get_coor(pos):
    global x,y
    x = pos[0]//square_len
    y = pos[1]//square_len

# draw sudoku board 9x9
def draw_board(grid_temp = [[]]):
    global grid
    if len(grid_temp) != 1: grid = grid_temp
    #print(grid)
    for i in range(9):
        for j in range(9):
            # draw pink board :D
            pygame.draw.rect(screen,(213,102,90), (i * square_len, j * square_len, square_len + 1, square_len + 1))
            if grid[i][j] != 0:
                value_text = text_font.render(str(grid[i][j]), 1, (0,0,0))    
                screen.blit(value_text, (i * square_len + 23, j * square_len + 15))

    for i in range(10):
        line_thick = 1
        if i % 3 == 0:
            line_thick = 5        
        pygame.draw.line(screen,(120,5,100),(0, square_len * i),(500, square_len*i), line_thick)
        pygame.draw.line(screen,(120,5,100),(square_len * i, 0),(square_len*i, 500), line_thick)
    
    screen.blit(GA_SOLVE_SURF, GA_SOLVE_RECT)
    screen.blit(BT_SOLVE_SURF, BT_SOLVE_RECT)
    screen.blit(NEW_GEN_SURF, NEW_GEN_RECT)

# border a cell when clicked
def draw_box_border():    
    if x>=9 or y >=9: 
        return
    pygame.draw.line(screen,(255,255,0),(x * square_len, y * square_len), ((x + 1) * square_len, y * square_len), 5)
    pygame.draw.line(screen,(255,255,0),(x * square_len, (y + 1) * square_len), ((x + 1) * square_len, (y + 1) * square_len), 5)
    pygame.draw.line(screen,(255,255,0),(x * square_len, y * square_len), (x * square_len, (y + 1) * square_len), 5)
    pygame.draw.line(screen,(255,255,0),((x + 1) * square_len, y * square_len), ((x + 1) * square_len, (y + 1) * square_len), 5)

# return text_rendered and its topleft coordinates
def makeText(text, color, bgcolor, top, left):
    # create the Surface and Rect objects for some text.
    textSurf = text_font.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)

def gen_new_board():
    global grid    
    grid = [[0]*9 for _ in range(9)]
    for i in range(9):
        col = random.randint(0,8)
        val = random.randint(1,9)
        if Backtrack_solve.isValid(grid, i, col, val):
            grid[i][col] = val 
        
    #print(grid)
    return

#check if mouse position is on game's option
def checkOption():
    if BT_SOLVE_RECT.collidepoint(pos):
        Backtrack_solve.backtrack_solve(grid, 0, 0)
    elif GA_SOLVE_RECT.collidepoint(pos):
        Genetic_solve.genetic_solve(grid)
    elif NEW_GEN_RECT.collidepoint(pos):
        gen_new_board()
    border_flag = 0
    bt_solve_flag = 0
    ga_solve_flag = 0
    return

# draw number on cell
def draw_value(val, x, y, grid):
    value_text = text_font.render(str(val), 1, (0,0,0))    
    screen.blit(value_text, (x * square_len + 23, y * square_len + 15))
    grid[int(x)][int(y)] = val




NEW_GEN_SURF, NEW_GEN_RECT = makeText("New Game", TEXT_COLOR, TEXT_BG_COLOR, 570, 610)
BT_SOLVE_SURF, BT_SOLVE_RECT= makeText("Backtrack Solve", TEXT_COLOR, TEXT_BG_COLOR, 570, 570)
GA_SOLVE_SURF, GA_SOLVE_RECT= makeText("Genetic Solve", TEXT_COLOR, TEXT_BG_COLOR, 570, 530)

if __name__ == '__main__':  
    # game option
    while True:
        draw_board()    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                get_coor(pos)
                checkOption()            
                border_flag = 1            
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                if event.key == pygame.K_1: value_flag = 1
                if event.key == pygame.K_2: value_flag = 2
                if event.key == pygame.K_3: value_flag = 3
                if event.key == pygame.K_4: value_flag = 4
                if event.key == pygame.K_5: value_flag = 5
                if event.key == pygame.K_6: value_flag = 6
                if event.key == pygame.K_7: value_flag = 7
                if event.key == pygame.K_8: value_flag = 8
                if event.key == pygame.K_9: value_flag = 9

                if event.key == pygame.K_s: solve_flag = 1
                    

        if border_flag: draw_box_border()

        if value_flag: 
            draw_value(value_flag, x, y, grid)
            value_flag = 0

        if solve_flag:
            Backtrack_solve.backtrack_solve(grid, 0, 0)
            bt_solve_flag = 0
        
        pygame.display.update()
            