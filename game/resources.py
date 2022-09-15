import pyglet

def center_image(image):
    """
    Sets image anchor to center of the image
    """
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2
    

#Get resource path
pyglet.resource.path = ['../resources']

#Reindex image
pyglet.resource.reindex()

#Load player ship image
player_image = pyglet.resource.image("player_ship_1.png")
center_image(player_image)

#Load asteroid image
asteroid_image = pyglet.resource.image("asteroid.png")
center_image(asteroid_image)

#Load player laser image
laser_image = pyglet.resource.image("player_laser.png")
center_image(laser_image)

#Load rear engine flame image
engine_flame_image = pyglet.resource.image("engine_flame.png")
engine_flame_image.anchor_x = engine_flame_image.width / 2
engine_flame_image.anchor_y = engine_flame_image.height * 1.7
