# Main File
import os
import pygame
import random
import stations

# Basic Setup
pygame.init()
run = True
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flatbread Fiasco!')

### --- Graphics --- ###
# Constant Graphics
logo = pygame.image.load("graphics/logo.png")
# Title graphics
title_title = pygame.font.SysFont("Arial", 100)
title_txtsurf = title_title.render("Placeholder", True, (255, 255, 255, 255))
new_button = pygame.Rect((WIDTH*.1, HEIGHT//3, 200, 200))
load_button = pygame.Rect((WIDTH*.75, HEIGHT//3, 200, 200))

# Visibility Variables
show_title = True
show_game = False

# Functions
def title():
    global logo
    screen.fill((255, 120, 120, 200))
    logo = pygame.transform.scale(logo, (620, 500))
    screen.blit(logo, (WIDTH//4, HEIGHT//5))
    screen.blit(title_txtsurf, (WIDTH//3, HEIGHT//15))
    pygame.draw.rect(screen, (255, 255, 255, 255), new_button, 400, 20)
    pygame.draw.rect(screen, (255, 255, 255, 255), load_button, 400, 20)

# Main Loop
while run:
    # Check Visibility
    if show_title:
        title()

    elif show_game:
        stations.order_screen()

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
                if new_button.collidepoint(pos):
                    show_title = False
                    show_game = True

    # Display Update
    pygame.display.update()

# Quit
pygame.quit()