# Customer File
import os
import pygame
from generate_order import order
import random

# Basic Setup
pygame.init()
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def place_customers(customer_list_1, customer_list_2):
    """
    Places customers based on the list they are in
    ----
    returns: None
    """
    for item in customer_list_1:
        screen.blit(item.image, item.pos)
    for item in customer_list_2:
        screen.blit(item.image, item.pos)

class customer():
    """
    Creates a customer object
    ----
    __init__(): constructor.
    change_index: changes index value
    index: tracks position in dir_list
    dir_list: list of customer graphics
    set_x(): changes x value of ticket image
    set_y(): changes y value of ticket image
    set_order(): sets order if there is no order
    """
    index = 0
    dir_list = os.listdir("customer_graphics/")
    random.shuffle(dir_list)

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
