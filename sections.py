# Stations
import os
import random
import pygame

# Basic Setup
pygame.init()
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Title Graphics
logo = pygame.image.load("graphics/logo.png")
title_title = pygame.font.SysFont("Arial", 100)
title_txtsurf = title_title.render("Placeholder", True, (255, 255, 255, 255))
new_button = pygame.Rect((WIDTH*.1, HEIGHT//3, 200, 200))
load_button = pygame.Rect((WIDTH*.75, HEIGHT//3, 200, 200))

def title():
    global logo, new_button, load_button
    screen.fill((255, 120, 120, 200))
    logo = pygame.transform.scale(logo, (620, 500))
    screen.blit(logo, (WIDTH//4, HEIGHT//5))
    screen.blit(title_txtsurf, (WIDTH//3, HEIGHT//15))
    pygame.draw.rect(screen, (255, 255, 255, 255), new_button, 400, 20)
    pygame.draw.rect(screen, (255, 255, 255, 255), load_button, 400, 20)
    return new_button, load_button


# Order Graphics
order_screen_image = pygame.image.load("graphics/order_screen.jpg")
def order_screen():
    screen.fill((255, 120, 120, 200))
    screen.blit(order_screen_image, (0, 0))
