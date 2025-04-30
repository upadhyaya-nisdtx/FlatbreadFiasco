# Pizza File
import pygame

# Basic Setup
pygame.init()
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class pizza():

    def __init__(self, num=None, cheese=None, sauce=None):
        self.num = num
        self.cheese = cheese
        self.sauce = sauce
        self.toppings = []
        self.x = WIDTH * .66
        self.y = HEIGHT *.67
        self.radius = 150

    def draw_pizza(self):
        available_items = []
        available_items += pygame.draw.circle(screen, (220, 190, 100), (self.x, self.y), self.radius)
        if self.sauce:
            available_items += pygame.draw.circle(screen, (255, 100, 100), (self.x, self.y), self.radius * .9)
        if self.cheese:
            available_items += pygame.draw.circle(screen, (255, 220, 100), (self.x, self.y), self.radius * .85)
        if "pepperoni" in self.toppings:
            available_items += pygame.draw.circle(screen, (255, 50, 50), (self.x*.9, self.y*.9), self.radius * .1)
            available_items += pygame.draw.circle(screen, (255, 50, 50), (self.x * .95, self.y * 1.15), self.radius * .1)
            available_items += pygame.draw.circle(screen, (255, 50, 50), (self.x, self.y), self.radius * .1)
            available_items += pygame.draw.circle(screen, (255, 50, 50), (self.x*1.1, self.y*1.05), self.radius * .1)
            available_items += pygame.draw.circle(screen, (255, 50, 50), (self.x * 1.05, self.y * .85), self.radius * .1)
        if "mushroom" in self.toppings:
            pass
        if "onion" in self.toppings:
            pass
        if "pineapple" in self.toppings:
            pass
        return available_items

    def add_topping(self, cheese=False, sauce=False, toppings=None):
        if cheese:
            self.cheese = cheese
        if sauce:
            self.sauce = sauce
        if toppings != None:
            self.toppings.append(toppings)
        self.draw_pizza()

    def change_position(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius