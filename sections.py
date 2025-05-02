# Stations
import pygame
import customer
import pizza
import generate_order

# Basic Setup
pygame.init()
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Title Graphics
title_screen_image = pygame.image.load("graphics/title_screen.png")
new_button = pygame.image.load("graphics/new_game_button.png")
new_button = pygame.transform.scale(new_button, (300, 300))
load_button = pygame.image.load("graphics/load_game_button.png")
load_button = pygame.transform.scale(load_button, (300, 300))

def title():
    global new_button, load_button
    screen.fill((0, 0, 0, 0))
    screen.blit(title_screen_image, (0, 0))
    screen.blit(new_button, (WIDTH*.03, HEIGHT//2))
    screen.blit(load_button, (WIDTH*.73, HEIGHT//2))
    return new_button, load_button

# Toggle Graphics
toggle_bar = pygame.image.load("graphics/top_bar.png")
order_toggle = pygame.image.load("graphics/order_screen_toggle.png")
order_toggle = pygame.transform.scale(order_toggle, (100, 100))
create_toggle = pygame.image.load("graphics/make_screen_toggle.png")
create_toggle = pygame.transform.scale(create_toggle, (100, 100))
bake_toggle = pygame.image.load("graphics/bake_screen_toggle.png")
bake_toggle = pygame.transform.scale(bake_toggle, (100, 100))
deliver_toggle = pygame.image.load("graphics/deliver_screen_toggle.png")
deliver_toggle = pygame.transform.scale(deliver_toggle, (100, 100))
settings_toggle = pygame.image.load("graphics/settings_toggle.png")
settings_toggle = pygame.transform.scale(settings_toggle, (100, 100))
def toggle():
    screen.blit(toggle_bar, (0, -150))
    screen.blit(order_toggle, (WIDTH*.3, 0))
    screen.blit(create_toggle, (WIDTH*.4, 0))
    screen.blit(bake_toggle, (WIDTH*.5, 0))
    screen.blit(deliver_toggle, (WIDTH*.6, 0))
    screen.blit(settings_toggle, (WIDTH * .8, 0))
    return order_toggle, create_toggle, bake_toggle, deliver_toggle, settings_toggle

# Order Graphics
order_screen_image = pygame.image.load("graphics/order_screen.jpg")
def order_screen(customer_list_1, customer_list_2):
    screen.fill((0, 0, 0, 0))
    screen.blit(order_screen_image, (0, 0))
    customer.place_customers(customer_list_1, customer_list_2)

order_event_image = pygame.image.load("graphics/order_event.png")
order_event_font = pygame.font.SysFont("Arial", 50)
order_event_font2 = pygame.font.SysFont("Arial", 25)
def order_event(customer):
    screen.fill((0, 0, 0, 0))
    screen.blit(order_event_image, (0, -10))
    screen.blit(customer.image, (WIDTH*.1, HEIGHT*.05))
    customer.image = pygame.transform.scale(customer.image, (474, 1095))
    # Fix Whatever the hell this is
    try:
        customer.order.image = pygame.transform.scale(customer.order.image, (400, 700))
    except:
        customer.order = generate_order.order()
        customer.order.image = pygame.transform.scale(customer.order.image, (400, 700))
    screen.blit(customer.order.image, (WIDTH*.6, HEIGHT*.05))
    # Order Items
    num_txtsurf = order_event_font.render("Order " + str(generate_order.order.orders), True, (0, 0, 0))
    sauce_txtsurf = order_event_font.render(customer.order.sauce, True, (0, 0, 0))
    cheese_txtsurf = order_event_font.render(customer.order.cheese, True, (0, 0, 0))
    temp_string = ", ".join(customer.order.toppings)
    toppings_txtsurf = order_event_font2.render(temp_string, True, (0, 0, 0))
    slices_txtsurf = order_event_font.render("Slices: " + str(customer.order.slices), True, (0, 0, 0))
    screen.blit(num_txtsurf, (WIDTH * .65, HEIGHT * .1))
    screen.blit(sauce_txtsurf, (WIDTH*.65, HEIGHT*.45))
    screen.blit(cheese_txtsurf, (WIDTH * .65, HEIGHT * .6))
    screen.blit(toppings_txtsurf, (WIDTH * .65, HEIGHT * .3))
    screen.blit(slices_txtsurf, (WIDTH * .65, HEIGHT * .75))
    return customer

# Make Graphics
make_screen_image = pygame.image.load("graphics/make_screen.png")
gen_pizza_toggle = pygame.image.load("graphics/make_screen_toggle.png")
gen_pizza_toggle = pygame.transform.scale(gen_pizza_toggle, (100, 100))
cheese_button = pygame.image.load("graphics/cheese_button.png")
sauce_button = pygame.image.load("graphics/sauce_button.png")
pepperoni_button = pygame.image.load("graphics/pepperoni_button.png")
mushroom_button = pygame.image.load("graphics/mushroom_button.png")
onion_button = pygame.image.load("graphics/onion_button.png")
pineapple_button = pygame.image.load("graphics/pineapple_button.png")
def make_screen():
    screen.fill((0, 0, 0, 0))
    screen.blit(make_screen_image, (0, 0))
    screen.blit(gen_pizza_toggle, (WIDTH * .75, HEIGHT * .4))
    screen.blit(cheese_button, (WIDTH*.09, HEIGHT*.53))
    screen.blit(sauce_button, (WIDTH * .18, HEIGHT * .53))
    screen.blit(pepperoni_button, (WIDTH*.27, HEIGHT*.53))
    screen.blit(mushroom_button, (WIDTH*.09, HEIGHT*.67))
    screen.blit(onion_button, (WIDTH*.18, HEIGHT*.67))
    screen.blit(pineapple_button, (WIDTH*.27, HEIGHT*.67))

    return gen_pizza_toggle, cheese_button, sauce_button, pepperoni_button, mushroom_button, onion_button, pineapple_button


# Bake Graphics
bake_screen_image = pygame.image.load("graphics/bake_screen.png")
def bake_screen(current_pizza, selected=False):
    screen.fill((0, 0, 0, 0))
    screen.blit(bake_screen_image, (0, 0))
    if not selected:
        try:
            current_pizza.change_position(WIDTH*0.08, HEIGHT*.7, 200)
        except:
            pass
    return current_pizza
deliver_screen_image = pygame.image.load("graphics/deliver_screen.png")
# Deliver Graphics
def deliver_screen():
    screen.fill((0, 0, 0, 0))
    screen.blit(deliver_screen_image, (0, 0))

# Settings Graphics
settings_screen_image = pygame.image.load("graphics/settings_screen.png")
quit_title = pygame.font.SysFont("Arial", 50)
quit_txtsurf = quit_title.render("Quit", True, (0, 0, 0))
quit_button = pygame.Rect((WIDTH*.05, HEIGHT*.25, 50, 50))
def settings_screen():
    screen.fill((0, 0, 0, 0))
    screen.blit(settings_screen_image, (0, 50))
    screen.blit(quit_txtsurf, (WIDTH*.1, HEIGHT*.25))
    pygame.draw.rect(screen, (255, 255, 255, 255), quit_button, 100, 100)
    return quit_button