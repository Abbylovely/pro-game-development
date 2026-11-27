import pgzrun
import pygame
from random import randint

WIDTH = 800
HEIGHT = 600
game_over = False

stars = Actor("star")
stars.pos = (randint(0, WIDTH), randint(0, HEIGHT))

space_ship = Actor("spaceship")
space_ship.pos = (WIDTH // 2, HEIGHT // 2)


def draw():
    screen.clear()
    stars.draw()
    space_ship.draw()

def update():
    if keyboard.left:
        space_ship.x -= 10
    if keyboard.right:
        space_ship.x += 10
    if keyboard.up:
        space_ship.y -= 10
    if keyboard.down:
        space_ship.y += 10

    # Keep the spaceship within the screen boundaries
    space_ship.x = max(0, min(WIDTH, space_ship.x))
    space_ship.y = max(0, min(HEIGHT, space_ship.y))

    if space_ship.colliderect(stars):
        stars.pos = (randint(0, WIDTH), randint(0, HEIGHT))
def time_up():
    global game_over
    game_over = True
clock.schedule(time_up, 30.0)  # Set the game duration to 30 seconds

pgzrun.go()