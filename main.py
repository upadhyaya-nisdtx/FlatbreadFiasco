# Main File
import pygame
import sections
from customer import customer, place_customers
from pizza import pizza

# Basic Setup
pygame.init()
run = True
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flatbread Fiasco!')
bg_music = pygame.mixer.Sound("audio/Double Polka.mp3")

### --- Graphics --- ###

# Cursor
pygame.mouse.set_visible(False)
cursor = pygame.image.load("graphics/pizza_cursor.png")
cursor = pygame.transform.scale(cursor, (35, 35))
click_sound = pygame.mixer.Sound("audio/click_tone")

# Visibility Variables
show_title = True
show_game = False
show_order = False
show_make = False
show_bake = False
show_deliver = False
show_settings = False
show_order_event = False

def visible_station(show_variable, boolean=True):
    global show_order, show_make, show_bake, show_deliver, show_settings, show_order_event
    show_order = False
    show_make = False
    show_bake = False
    show_deliver = False
    show_settings = False
    show_order_event = False
    show_variable = boolean
    return show_variable

# Misc
doorbell_sound = pygame.mixer.Sound("audio/doorbell.mp3")
toggles = sections.toggle()
quit_button = sections.settings_screen()
ordering_customers = []
waiting_customers = []
showing_customer = None
time_1 = 0
time_2 = 0
time_3 = 0
temp_customer = None
gen_pizza_toggle = sections.make_screen()
pizzas = []

def reset():
    global ordering_customers, waiting_customers, showing_customer, time_1, time_2, time_3, temp_customer, pizzas
    ordering_customers = []
    waiting_customers = []
    showing_customer = None
    time_1 = 0
    time_2 = 0
    time_3 = 0
    temp_customer = None
    pizzas = []

bg_music.play(loops=-1)
# Main Loop
while run:
    # Check Visibility
    if show_title:
        buttons = sections.title()
        time_1 = 0
        time_2 = 0
    elif show_game:
        # Time Check
        time_2 = pygame.time.get_ticks()
        if time_2 - time_1 >= 1000 and (len(ordering_customers) + len(waiting_customers)) <= 4:
            doorbell_sound.play()
            temp = customer()
            ordering_customers.append(temp)
            time_1 = pygame.time.get_ticks()
        if show_order:
            sections.order_screen(ordering_customers,waiting_customers)
            for i in range(len(ordering_customers)):
                ordering_customers[i].set_x(WIDTH*.2 + (i * 200))
            for i in range(len(waiting_customers)):
                waiting_customers[i].set_x(WIDTH*.2 + (i * 200))
        elif show_order_event:
            try:
                temp_customer = sections.order_event(item)
            except:
                temp_customer = sections.order_event(item)
            if time_2 - time_3 >= 3000:
                show_order = visible_station(show_order)
                temp_customer.image = pygame.transform.scale(temp_customer.image, (174, 395))
        elif show_make:
            gen_pizza_toggle = sections.make_screen()
            if len(pizzas) != 0:
                pizzas[0].draw_pizza(pizzas[-3], pizzas[-2], pizzas[-1])
        elif show_bake:
            sections.bake_screen()
        elif show_deliver:
            sections.deliver_screen()
        elif show_settings:
            quit_button = sections.settings_screen()
        if not show_order_event:
            toggles = sections.toggle()

    # Mouse Position
    pos = pygame.mouse.get_pos()
    screen.blit(cursor, (pos[0], pos[-1]))

    # Event Check
    for event in pygame.event.get():
        # Quit Check
        if event.type == pygame.QUIT:
            run = False
        # Mouse Click Check
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Sound
            click_sound.play()
            # If TITLE is visible
            if show_title:
                if buttons[0].get_rect(topleft=(WIDTH*.03, HEIGHT//2)).collidepoint(pos):
                    time_1 = pygame.time.get_ticks()
                    show_title = False
                    show_game = True
                    show_order = True
                elif buttons[1].get_rect(topleft=(WIDTH*.73, HEIGHT//2)).collidepoint(pos):
                    time_1 = pygame.time.get_ticks()
                    show_title = False
                    show_game = True
                    show_order = True
            # If GAME is visible
            if show_game:
                # Toggle Checks
                if toggles[0].get_rect(topleft=(WIDTH*.3, 0)).collidepoint(pos):
                    show_order = visible_station(show_order)
                elif toggles[1].get_rect(topleft=(WIDTH*.4, 0)).collidepoint(pos):
                    show_make = visible_station(show_make)
                elif toggles[2].get_rect(topleft=(WIDTH*.5, 0)).collidepoint(pos):
                    show_bake = visible_station(show_bake)
                elif toggles[3].get_rect(topleft=(WIDTH*.6, 0)).collidepoint(pos):
                    show_deliver = visible_station(show_deliver)
                elif toggles[4].get_rect(topleft=(WIDTH*.8, 0)).collidepoint(pos):
                    show_settings = visible_station(show_settings)
                # Settings Check
                if show_settings:
                    if quit_button.collidepoint(pos):
                        reset()
                        show_settings = visible_station(show_settings, False)
                        show_title = True
                # Customer Click Check
                elif show_order:
                    for item in ordering_customers:
                        if item.image.get_rect(topleft=item.pos).collidepoint(pos):
                            time_3 = pygame.time.get_ticks()
                            showing_customer = item
                            item.set_y(HEIGHT*.2 + HEIGHT *.3)
                            item.set_x(WIDTH*.2 + (len(ordering_customers) - 1) * 100)
                            waiting_customers.append(item)
                            ordering_customers.remove(item)
                            place_customers(ordering_customers, waiting_customers)
                            item.set_order()
                            temp_customer = sections.order_event(item)
                            show_order_event = visible_station(show_order_event)
                elif show_make:
                    if gen_pizza_toggle.get_rect(topleft=(WIDTH * .75, HEIGHT * .4)).collidepoint(pos) and len(pizzas) == 0:
                            pizzas.append(pizza())
                            pizzas+= [WIDTH * .66, HEIGHT *.67, 150]
                            pizzas[0].draw_pizza(pizzas[-3], pizzas[-2], pizzas[-1])

    # Display Update
    pygame.display.update()

# Quit
pygame.quit()