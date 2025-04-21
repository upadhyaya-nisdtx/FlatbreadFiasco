# Pizza File
import pygame

# Basic Setup
pygame.init()
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class pizza():

    def __init__(self, num, cheese, sauce, toppings):
        self.num = num
        self.cheese = cheese
        self.sauce = sauce
        self.toppings = toppings
        self.draw = [pygame.draw.circle(screen, (200, 200, 0), (x, y), radius)]

    def draw_pizza(self):
        return self.draw

    def add_topping(self, cheese=None, sauce=None, toppings=None):
        if cheese != None:
            self.cheese = cheese
        if sauce != None:
            self.sauce = sauce
        if toppings != None:
            self.toppings.append(toppings)
        self.draw_pizza()
