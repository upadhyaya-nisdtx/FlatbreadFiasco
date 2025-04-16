# Customer File
import pygame
from generate_order import order

# Basic Setup
pygame.init()
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class customer():
    def __init__(self):
        self.image = pygame.image.load("graphics/customer.png")
        self.order = None
        self.pos = (WIDTH*.2, HEIGHT*.3)

    def set_x(self, x):
        self.pos = (WIDTH*.2 + x, HEIGHT*.3)
        screen.blit(self.image, self.pos)
    def set_order(self):
        self.order = order()




