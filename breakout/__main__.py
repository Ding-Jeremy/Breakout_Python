# name:     main.py
# author:
# date:     02.12.2024
#
# descrption: This file is ran by calling "python -m breakout". It runs the game

import pygame
from . import Breakout
import sys

# Initialize pygame
pygame.init()

# Set up the screen dimensions and create a window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Breakout Game")

# Set up the clock for managing the frame rate
clock = pygame.time.Clock()

# Main loop
running = True

# Create a Breakout object
breakout = Breakout(screen)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draws background
    screen.fill("white")
    # Draws game
    breakout.show()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate to 60 frames per second
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()