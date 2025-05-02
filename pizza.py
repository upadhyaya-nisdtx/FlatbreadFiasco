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

    def draw_pizza(self, scale=200, pos=None, selected=False):
        available_items = []
        if pos != None and selected:
            available_items += pygame.draw.circle(screen, (220, 190, 100), (pos[0], pos[1]), self.radius)
        else:
            available_items += pygame.draw.circle(screen, (220, 190, 100), (self.x, self.y), self.radius)
        if self.sauce:
            if pos != None and selected:
                available_items += pygame.draw.circle(screen, (255, 100, 100), (pos[0], pos[1]), self.radius * .9)
            else:
                available_items += pygame.draw.circle(screen, (255, 100, 100), (self.x, self.y), self.radius * .9)
        if self.cheese:
            if pos != None and selected:
                available_items += pygame.draw.circle(screen, (255, 220, 100), (pos[0], pos[1]), self.radius * .85)
            else:
                available_items += pygame.draw.circle(screen, (255, 220, 100), (self.x, self.y), self.radius * .85)
        if "pepperoni" in self.toppings:
            temp = pygame.image.load("graphics/pepperoni.png")
            temp = pygame.transform.scale(temp, (scale, scale))
            if pos != None and selected:
                available_items += screen.blit(temp, (pos[0] - 120, pos[1] - 120))
            else:
                available_items += screen.blit(temp, (self.x - scale//2, self.y - scale//2))
        if "mushroom" in self.toppings:
            temp = pygame.image.load("graphics/mushroom.png")
            temp = pygame.transform.scale(temp, (scale, scale))
            if pos != None and selected:
                available_items += screen.blit(temp, (pos[0] - 120, pos[1] - 120))
            else:
                available_items += screen.blit(temp, (self.x - scale//2, self.y - scale//2))
        if "onion" in self.toppings:
            temp = pygame.image.load("graphics/onion.png")
            temp = pygame.transform.scale(temp, (scale, scale))
            if pos != None and selected:
                available_items += screen.blit(temp, (pos[0] - 120, pos[1] - 120))
            else:
                available_items += screen.blit(temp, (self.x - scale//2, self.y - scale//2))
        if "pineapple" in self.toppings:
            temp = pygame.image.load("graphics/pineapple.png")
            temp = pygame.transform.scale(temp, (scale, scale))
            if pos != None and selected:
                available_items += screen.blit(temp, (pos[0] - 120, pos[1] - 120))
            else:
                available_items += screen.blit(temp, (self.x - scale//2, self.y - scale//2))
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