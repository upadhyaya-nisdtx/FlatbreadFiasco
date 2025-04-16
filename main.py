# Main File
import pygame
import sections
from customer import customer

# Basic Setup
pygame.init()
run = True
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flatbread Fiasco!')

### --- Graphics --- ###

# Cursor
pygame.mouse.set_visible(False)
cursor = pygame.image.load("graphics/pizza_cursor.png")
cursor = pygame.transform.scale(cursor, (35, 35))

# Visibility Variables
show_title = True
show_game = False
show_order = False
show_make = False
show_bake = False
show_deliver = False
show_settings = False

def visible_station(show_variable, boolean=True):
    global show_order, show_make, show_bake, show_deliver, show_settings
    show_order = False
    show_make = False
    show_bake = False
    show_deliver = False
    show_settings = False
    show_variable = boolean
    return show_variable

# Misc
toggles = sections.toggle()
quit_button = sections.settings_screen()
customers = []
time_1 = pygame.time.get_ticks()
time_2 = 0

# Main Loop
while run:
    # Check Visibility
    if show_title:
        buttons = sections.title()
    elif show_game:
        # Time Check
        time_2 = pygame.time.get_ticks()
        if time_2 - time_1 >= 6000 and len(customers) <= 4:
            customers.append(customer())
            time_1 = pygame.time.get_ticks()
            for i in range(len(customers)):
                customers[i].set_x(i * 200)
        if show_order:
            sections.order_screen(customers)
        elif show_make:
            sections.make_screen()
        elif show_bake:
            sections.bake_screen()
        elif show_deliver:
            sections.deliver_screen()
        elif show_settings:
            quit_button = sections.settings_screen()
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
            # If TITLE is visible
            if show_title:
                if buttons[0].get_rect(topleft=(WIDTH*.03, HEIGHT//2)).collidepoint(pos):
                    show_title = False
                    show_game = True
                    show_order = True
                elif buttons[1].get_rect(topleft=(WIDTH*.73, HEIGHT//2)).collidepoint(pos):
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
                        show_settings = visible_station(show_settings, False)
                        show_title = True


    # Display Update
    pygame.display.update()

# Quit
pygame.quit()