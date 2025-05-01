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
        self.y = HEIGHT *.445
        self.radius = 150

    def draw_pizza(self):
        available_items = []
        available_items += pygame.draw.circle(screen, (220, 190, 100), (self.x, self.y), self.radius)
        if self.sauce:
            available_items += pygame.draw.circle(screen, (255, 100, 100), (self.x, self.y), self.radius * .9)
        if self.cheese:
            available_items += pygame.draw.circle(screen, (255, 220, 100), (self.x, self.y), self.radius * .85)
        if "pepperoni" in self.toppings:
            available_items += screen.blit(pygame.image.load("graphics/pepperoni.png"), (self.x * .87, self.y * .8))
        if "mushroom" in self.toppings:
            available_items += screen.blit(pygame.image.load("graphics/mushroom.png"), (self.x *.87, self.y*.8))
        if "onion" in self.toppings:
            available_items += screen.blit(pygame.image.load("graphics/onion.png"), (self.x*.87, self.y*.8))
        if "pineapple" in self.toppings:
            available_items += screen.blit(pygame.image.load("graphics/pineapple.png"), (self.x*.87, self.y*.8))
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