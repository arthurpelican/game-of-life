import pygame
import random as rd
pygame.init()

WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of life                                                                                                                  SPACE to start simulation")

FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def reset_grid(grid) :
    for v in grid :
        grid[v] = False

def draw(win, grid, size, selected_cell = None) :  

    for v in grid :
        pygame.draw.rect(win, BLACK, (size * v[0], size * v[1], size, size))
        if not grid[v] :
            pygame.draw.rect(win, WHITE, (size * v[0] + 1, size * v[1] + 1, size - 2, size - 2))

    if selected_cell != None :
        pygame.draw.rect(win, RED, (size * selected_cell[0], size * selected_cell[1], size, size))
        if not grid[selected_cell] :
            pygame.draw.rect(win, WHITE, (size * selected_cell[0] + 1, size * selected_cell[1] + 1, size - 2, size - 2))
        else :
            pygame.draw.rect(win, BLACK, (size * selected_cell[0] + 1, size * selected_cell[1] + 1, size - 2, size - 2))

    pygame.display.update()
   
def creating_grid() :
    running = True
    clock = pygame.time.Clock()
    size = 25

    grid = {}
    for x in range(WIDTH // size + 1) :
        for y in range(HEIGHT // size + 1) :
            grid[(x, y)] = False

    while running :
        clock.tick()

        mouse_pos = pygame.mouse.get_pos()
        events = pygame.event.get()

        selected_cell = (mouse_pos[0] // size, mouse_pos[1] // size)

        for event in events:
            if event.type == pygame.QUIT :
                running = False
                return False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE :
                    return grid
            if event.type == pygame.MOUSEBUTTONUP :
                grid[selected_cell] = not grid[selected_cell]

        draw(WIN, grid, size, selected_cell)

def evolution(grid) :
    running = True
    clock = pygame.time.Clock()
    size = 25

    while running :
        clock.tick()

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT :
                running = False
                return False

        draw(WIN, grid, size)

        new_grid = {}

        keys = grid.keys()

        for v in grid :
            x = v[0]
            y = v[1]
            neighbors = 0
            cells = {(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)}
            for cell in cells :
                if cell in keys :
                    if grid[cell] : 
                        neighbors += 1
            if neighbors == 3 :
                new_grid[v] = True
            elif neighbors == 2 :
                new_grid[v] = grid[v]
            else :
                new_grid[v] = False
        
        grid = new_grid
        pygame.time.delay(250)

if __name__ == "__main__" :
    grid = creating_grid()
    if grid != False :
        evolution(grid)