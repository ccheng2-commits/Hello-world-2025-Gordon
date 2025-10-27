## For this exercise, I attempted to build a simple Snake Game using pygame.
##I started by installing the library, then learned how to control movements through keyboard inputs.
##The main mechanic is that when the snake “eats” food, it grows longer.
##Finally, I used pygame’s drawing functions to render blocks on the screen. （not completed yet）


import pygame
import sys
import random

pygame.init()

# --- Game Settings ---
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
SNAKE_SIZE = 20
SNAKE_SPEED = 10 

BACKGROUND_COLOR_BLACK = (0, 0, 0)
SNAKE_COLOR_GREEN = (0, 255, 0)
FOOD_COLOR_RED = (255, 0, 0)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("The snake Game!")

clock = pygame.time.Clock()

snake_body = [ [300, 200], [280, 200], [260, 200] ]

snake_change_x = SNAKE_SIZE
snake_change_y = 0

# --- Food Variables ---
max_grid_x = WINDOW_WIDTH // SNAKE_SIZE
max_grid_y = WINDOW_HEIGHT // SNAKE_SIZE
food_x = random.randint(0, max_grid_x - 1) * SNAKE_SIZE
food_y = random.randint(0, max_grid_y - 1) * SNAKE_SIZE

# --- The Main Game Loop ---
game_is_running = True
while game_is_running:
    
    # --- 1. Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False
        
        if event.type == pygame.KEYDOWN:
            # 
            if event.key == pygame.K_LEFT:
                snake_change_x = -SNAKE_SIZE
                snake_change_y = 0
            elif event.key == pygame.K_RIGHT:
                snake_change_x = SNAKE_SIZE
                snake_change_y = 0
            elif event.key == pygame.K_UP:
                snake_change_x = 0
                snake_change_y = -SNAKE_SIZE
            elif event.key == pygame.K_DOWN:
                snake_change_x = 0
                snake_change_y = SNAKE_SIZE

    # --- 2. Game Logic ---
    
    # (A) Calculate the position of the "new snake head"
    # Head = Old Head (snake_body[0]) + Direction (snake_change)
    current_head = snake_body[0] # [0] is the "first item" in the list
    new_head_x = current_head[0] + snake_change_x
    new_head_y = current_head[1] + snake_change_y
    new_head = [new_head_x, new_head_y]

    # (B) "Insert" the "new head" at the "front" of the list (position 0)
    snake_body.insert(0, new_head)

    # (C) Check if the snake ate the food
    #     We check if the "new head" is "equal to" the food's position
    if new_head_x == food_x and new_head_y == food_y:
        print("Ate it! Getting longer!")
        
        # Respawn the food
        food_x = random.randint(0, max_grid_x - 1) * SNAKE_SIZE
        food_y = random.randint(0, max_grid_y - 1) * SNAKE_SIZE
        
       
    
    else:
       
        snake_body.pop()

    # --- 3. Drawing ---
    screen.fill(BACKGROUND_COLOR_BLACK)
    
    # 【Draw the snake】
    # to "iterate" (go through) "each segment" of the snake's body and draw it
    for block in snake_body:
        # block will be [300, 200], then [280, 200], ...
        block_x = block[0]
        block_y = block[1]
        block_rect = pygame.Rect(block_x, block_y, SNAKE_SIZE, SNAKE_SIZE)
        pygame.draw.rect(screen, SNAKE_COLOR_GREEN, block_rect)
    
    # (Draw the food)
    food_rect = pygame.Rect(food_x, food_y, SNAKE_SIZE, SNAKE_SIZE)
    pygame.draw.rect(screen, FOOD_COLOR_RED, food_rect)

    # 4. Update the screen & control the speed
    pygame.display.flip()
    clock.tick(SNAKE_SPEED)

# --- Game Over ---
pygame.quit()
sys.exit()