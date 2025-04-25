# Pizza File
import pygame

# Basic Setup
pygame.init()
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class pizza():

    def __init__(self, num=None, cheese=None, sauce=None, toppings=None):
        self.num = num
        self.cheese = cheese
        self.sauce = sauce
        self.toppings = toppings

    def draw_pizza(self, x, y, radius):
        item = pygame.draw.circle(screen, (220, 200, 100), (x, y), radius)
        return item

    def add_topping(self, cheese=None, sauce=None, toppings=None):
        if cheese != None:
            self.cheese = cheese
        if sauce != None:
            self.sauce = sauce
        if toppings != None:
            self.toppings.append(toppings)
        self.draw_pizza()
