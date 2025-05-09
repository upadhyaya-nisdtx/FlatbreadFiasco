# Main File
import pygame
import sections
from customer import customer, place_customers
from pizza import pizza
import generate_order

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
show_tutorial = False

def visible_station(show_variable, boolean=True):
    global show_order, show_make, show_bake, show_deliver, show_settings, show_order_event, show_tutorial
    show_order = False
    show_make = False
    show_bake = False
    show_deliver = False
    show_settings = False
    show_order_event = False
    show_tutorial = False
    show_variable = boolean
    return show_variable

# Misc
doorbell_sound = pygame.mixer.Sound("audio/doorbell.mp3")
toggles = sections.toggle()
quit_button, tut_button = sections.settings_screen()
ordering_customers = []
waiting_customers = []
showing_customer = None
customer_time = 2000
time_1 = 0
time_2 = 0
time_3 = 0
temp_customer = None
create_toggles = sections.make_screen()
current_pizza = None
pizza_list = []
selected = False
available_items = []
bake_x = WIDTH * .08
bake_y = HEIGHT * .7
invisible_surface = None
invisible_rect = None
invisible_surface_2 = None
invisible_rect_2 = None
deliver_items = []
invisible_rect_2 = None
invisible_surface_2 = None

"""
only allow 1 save file, override when making new save
def save(filename, 1, 2, 3):

        dictionary_save = {
            "filename": filename,
            "item1": 1,
            "item2": 2,
            "item3": 3
        }
        json_object = json.dumps(dictionary_save, indent=4)
        with open(filename, "w") as saved_file:
            saved_file.write(json_object)
"""
def reset():
    global ordering_customers, waiting_customers, showing_customer, time_1, time_2, time_3, temp_customer
    global current_pizza, pizza_list, selected, available_items, bake_x, bake_y, customer_time, invisible_surface
    global invisible_rect, deliver_items, invisible_rect_2, invisible_surface_2
    ordering_customers = []
    waiting_customers = []
    showing_customer = None
    time_1 = 0
    time_2 = 0
    time_3 = 0
    temp_customer = None
    current_pizza = None
    pizza_list = []
    selected = False
    available_items = []
    bake_x = WIDTH * .08
    bake_y = HEIGHT * .7
    customer_time = 2000
    invisible_surface = None
    invisible_rect = None
    invisible_surface_2 = None
    invisible_rect_2 = None
    deliver_items = []

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
        if time_2 - time_1 >= customer_time and (len(ordering_customers) + len(waiting_customers)) <= 4:
            doorbell_sound.play()
            temp = customer()
            ordering_customers.append(temp)
            time_1 = pygame.time.get_ticks()
            customer_time = 10000
        # Section Checks
        if show_order:
            selected = False
            sections.order_screen(ordering_customers,waiting_customers)
            for i in range(len(ordering_customers)):
                ordering_customers[i].set_x(WIDTH*.2 + (i * 200))
            for i in range(len(waiting_customers)):
                waiting_customers[i].set_x(WIDTH*.2 + (i * 200))
        elif show_order_event:
            temp_customer = sections.order_event(item)
            if time_2 - time_3 >= 3000:
                show_order = visible_station(show_order)
                temp_customer.image = pygame.transform.scale(temp_customer.image, (174, 395))
        elif show_make:
            selected = False
            create_toggles = sections.make_screen()
            if current_pizza != None:
                current_pizza.change_position(WIDTH * .66, WIDTH * .445, 150)
                current_pizza.base.move(WIDTH * .66, WIDTH * .445)
                current_pizza.base.radius = 150
                available_items = current_pizza.draw_pizza()
        elif show_bake:
            bake_items = sections.bake_screen(current_pizza, selected)
            current_pizza = bake_items[0]
            invisible_surface = bake_items[1]
            invisible_rect = bake_items[2]
            if current_pizza != None:
                if selected:
                    bake_x = pos[0]
                    bake_y = pos[1]
                current_pizza.change_position(bake_x, bake_y, 200)
                current_pizza.base.move(bake_x, bake_y)
                current_pizza.base.radius = 200
                available_items = current_pizza.draw_pizza()
        elif show_deliver:
            selected = False
            deliver_items = sections.deliver_screen()
            invisible_surface_2 = deliver_items[0]
            invisible_rect_2 = deliver_items[1]
            if current_pizza != None:
                current_pizza.change_position(WIDTH * .52, WIDTH * .375, 275)
                current_pizza.base.move(WIDTH * .52, WIDTH * .375)
                current_pizza.base.radius = 275
                available_items = current_pizza.draw_pizza(400)
        elif show_settings:
            quit_button, tut_button = sections.settings_screen()
        elif show_tutorial:
            sections.show_tutorial()
        if not show_order_event:
            toggles = sections.toggle(waiting_customers)

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
                    elif tut_button.collidepoint(pos):
                        show_tutorial = visible_station(show_tutorial)
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
                            item.order = generate_order.order()
                            temp_customer = sections.order_event(item)
                            show_order_event = visible_station(show_order_event)
                elif show_make:
                    if create_toggles[0].get_rect(topleft=(WIDTH * .75, HEIGHT * .4)).collidepoint(pos) and current_pizza == None:
                            pizza_list += [pizza()]
                            current_pizza = pizza_list[-1]
                    elif create_toggles[1].get_rect(topleft=(WIDTH*.09, HEIGHT*.53)).collidepoint(pos) and current_pizza != None:
                        current_pizza.add_topping(cheese=True)
                    elif create_toggles[2].get_rect(topleft=(WIDTH * .18, HEIGHT * .53)).collidepoint(pos) and current_pizza != None:
                        current_pizza.add_topping(sauce=True)
                    elif create_toggles[3].get_rect(topleft=(WIDTH*.27, HEIGHT*.53)).collidepoint(pos) and current_pizza != None:
                        current_pizza.add_topping(toppings="pepperoni")
                    elif create_toggles[4].get_rect(topleft=(WIDTH*.09, HEIGHT*.67)).collidepoint(pos) and current_pizza != None:
                        current_pizza.add_topping(toppings="mushroom")
                    elif create_toggles[5].get_rect(topleft=(WIDTH*.18, HEIGHT*.67)).collidepoint(pos) and current_pizza != None:
                        current_pizza.add_topping(toppings="onion")
                    elif create_toggles[6].get_rect(topleft=(WIDTH*.27, HEIGHT*.67)).collidepoint(pos) and current_pizza != None:
                        current_pizza.add_topping(toppings="pineapple")
                elif show_bake:
                    if current_pizza != None:
                        if current_pizza.base.get_rect().collidepoint(pos):
                            selected = True
                elif show_deliver:
                    if invisible_rect_2 != None:
                        if invisible_rect_2.collidepoint(pos):
                            if len(waiting_customers) != 0:
                                print("delivered!")
                                bake_x = WIDTH * .08
                                bake_y = HEIGHT * .7
                                current_pizza = None
                                del waiting_customers[0]
                elif show_tutorial:
                    show_settings = visible_station(show_settings)

        # Drag Check
        elif event.type == pygame.MOUSEBUTTONUP:
            # If GAME is visible
            if show_game:
                if show_bake:
                    if current_pizza is not None:
                        selected = False
                        if current_pizza.base.get_rect().colliderect(invisible_rect):
                            current_pizza.base.baked = True


    # Display Update
    pygame.display.update()

# Quit
pygame.quit()