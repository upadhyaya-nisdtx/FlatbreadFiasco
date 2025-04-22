# Customer File
import os
import pygame
from generate_order import order

# Basic Setup
pygame.init()
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def place_customers(customer_list_1, customer_list_2):
    for item in customer_list_1:
        screen.blit(item.image, item.pos)
    for item in customer_list_2:
        screen.blit(item.image, item.pos)

class customer():
    index = 0
    dir_list = os.listdir("customer_graphics/")

    @classmethod
    def change_index(cls):
        cls.index += 1
        if cls.index >= len(cls.dir_list):
            cls.index = 0

    def __init__(self):
        self.image = pygame.image.load("customer_graphics/" + customer.dir_list[customer.index])
        customer.change_index()
        self.order = None
        self.pos = (WIDTH*.2, HEIGHT*.3)

    def set_x(self, x):
        self.pos = ( x, self.pos[-1])

    def set_y(self, y):
        self.pos = (self.pos[0], y)

    def set_order(self):
        if self.order != None:
            return
        self.order = order()




