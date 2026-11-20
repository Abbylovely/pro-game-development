import pgzrun
import pygame
from random import randint

WIDTH = 800
HEIGHT = 600

stars = Actor("star")
stars.pos = (randint(0, WIDTH), randint(0, HEIGHT))

space_ship = Actor("spaceship")
space_ship.pos = (WIDTH // 2, HEIGHT // 2)


def draw():
    screen.clear()
    stars.draw()
    space_ship.draw()

def update():
    pass

pgzrun.go()