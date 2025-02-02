import pygame
import random


pygame.init()

#settings
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

#Initial direction
dx, dy = CELL_SIZE, 0

#initializer snake and food
snake = [(100, 100), (80, 100), (60, 100)]
food = (random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE, random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE)

#game loop
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -CELL_SIZE
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, CELL_SIZE
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -CELL_SIZE, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = CELL_SIZE, 0
    
    #snake movement
    new_head = (snake[0][0] + dx, snake[0][1] + dy)
    print(f"Snake head: {new_head}, Food: {food}")  # Depuración
    
    #border collision
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        running = False
    
    #snake collision
    if new_head in snake:
        running = False
    
    snake.insert(0, new_head)
    
    #snake eat food
    if new_head == food:
        food = (random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE, random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE)
    else:
        snake.pop()
    
    #draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, WHITE, (segment[0], segment[1], CELL_SIZE, CELL_SIZE), 1)
    
    #draw food
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, WHITE, (food[0], food[1], CELL_SIZE, CELL_SIZE), 1)
    
    pygame.display.update()
    clock.tick(10)

pygame.quit()







