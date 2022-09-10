#Modul is setting up all objects loaded at the start of game
import pyglet
import random
from . import resources, util, physycalobjects

def asteroids (number_of_asteroids, player_position, batch=None):
    asteroids = []
    for i in range(number_of_asteroids):
        asteroid_x, asteroid_y = player_position
        while util.distance((asteroid_x, asteroid_y), player_position) < 200: 
            asteroid_x = random.randint(0, 1280)
            asteroid_y = random.randint(0, 740)
        new_asteroid = physycalobjects.PhysycalObjects(img=resources.asteroid_image,
                                            x=asteroid_x, y=asteroid_y, batch=batch)
        new_asteroid_rotation = random.randint(0, 360)
        new_asteroid.speed_x, new_asteroid.speed_y = random.random() * 60, random.random() * 60
        asteroids.append(new_asteroid)
    return asteroids