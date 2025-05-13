# Order file
import random
import pygame

# Basic Setup
pygame.init()
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Lists for order generation
toppings = ["Pepperoni", "Mushroom", "Onion", "Pineapple"]
sauces = ["Tomato Sauce", "Alfredo Sauce", "BBQ Sauce"]
cheeses = ["Mozzarella", "Parmesan", "Provolone", "Cheddar"]

class order():
    """
    Creates an order
    ----
    __init__(): constructor. Randomly generates an order based on lists.
    orders: keeps track of the number of orders made
    """
    orders = 0

    def __init__(self):
        num = random.randint(0, 4)
        order.orders += 1
        self.order_num = order.orders
        temp_list = []
        for i in range(num):
            temp_item = random.choice(toppings)
            if temp_item not in temp_list:
                temp_list.append(temp_item)
        self.toppings = temp_list
        self.sauce = random.choice(sauces)
        self.cheese = random.choice(cheeses)
        self.slices = random.randint(2, 8)
        self.image = pygame.image.load("graphics/ticket.png")