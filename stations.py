# Stations
import os
import random
import pygame

# Basic Setup
pygame.init()
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def order_screen():
    screen.fill((255, 120, 120, 200))