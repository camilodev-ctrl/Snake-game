import pygame 
import random as rd

pygame.init()

#Screen setup
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("snake game")

#Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#initial snake position
dx, dy = 0, 0 

#initializer snake and food 
snake = [(100, 100), (80,100), (60,100)]
food = (rd.randrange(0, WIDTH, CELL_SIZE), rd.randrange(0, HEIGHT, CELL_SIZE))

#timer for snake movement
clock = pygame.time.Clock()




