# Main File
import os
import pygame
import random
import sections

# Basic Setup
pygame.init()
run = True
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flatbread Fiasco!')

### --- Graphics --- ###

# Visibility Variables
show_title = True
show_game = False
show_order = False
show_make = False
show_bake = False
show_deliver = False

# Misc
toggles = []

# Main Loop
while run:
    # Check Visibility
    if show_title:
        buttons = sections.title()

    elif show_game:
        if show_order:
            sections.order_screen()
        toggles = sections.toggle()

    # Mouse Position
    pos = pygame.mouse.get_pos()

    # Event Check
    for event in pygame.event.get():
        # Quit Check
        if event.type == pygame.QUIT:
            run = False
        # Mouse Click Check
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if show_title:
                if buttons[0].get_rect(topleft=(WIDTH*.03, HEIGHT//2)).collidepoint(pos):
                    show_title = False
                    show_game = True
                    show_order = True
                elif buttons[1].get_rect(topleft=(WIDTH*.73, HEIGHT//2)).collidepoint(pos):
                    show_title = False
                    show_game = True
                    show_order = True
            if show_game:
                for toggle in toggles:
                    if toggle.get_rect(topleft=()).collidepoint(pos):
                        print("toggle")

    # Display Update
    pygame.display.update()

# Quit
pygame.quit()