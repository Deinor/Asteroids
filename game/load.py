#Modul is setting up all objects loaded at the start of game
import pyglet
import random
from . import util, asteroid

def asteroids_big (number_of_asteroids_big, player_position, batch=None):
    asteroids = []
    for i in range(number_of_asteroids_big):
        asteroid_x, asteroid_y = player_position
        while util.distance((asteroid_x, asteroid_y), player_position) < 200: 
            asteroid_x = random.randint(0, 1280)
            asteroid_y = random.randint(0, 740)
        new_asteroid = asteroid.AsteroidBig(x=asteroid_x, y=asteroid_y, batch=batch)
        new_asteroid.rotation = random.randint(0.0, 360.0)
        new_asteroid.speed_x, new_asteroid.speed_y = random.random() * 60, random.random() * 60
        asteroids.append(new_asteroid)
    return asteroids 

def asteroids_medium (number_of_asteroids_medium, player_position, batch=None):
    asteroids_medium = []
    for i in range(number_of_asteroids_medium):
        asteroid_x, asteroid_y = player_position
        while util.distance((asteroid_x, asteroid_y), player_position) < 200: 
            asteroid_x = random.randint(0, 1280)
            asteroid_y = random.randint(0, 740)
        new_asteroid = asteroid.AsteroidMedium(x=asteroid_x, y=asteroid_y, batch=batch)
        new_asteroid.rotation = random.randint(0.0, 360.0)
        new_asteroid.speed_x, new_asteroid.speed_y = random.random() * 60, random.random() * 60
        asteroids_medium.append(new_asteroid)
    return asteroids_medium 