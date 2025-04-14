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

# Main Loop
while run:
    # Check Visibility
    if show_title:
        buttons = sections.title()

    elif show_game:
        sections.order_screen()

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
                if buttons[0].collidepoint(pos):
                    show_title = False
                    show_game = True

    # Display Update
    pygame.display.update()

# Quit
pygame.quit()