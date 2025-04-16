# Order file
import random

toppings = ["Pepperoni", "Mushroom", "Onion", "Pineapple"]
sauces = ["Tomato Sauce", "Alfredo Sauce", "BBQ Sauce"]
cheeses = ["Mozzarella", "Parmesan", "Provolone", "Cheddar"]

class order():
    def __init__(self):
        num = random.randint(0, 4)
        temp_list = []
        for i in range(num):
            temp_item = random.choice(toppings)
            if temp_item not in temp_list:
                temp_list.append(temp_item)
        self.toppings = temp_list
        self.sauce = random.choice(sauces)
        self.cheese = random.choice(cheeses)